from PairWise_Server.models import UserSearchEntry, GroupSearchEntry, SearchResultsCache,\
                                   NewNotification, CourseOffering
from django.db.models import F, ObjectDoesNotExist
from django.db.models.query_utils import Q
from django.db.transaction import atomic


def add_to_group(newcomer, inviter, offering):

    try:
        old_group = GroupSearchEntry.objects.get(members__user=inviter, category=offering)
        SearchResultsCache.objects.filter(searcher=newcomer).delete()
        SearchResultsCache.objects.filter(result=newcomer).update(result=old_group)

        old_group.members.add(newcomer)
        old_group.size += 1

        UserSearchEntry.objects.filter(host=newcomer).delete()

        if old_group.size == old_group.capacity:
            GroupSearchEntry.objects.filter(host=old_group).delete()
            SearchResultsCache.objects.filter(Q(searcher=old_group) | Q(result=old_group)).delete()

        old_group.save()
    except ObjectDoesNotExist:
        old_search_entry = UserSearchEntry.objects.get(host__user=inviter)
        my_search_entry = UserSearchEntry.objects.get(host__user=newcomer)

        new_group = GroupSearchEntry.objects.create(category=offering, title=old_search_entry.title, description=old_search_entry.description)
        new_group.capacity = old_search_entry.capacity
        new_group.required_section = old_search_entry.required_section
        new_group.quality_cutoff = (old_search_entry.quality_cutoff + my_search_entry.quality_cutoff) / 2

        new_group.members.add(old_search_entry.host, my_search_entry.host)
        new_group.size = 2

        with atomic():
            new_group.save()
            old_search_entry.delete()
            my_search_entry.delete()
        # Create a group search entry with two members
        # new_group = GroupSearchEntry.objects.create(offering=offering, capacity=capacity, size=2)
        # new_group.members.add(inviter, newcomer)
        # new_group.save()
        #
        # UserSearchEntry.objects.filter(host__in=[newcomer, inviter]).delete()


def remove_from_group(user, category):
    my_group = GroupSearchEntry.objects.get(members__user=user, offering=category)

    new_search = _transfer_state_from_group(user, my_group)
    _transfer_searches_from_group(my_group, new_search)

    if my_group.size == 2:
        other_user = my_group.members.get().id

        new_search = _transfer_state_from_group(other_user, my_group)
        _transfer_searches_from_group(my_group, new_search)

        GroupSearchEntry.objects.delete(host=my_group)
        my_group.delete()
    else:
        my_group.members.remove(user)
        my_group.size = F('size') - 1
        my_group.save()


def _transfer_state_from_group(user, group):
    try:
        my_search_entry = GroupSearchEntry.objects.get(host=group)
        my_new_search = UserSearchEntry(host=user, category=my_search_entry.category, subhead=my_search_entry.subhead,
                                        capacity=my_search_entry.capacity, description=my_search_entry.description,
                                        desired_fields=my_search_entry.desired_fields)
        my_new_search.save()
        return my_new_search
    except ObjectDoesNotExist:
        return None


def _transfer_searches_from_group(my_group, my_search):
    for searching_for_my_group in SearchResultsCache.objects.filter(result__groupsearchentry__host=my_group):
        SearchResultsCache.objects.create(searcher=searching_for_my_group, result__host=my_search)

    for found_by_my_group in SearchResultsCache.objects.filter(searcher__groupsearchentry__host=my_group):
        SearchResultsCache.objects.create(searcher=my_search, result=found_by_my_group.id)


def send_invite(sender, receiver, category, msg_text=None):

    if msg_text is None:
        msg_text = "{0} {1} ({2}) wants to invite you to a {3} group!".format(sender.first_name, sender.last_name, sender.username, category.course.course_code)

    msg = NewNotification.objects.get_or_create(sender=sender, receiver=receiver, category=category, is_invite=True)[0]
    msg.text = msg_text
    msg.save()
