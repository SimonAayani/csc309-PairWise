from PairWise_Server.models import AvailableSearchEntry, AbandonedSearchEntry, UserSearchData, SearchResultsCache
from django.db.models import Count, Q, F


def cancel_search(user, offering):
    AvailableSearchEntry.objects.filter(members__user=user, category=offering).delete()


def mark_search_result(searcher, found, match_coefficient):
    SearchResultsCache.objects.create(searcher=searcher, result=found, match_coefficient=match_coefficient)


def get_marked_results(searcher, category=None):
    if category is None:
        return list(SearchResultsCache.objects.filter(searcher__members__user=searcher))
    else:
        return list(SearchResultsCache.objects.filter(searcher__members__user=searcher,
                                                      searcher__category=category))


def abandon_search(user_search_data):
    search_entry = user_search_data.search
    SearchResultsCache.objects.filter(Q(searcher=search_entry) | Q(result=search_entry)).delete()
    new_abandoned = AbandonedSearchEntry.objects.create(category=search_entry.category,
                                                        title=search_entry.title,
                                                        description=search_entry.description,
                                                        size=search_entry.size,
                                                        capacity=search_entry.capacity,
                                                        required_section=search_entry.required_section,
                                                        quality_cutoff=search_entry.quality_cutoff,
                                                        active_search=search_entry.active_search,
                                                        owner=user_search_data.user)
    new_abandoned.save()
    search_entry.delete()


def recover_search(user, category):
    abandoned_search = AbandonedSearchEntry.objects.get(owner=user, category=category)
    recovered_search = AvailableSearchEntry.objects.create(category=abandoned_search.category,
                                                           title=abandoned_search.title,
                                                           description=abandoned_search.description,
                                                           size=abandoned_search.size,
                                                           capacity=abandoned_search.capacity,
                                                           required_section=abandoned_search.required_section,
                                                           quality_cutoff=abandoned_search.quality_cutoff,
                                                           active_search=abandoned_search.active_search)
    recovered_search.save()

    search_criteria = UserSearchData.objects.get(user=user, course_section__offering=category)
    search_criteria.search = recovered_search
    search_criteria.save()

    update_cache(recovered_search)
    abandoned_search.delete()


def get_search_targets(search_entry, sections):
    condition = Q(required_section=sections[0])
    if len(sections) > 1:
        for section in sections[1:]:
            condition &= Q(required_section=section)

    targets = AvailableSearchEntry.objects.filter(category=search_entry.category,
                                                  size__lte=(F('capacity') - search_entry.size)) \
                                          .exclude(Q(id=search_entry.id))
    if search_entry.required_section is not None:
        targets = targets.exclude(~Q(members__course_section=search_entry.required_section))

    return targets


def get_annotated_results(search_entry):
    skill_reqs = []
    locations = []
    sections = []
    for user_search in search_entry.members.all():
        skill_reqs.extend(list(user_search.user.profile_set.all()[0].skills.all()))
        locations.append(user_search.location)
        sections.append(user_search.course_section)

    targets = get_search_targets(search_entry, sections)

    my_match_filter = Q(members__user__profile__skills__in=skill_reqs)
    other_match_filter = Q(members__desired_skills__in=skill_reqs)

    # Additional conditions: Section, location
    results = targets.annotate(my_match_coeff=(Count('members__user__profile__skills', filter=my_match_filter)),
                               other_match_coeff=Count('members__desired_skills', filter=other_match_filter),
                               location_bonus=Count('members__location', filter=Q(members__location__in=locations)),
                               section_bonus=Count('members__course_section',
                                                   filter=Q(members__course_section__in=sections)))
    return results


def measure_matches_as_searcher(search_entry):
    results = get_annotated_results(search_entry)
    matches = results.annotate(abs_match_coeff=(F('my_match_coeff') * 60 + F('other_match_coeff') * 15 +
                                                F('section_bonus') * 15 + F('location_bonus') * 5)
                               ).filter(abs_match_coeff__gte=search_entry.quality_cutoff).order_by('-abs_match_coeff')

    for match in matches:
        mark_search_result(search_entry, match, match.abs_match_coeff)


def measure_matches_as_search_target(search_entry):
    results = get_annotated_results(search_entry)
    matches = results.annotate(abs_match_coeff=(F('my_match_coeff') * 15 + F('other_match_coeff') * 60 +
                                                F('section_bonus') * 15 + F('location_bonus') * 5)
                               ).filter(abs_match_coeff__gte=search_entry.quality_cutoff).order_by('-abs_match_coeff')

    for match in matches:
        mark_search_result(search_entry, match, match.abs_match_coeff)


def update_cache(search_entry):
    SearchResultsCache.objects.filter(Q(searcher=search_entry) | Q(result=search_entry)).delete()
    measure_matches_as_searcher(search_entry)
    measure_matches_as_search_target(search_entry)
