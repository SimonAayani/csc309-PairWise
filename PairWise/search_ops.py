from PairWise.models import Searching, Results, Group
from django.contrib.auth.models import User


def enter_search(user_id, course_section, search_active=True):
    Searching.objects.create(user_id, course_section, search_active)


def cancel_search(user_id, course_section):
    Searching.objects.filter(user_id=user_id, section_id=course_section).delete()

    group = Group.objects.filter(course_id=course_section, members__id=user_id)
    if group.exists():
        Searching.objects.filter(searcher=group.leader).delete()


def get_available_groups(user_id, course, term):
    searchers = list(User.objects.filter(searching__coursesection__courseterm__course__course_id=course,
                                         searching__coursesection__courseterm__term_id=term).exclude(
                                             id=user_id).prefetch_related('group_set'))

    for ind in range(len(searchers)):
        searcher = searchers[ind]
        if searcher.group_set.filter(coursesection__courseterm__course__course_id=course,
                                     coursesection__courseterm__term_id=term).exists():
            searchers[ind] = searcher.group_set.get(coursesection__courseterm__course__course_id=course,
                                                    coursesection__courseterm__term_id=term)

    return searchers


def mark_search_result(searcher, found):
    for result in found:
        Results.objects.create(searcher=searcher, result=result)


def get_marked_results(searcher):
    return list(Results.objects.filter(searcher=searcher))


def get_past_group_members(user_id):
    my_member_groups = Group.objects.select_related('members').get(id=user_id)
    my_leader_groups = Group.objects.filter(leader=user_id)
    my_member_groups.union(my_leader_groups)

    return list(group.members for group in my_member_groups)
