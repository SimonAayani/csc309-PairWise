from PairWise.models import SearchEntry, UserSearchEntry, GroupSearchEntry, SearchResultsCache, Group, Profile
from django.contrib.auth.models import User
from django.db.models import Count, Sum, Q


def enter_search(user_id, course_section, search_active=True):
    SearchEntry.objects.create(user_id, course_section, search_active)


def cancel_search(user_id, course_section):
    SearchEntry.objects.filter(user_id=user_id, section_id=course_section).delete()


def get_available_groups(user_id, offering, term):
    searchers = list(User.objects.filter(searchentry__courseoffering__id=offering,
                                         searchentry__courseoffering__term__id=term).exclude(id=user_id))

    for ind in range(len(searchers)):
        print(type(searchers[ind]))

    return searchers


def mark_search_result(searcher, found):
    for result in found:
        SearchResultsCache.objects.create(searcher=searcher, result=result)


def get_marked_results(searcher):
    return list(SearchResultsCache.objects.filter(searcher=searcher))


def get_past_group_members(user_id):
    my_member_groups = Group.objects.filter(members__id=user_id)

    return list(group.members for group in my_member_groups)


def measure_matches(user, cutoff=0):
    my_search_entry = UserSearchEntry.objects.get(host=user)
    my_match_filter = Q(host__profile__skills__in=list(my_search_entry.desired_fields))
    num_fields = my_search_entry.desired_fields.count()
    other_match_filter = Q(desired_fields__in=list(my_search_entry.host__profile__skills))

    UserSearchEntry.objects.exclude(host=user).annotate(match_coeff=(Count('host__profile__skills',
                                                                           filter=my_match_filter)
                                                                     / num_fields) * 75
                                                                  + (Count('desired_fields',
                                                                           filter=other_match_filter)
                                                                     / Count('desired_fields')) * 25)

    my_match_filter = Q(host__members__profile__skills__in=list(my_search_entry.desired_fields))
    GroupSearchEntry.objects.annotate(match_coeff=(Count('host__members__profile__skills',
                                                         filter=my_match_filter) / num_fields) * 75
                                                + (Count('desired_fields',
                                                         filter=other_match_filter) / Count('desired_fields')) * 25)

    singles = list(UserSearchEntry.objects.filter(match_coeff__gt=cutoff).order_by('match_coeff'))
    groups = list(GroupSearchEntry.objects.filter(match_coeff__gt=cutoff).order_by('match_coeff'))
    combined = []

    i = 0
    j = 0
    while i < len(singles) and j < len(groups):
        if singles[i].match_coeff > groups[j].match_coeff:
            combined.append(singles[i])
        else:
            combined.append(groups[i])

    combined.extend(groups[j:])
    combined.extend(singles[i:])

    return combined
