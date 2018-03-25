from PairWise_Server.models import SearchEntry, UserSearchEntry, GroupSearchEntry, SearchResultsCache,\
                                   CourseOffering, Course
from django.contrib.auth.models import User
from django.db.models import Count, Q, F
from PairWise_Server.fetch import fetch_user_by_username, fetch_term_by_time_of_year,\
                                  fetch_offering_by_term, fetch_course_by_course_code


def cancel_search(user, course_section):
    if isinstance(user, User):
        UserSearchEntry.objects.filter(host=user, category=course_section).delete()
    else:
        GroupSearchEntry.objects.filter(members__user=user, category=course_section).delete()


def mark_search_result(searcher, found):
    for result in found:
        SearchResultsCache.objects.create(searcher=searcher, result=result)


def get_marked_results(searcher, category=None):
    if category is None:
        return list(SearchResultsCache.objects.filter(searcher__usersearchentry__host=searcher))
    else:
        return list(SearchResultsCache.objects.filter(searcher__usersearchentry__host=searcher, searcher_category=category))


def get_past_group_members(user):
    my_member_groups = GroupSearchEntry.objects.filter(members__user=user)

    return list(group.members for group in my_member_groups)


def measure_matches_user_to_user(user_search_entry, cutoff=0):
    category = user_search_entry.category
    my_match_filter = Q(host__user__profile__skills__in=list(user_search_entry.host.desired_skills.all()))
    other_match_filter = Q(host__desired_skills__in=list(user_search_entry.host.user.profile_set.all()[0].skills.all()))

    if user_search_entry.required_section is None:
        targets = UserSearchEntry.objects.filter(category=category).exclude(host=user_search_entry.host)
    else:
        targets = UserSearchEntry.objects.filter(category=category, host__course_section=user_search_entry.required_section).exclude(host=user_search_entry.host)

    # Additional conditions: Section, location
    results = targets.annotate(my_match_coeff=Count('host__user__profile__skills', filter=my_match_filter),
                               other_match_coeff=Count('host__desired_skills', filter=other_match_filter),
                               location_bonus=Count('host__location', filter=Q(host__location=user_search_entry.host.location)),
                               section_bonus=Count('host__course_section', filter=Q(host__course_section=user_search_entry.host.course_section)))
    print(results)
    matches = results.annotate(abs_match_coeff=(F('my_match_coeff') * 60 + F('other_match_coeff') * 15 +
                                                F('section_bonus') * 15 + F('location_bonus') * 5)
                               ).filter(abs_match_coeff__gte=cutoff).order_by('-abs_match_coeff')

    for match in matches:
        SearchResultsCache.objects.create(searcher=user_search_entry, result=match, match_coefficient=match.abs_match_coeff)



def measure_matches_user_to_group(user_search_entry, cutoff=0):
    category = user_search_entry.category
    my_match_filter = Q(members__user__profile__skills__in=list(user_search_entry.host.desired_skills.all()))
    group_match_filter = Q(
        members__desired_skills__in=list(user_search_entry.host.user.profile_set.all()[0].skills.all()))
    targets = GroupSearchEntry.objects.filter(category=category)
    results = targets.annotate(my_match_coeff=Count('members__user__profile__skills', filter=my_match_filter),
                               other_match_coeff=Count('members__desired_skills', filter=group_match_filter))
    groups = results.annotate(abs_match_coeff=(F('my_match_coeff') * 0.75 + F('other_match_coeff') * 0.25)
                              ).filter(abs_match_coeff__gte=cutoff).order_by('-abs_match_coeff')