from PairWise import Profile, Course, SkillTag
from django.db.transaction import atomic


class ProfileBuilder:
    def __init__(self, student_id):
        if student_id is None or type(student_id) != int:
            raise ValueError("Location value must be an integer (is {0})".format(student_id))

        self._student = student_id
        self._course_codes = []
        self._location = None
        self._language_tags = []
        self._concept_tags = []
        self._framework_tags = []
        self._bio = None
        self._pic = None

    def set_location(self, location):
        if location is None:
            raise ValueError("Location value must not be None")
        self._location = location
        return self

    def location_is_set(self):
        return self._location is not None

    def set_bio(self, bio):
        if bio is None:
            raise ValueError("Biography value must not be None")
        self._bio = bio
        return self

    def bio_is_set(self):
        return self._bio is not None

    def set_profile_pic(self, pic):
        if pic is None:
            raise ValueError("Profile picture must not be None")
        self._pic = pic
        return self

    def profile_pic_is_set(self):
        return self._bio is not None

    def add_course(self, course_id):
        if course_id is None:
            raise ValueError("Course code must not be None")
        self._course_codes.append(course_id)
        return self

    def course_is_set(self):
        return len(self._course_codes) > 0

    def add_prg_language(self, language):
        if language is None:
            raise ValueError("Programming language entry must not be None")
        self._language_tags.append(language)
        return self

    def prg_language_is_set(self):
        return len(self._language_tags) > 0

    def add_concept(self, concept):
        if concept is None:
            raise ValueError("Concept entry must not be None")
        self._concept_tags.append(concept)
        return self

    def concept_is_set(self):
        return len(self._concept_tags) > 0

    def add_framework(self, framework):
        if framework is None:
            raise ValueError("Framework entry must not be None")
        self._concept_tags.append(framework)
        return self

    def framework_is_set(self):
        return len(self._concept_tags) > 0

    def ready_to_build(self):
        return self._course_codes and self._bio

    def build(self):
        if self.ready_to_build():
            new_profile = Profile.objects.get_or_create(student_id=self._student, location=self._location,
                                                        bio=self._bio, pic=self._pic)

            my_courses = Course.objects.filter(course_code_in=self._course_codes)

            all_skills = []
            all_skills.extend(self._language_tags)
            all_skills.extend(self._concept_tags)
            all_skills.extend(self._framework_tags)

            with atomic():
                for course in my_courses:
                    new_profile.courses.add(course)
                for skill in all_skills:
                    new_profile.skills.add(SkillTag.objects.get(tag_text=skill))

            new_profile.save()
            return new_profile
        else:
            missing = []
            if not self._course_codes:
                missing.append("Courses")
            if not self._bio:
                missing.append("Bio")

            if len(missing) > 1:
                missing[-1] = "and " + missing[-1]

            missing_list = ", ".join(missing)
            raise AssertionError("Not ready to build! Missing items: {0}".format(missing_list))
