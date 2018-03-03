from PairWise.models import Searching, Results, Group
from django.db.models.query_utils import Q


def add_to_group(newcomer, group_lead, course_section):
    old_group = group_lead.group_set.filter(course_id=course_section)
    if old_group.exists():
        old_group.members.add(newcomer)
        Searching.objects.filter(user_id=newcomer).delete()
        Results.objects.filter(searcher=newcomer).delete()
        Results.objects.filter(result=newcomer).update(result=group_lead)
        old_group.size += 1

        if old_group.size == old_group.capacity:
            Searching.objects.filter(user_id=group_lead).delete()
            Results.objects.filter(Q(searcher=group_lead) | Q(result=group_lead)).delete()

        old_group.save()
    else:
        new_group = Group()
        new_group.section_id = course_section
        new_group.members.add(group_lead, newcomer)
        new_group.size = 2

        new_group.save()


def remove_from_group(user_id, course_id):
    my_group = Group.objects.filter(course_id=course_id).select_related(members__user_id=user_id)
    if my_group.leader == user_id:
        new_leader = my_group.members[0]
        my_group.members.remove(new_leader)
        my_group.leader = new_leader

        for searching_for_me in Searching.objects.filter(result=user_id):
            Searching.objects.create(searcher=searching_for_me.searcher, result=new_leader)

        for found_by_my_group in Searching.objects.filter(searcher=user_id):
            Searching.objects.create(searcher=new_leader, result=found_by_my_group)
    else:
        my_group.members.remove(user_id)

        for searching_for_my_group in Searching.objects.filter(result=my_group.leader):
            Searching.objects.create(searcher=searching_for_my_group.user_id, result=user_id)

        for found_by_my_group in Searching.objects.filter(searcher=my_group.leader):
            Searching.objects.create(searcher=user_id, result=found_by_my_group.user_id)

    if my_group.size == 2:
        my_group.delete()
    else:
        my_group.size -= 1
        my_group.save()