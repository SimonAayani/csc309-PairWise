from PairWise_Server.models import LanguageTag, ConceptTag, FrameworkTag, LocationTag,\
                                   Course, CourseOffering, CourseSection, Term,\
                                   GroupSearchEntry, UserSearchEntry, Profile
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


def fetch_languages():
    """
    Returns a list of programming language tags from the database, which represent the whole list of options
    for programming languages a user may report under the skills in their profile, or as group search criteria.
    """
    return list(LanguageTag.objects.all())


def fetch_concepts():
    """
    Returns a list of conceptual area tags (such as machine learning, functional programming, concurrency),
    which represent the whole list of concept options a user may report under the skills in their profile,
    or as group search criteria.
    """
    return list(ConceptTag.objects.all())


def fetch_frameworks():
    """
    Returns a list of frameworks and library tags (such sa web frameworks, DBMS, and oter libraries)
    that a user may report under the skills in their profile, or as group search criteria.
    """
    return list(FrameworkTag.objects.all())


def fetch_locations():
    """
    Returns a list of options a user may choose as their home location for their profile.

    :return: The location tags in the database
    :rtype: list[LocationTag]
    """
    return list(LocationTag.objects.all())


def fetch_course_by_course_code(code):
    """
    Returns the whole course entry that matches the course code (i.e. CSC301) provided, or
    None if no course matches the code. Note that any term information such as H1F must not
    be included, or the match will fail.

    :param code: The course code of a course
    :type code: str
    :return: The course matching the provided course code
    :rtype: Course | None

    :raises: MultipleObjectsReturned
             If multiple courses in the database have the given course code
    """
    try:
        return Course.objects.get(course_code=code)
    except ObjectDoesNotExist:
        return None


def fetch_course_by_subtitle(subtitle):
    """
    Returns the course whose title (e.g. Introduction to Software Engineering) matches the
    string provided.

    :param subtitle:
    :type subtitle:
    :return:
    :rtype:
    """
    return Course.objects.get(name=subtitle)


def fetch_most_recent_term():
    return Term.objects.all().order_by('-year', '-term')[0]


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


def fetch_profile_by_user(user):
    return Profile.objects.get(student=user)


def fetch_group_by_member(member, offering):
    try:
        return GroupSearchEntry.objects.get(members__user=member, category=offering)
    except ObjectDoesNotExist:
        return None


def fetch_search_by_user(user, offering):
    try:
        if UserSearchEntry.objects.filter(host__user=user, category=offering).exists():
            return UserSearchEntry.objects.get(host__user=user, category=offering)
        else:
            return fetch_group_by_member(user, offering)
    except ObjectDoesNotExist:
        return None


if __name__ == '__main__':
    recent = fetch_most_recent_term()
    print("{0} {1}".format(recent.year, recent.term))