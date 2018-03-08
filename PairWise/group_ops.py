from PairWise.models import UserSearchEntry, GroupSearchEntry, SearchEntry, SearchResultsCache, Group
from django.db.models import F
from django.db.models.query_utils import Q


def add_to_group(newcomer, inviter, course_offr, capacity=2):
    old_group = Group.objects.filter(members__id=inviter, offering=course_offr)

    if old_group.exists():
        old_group.members.add(newcomer)
        old_group.size += 1
        SearchResultsCache.objects.filter(searcher=newcomer).delete()
        SearchResultsCache.objects.filter(result=newcomer).update(result=old_group.id)
        UserSearchEntry.objects.filter(host=newcomer).delete()

        if old_group.size == old_group.capacity:
            GroupSearchEntry.objects.filter(host=old_group.id).delete()
            SearchResultsCache.objects.filter(Q(searcher=old_group.id) | Q(result=old_group.id)).delete()

        old_group.save()
    else:
        new_group = Group(offering=course_offr, capacity=capacity, size=2)
        new_group.members.add(old_group.id, newcomer)
        new_group.save()


def remove_from_group(user_id, category):
    my_group = Group.objects.filter(course_id=category, members__id=user_id).prefetch_related('members')

    new_search_id = transfer_state_from_group(user_id, my_group.id)
    transfer_searches(user_id, new_search_id)

    if my_group.size == 2:
        other_user_id = my_group.members.get().id

        new_search_id = transfer_state_from_group(other_user_id, my_group.id)
        transfer_searches(other_user_id, new_search_id)

        GroupSearchEntry.objects.get(host=my_group.id).delete()
        my_group.delete()
    else:
        my_group.members.remove(my_group.members.get(id=user_id))
        my_group.size = F('size') - 1


def transfer_state_from_group(user_id, group_id):
    my_search_entry = GroupSearchEntry.objects.get(host=group_id)
    my_new_search = UserSearchEntry(host=user_id, category=my_search_entry.category, subhead=my_search_entry.subhead,
                                    capacity=my_search_entry.capacity, description=my_search_entry.description,
                                    desired_fields=my_search_entry.desired_fields)
    my_new_search.save()
    return my_new_search.id


def transfer_searches(my_group_id, my_search_id):
    for searching_for_my_group in SearchResultsCache.objects.filter(result=my_group_id):
        SearchResultsCache.objects.create(searcher=searching_for_my_group.id, result=my_search_id)

    for found_by_my_group in SearchResultsCache.objects.filter(searcher=my_group_id):
        SearchResultsCache.objects.create(searcher=my_search_id, result=found_by_my_group.id)
