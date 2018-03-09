from PairWise.models import LanguageTag, ConceptTag, FrameworkTag, LocationTag,\
                            Course, CourseOffering, CourseSection, Term,\
                            Group, GroupSearchEntry, UserSearchEntry, Profile
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


def fetch_languages():
    return list(LanguageTag.objects.all())


def fetch_concepts():
    return list(ConceptTag.objects.all())


def fetch_frameworks():
    return list(FrameworkTag.objects.all())


def fetch_locations():
    return list(LocationTag.objects.all())


def fetch_course_by_course_code(code):
    return Course.objects.get(course_code=code)


def fetch_course_by_subtitle(subtitle):
    return Course.objects.get(name=subtitle)


def fetch_term_by_time_of_year(year, term_code):
    return Term.objects.get(year=year, term=term_code)


def fetch_offering_by_term(course, term):
    return CourseOffering.objects.get(course=course, term=term)


def fetch_course_section_by_name(offr, name):
    try:
        return CourseSection.objects.get(offering=offr, section_name=name)
    except ObjectDoesNotExist:
        return None


def fetch_user_by_username(name):
    return User.objects.get(username=name)


def fetch_user_by_name_email(first, last, email):
    return User.objects.get(first_name=first, last_name=last, email=email)


def fetch_group_by_member(member, offering):
    try:
        return Group.objects.get(members=member, category=offering)
    except ObjectDoesNotExist:
        return None


def fetch_search_by_user(user, offering):
    try:
        if isinstance(user, User):
            return UserSearchEntry.objects.get(host=user, category=offering)
        else:
            my_group = fetch_group_by_member(user, offering)
            return GroupSearchEntry.objects.get(host=my_group, host__category=offering)
    except ObjectDoesNotExist:
        return None