from PairWise.models import SearchEntry, SearchResultsCache, Group
from django.contrib.auth.models import User


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
