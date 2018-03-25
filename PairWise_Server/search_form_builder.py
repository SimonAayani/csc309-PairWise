from PairWise_Server.fetch import fetch_user_by_username, fetch_course_by_course_code, fetch_most_recent_term,\
                                  fetch_offering_by_term, fetch_course_section_by_name
from PairWise_Server.models import SkillTag, LocationTag, UserSearchData, UserSearchEntry, CourseOffering


class SearchFormBuilder:
    def __init__(self, user, course):
        if user is None:
            print("User is wrong")
            raise ValueError("User must be of type User (is {0})".format(type(user)))
        elif course is None or type(course) != CourseOffering:
            print("Course is wrong")
            raise ValueError("Course must be of type Course (is {0})".format(type(course)))

        self._student = user
        self._course = course

        self._course_section = None
        self._requre_same_section = False
        self._skills = []
        self._preferred_location = None
        self._capacity = 2
        self._title = ""
        self._description = ""
        self._cutoff = 0
        self._active_search = True


    def set_course_section(self, section):
        if section is None or type(section) != str:
            raise ValueError("Section code must be a string (is {0})".format(section))
        elif not section.startswith("L"):
            raise ValueError("Section code must begin with L (is {0})".format(section))

        self._course_section = fetch_course_section_by_name(self._course, section)

        if self._course_section is None:
            raise ValueError("No section {0} for selected course".format(section))

        return self

    def require_same_section(self):
        self._requre_same_section = True
        return self

    def add_skill(self, tag_id):
        if tag_id is None or type(tag_id) != int:
            raise ValueError("Tag ID must be an integer (is {0})".format(tag_id))

        new_tag = SkillTag.objects.get(datatag_ptr_id=tag_id)

        self._skills.append(new_tag)
        return self

    def add_location(self, loc_id):
        if loc_id is None or type(loc_id) != int:
            raise ValueError("Location ID must be an integer (is {0})".format(loc_id))

        self._preferred_location = LocationTag.objects.get(datatag_ptr_id=loc_id)
        return self

    def set_capacity(self, cap):
        if cap is None or type(cap) != int:
            raise ValueError("Capacity must be an integer (is {0})".format(cap))
        elif cap < 2:
            raise ValueError("Capacity must be greater than 1 (is {0})".format(cap))

        self._capacity = cap
        return self

    def set_title(self, title):
        if title is None or type(title) != str:
            raise ValueError("Title must be a string (is {0})".format(title))
        elif len(title) > 255:
            raise ValueError("Title must be shorter than 255 characters (is {0})".format(len(title)))

        self._title = title
        return self

    def set_description(self, descr):
        if descr is None or type(descr) != str:
            raise ValueError("Description must be a string (is {0})".format(descr))

        self._description = descr
        return self

    def set_quality_cutoff(self, cutoff):
        if cutoff is None or type(cutoff) != int:
            raise ValueError("Cutoff value must be an integer (is {0})".format(cutoff))
        elif cutoff < 0:
            raise ValueError("Cutoff value must be positive (is {0})".format(cutoff))

        self._cutoff = cutoff
        return self

    def set_search_inactive(self):
        self._active_search = False
        return self

    def ready_to_build(self):
        return self._course_section is not None

    def build(self):
        if not self.ready_to_build():
            return None
        else:
            search_criteria = UserSearchData.objects.create(user=self._student)
            search_criteria.course_section = self._course_section
            search_criteria.location = self._preferred_location

            for tag in self._skills:
                search_criteria.desired_skills.add(tag)

            search_criteria.save()

            new_search = UserSearchEntry.objects.create(host=search_criteria, category=self._course)

            new_search.capacity = self._capacity
            new_search.title = self._title
            new_search.description = self._description
            new_search.quality_cutoff = self._cutoff
            new_search.active_search = self._active_search

            if self._requre_same_section:
                new_search.reqired_section = self._course_section
            else:
                new_search.reqired_section = None

            new_search.save()
            return new_search