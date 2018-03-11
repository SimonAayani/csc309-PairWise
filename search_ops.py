from PairWise.models import SearchEntry, UserSearchEntry, GroupSearchEntry, SearchResultsCache, Group, CourseOffering, Course
from django.contrib.auth.models import User
from django.db.models import Count, Q, F
from PairWise.fetch import fetch_user_by_username, fetch_term_by_time_of_year, fetch_offering_by_term, fetch_course_by_course_code


def enter_search(user, course_section, headline='', descr='', search_active=True, cap=2):
    UserSearchEntry.objects.get_or_create(host=user, category=course_section, subhead=headline,
                                          description=descr, active_search=search_active)


def cancel_search(user, course_section):
    if isinstance(user, User):
        UserSearchEntry.objects.filter(host=user, category=course_section).delete()
    else:
        GroupSearchEntry.objects.filter(host=user, category=course_section).delete()


def mark_search_result(searcher, found):
    for result in found:
        SearchResultsCache.objects.create(searcher=searcher, result=result)


def get_marked_results(searcher, category=None):
    if category is None:
        return list(SearchResultsCache.objects.filter(searcher__usersearchentry__host=searcher))
    else:
        return list(SearchResultsCache.objects.filter(searcher__usersearchentry__host=searcher, searcher_category=category))


def get_past_group_members(user):
    my_member_groups = Group.objects.filter(members=user)

    return list(group.members for group in my_member_groups)


def measure_matches(user, category, cutoff=0):
    my_search_entry = UserSearchEntry.objects.get(host=user, category=category)
    my_match_filter = Q(host__profile__skills__in=list(my_search_entry.desired_fields.all()))
    other_match_filter = Q(desired_fields__in=list(my_search_entry.host.profile.skills.all()))

    # print(UserSearchEntry.objects.filter(category=category).exclude(host=my_search_entry.host))
    targets = UserSearchEntry.objects.filter(category=category).exclude(host=user)
    results = targets.annotate(my_match_coeff=Count('host__profile__skills', filter=my_match_filter),
                               other_match_coeff=Count('desired_fields', filter=other_match_filter))
    singles = results.annotate(abs_match_coeff=(F('my_match_coeff') * 0.75 + F('other_match_coeff') * 0.25)
                               ).filter(abs_match_coeff__gte=cutoff).order_by('-abs_match_coeff')

    my_match_filter = Q(host__members__profile__skills__in=list(my_search_entry.desired_fields.all()))
    targets = GroupSearchEntry.objects.filter(category=category)
    results = targets.annotate(my_match_coeff=Count('host__members__profile__skills', filter=my_match_filter),
                              other_match_coeff=Count('desired_fields', filter=other_match_filter))
    groups = results.annotate(abs_match_coeff=(F('my_match_coeff') * 0.75 + F('other_match_coeff') * 0.25)
                              ).filter(abs_match_coeff__gte=cutoff).order_by('-abs_match_coeff')

    combined = []

    i = 0
    j = 0
    while i < len(singles) and j < len(groups):
        if singles[i].abs_match_coeff > groups[j].abs_match_coeff:
            combined.append(singles[i])
        else:
            combined.append(groups[i])

    combined.extend(groups[j:])
    combined.extend(singles[i:])

    return combined


if __name__ == '__main__':
    alex = fetch_user_by_username('AHurka')
    csc369 = fetch_course_by_course_code('CSC369')
    winter2018 = fetch_term_by_time_of_year(2018, 'S')
    my_class = fetch_offering_by_term(csc369, winter2018)

    enter_search(alex, my_class)
