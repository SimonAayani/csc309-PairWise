from PairWise_Server.models import AvailableSearchEntry, SearchResultsCache, Notification
from PairWise_Server.search_ops import update_cache, abandon_search, recover_search
from django.db.models import F, ObjectDoesNotExist
from django.db.models.query_utils import Q
from django.db.transaction import atomic


def add_to_group(newcomer, inviter, offering):

        old_search_entry = AvailableSearchEntry.objects.get(members__user=inviter, category=offering)
        my_search_entry = AvailableSearchEntry.objects.get(members__user=newcomer, category=offering)
        print(my_search_entry.members.all())

        old_search_entry.quality_cutoff = (old_search_entry.quality_cutoff * old_search_entry.size +
                                           my_search_entry.quality_cutoff * my_search_entry.size) /\
                                          (old_search_entry.size + my_search_entry.size)

        for member in my_search_entry.members.all():
            abandon_search(member)
            member.search = old_search_entry
            member.save()
        old_search_entry.size = F('size') + my_search_entry.size

        old_search_entry.save()
        update_cache(old_search_entry)


def remove_from_group(user, category):
    my_group = AvailableSearchEntry.objects.get(members__user=user, category=category)

    if my_group.size == 1:
        SearchResultsCache.objects.filter(Q(searcher=my_group) | Q(result=my_group)).delete()
        my_group.delete()
    else:
        my_group.size = F('size') - 1
        my_group.save()
        recover_search(user, category)
        update_cache(my_group)


def send_invite(sender, receiver, category):
    msg_text = "{0} {1} ({2}) has invited you to a group for {0}!".format(sender.first_name, sender.last_name,
                                                                          sender.username, category.course.course_code)

    msg, new = Notification.objects.get_or_create(sender=sender, receiver=receiver, category=category)
    msg.text = msg_text
    msg.save()

    
def cancel_invite(sender, receiver, category):
    Notification.objects.filter(sender=sender, receiver=receiver, category=category).delete()
