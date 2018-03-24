from PairWise_Server.fetch import fetch_user_by_username, fetch_course_by_course_code, fetch_most_recent_term,\
                                  fetch_offering_by_term, fetch_course_section_by_name
from PairWise_Server.models import SkillTag, LocationTag, UserSearchEntry


class SearchFormBuilder:
    def __init__(self, user_name, course_code):
        if user_name is None or type(user_name) != str:
            raise ValueError("Student username must be a string (is {0})".format(user_name))
        elif course_code is None or type(course_code) != str:
            raise ValueError("Course code must be a string (is {0})".format(course_code))

        self._student = fetch_user_by_username(user_name)
        course = fetch_course_by_course_code(course_code)

        if course is None:
            raise ValueError("No course found with course code {0}".format(course_code))

        current_term = fetch_most_recent_term()
        self._course = fetch_offering_by_term(course, current_term)

        if self._student is None:
            raise ValueError("No student found with username {0}".format(user_name))
        elif self._course is None:
            raise ValueError("Course {0} is not currently offered".format(course_code))

        self._course_section = None
        self._requre_same_section = False
        self._skills = []
        self._preferred_location = None
        self._title = ""
        self._description = ""
        self._active_search = True


    def set_course_section(self, section):
        if section is None or type(section) != str:
            raise ValueError("Section code must be a string (is {0})".format(section))
        elif not section.startswith("LEC"):
            raise ValueError("Section code must begin with LEC (is {0})".format(section))

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

        self._title = descr
        return self

    def set_search_inactive(self):
        self._active_search = False
        return self

    def ready_to_build(self):
        return self._course_section is not None

    def build(self):
        if self.ready_to_build():
            new_search = UserSearchEntry.objects.create(host=self._student, category=self._course)

            new_search.subhead = self._title
            new_search.description = self._description

            for tag in self._skills:
                new_search.desired_fields.add(tag)

            new_search.active_search = self._active_search
