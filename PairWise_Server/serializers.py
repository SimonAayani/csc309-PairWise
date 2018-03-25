from rest_framework import serializers
from PairWise_Server.models import DataTag, Course, Profile, User, Notification,\
                                   UserSearchEntry, GroupSearchEntry, UserSearchData, CourseSection, SearchEntry, SearchResultsCache


class DataTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataTag
        fields = ('id', 'tag_text')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('course_id', 'course_code', 'name')


class CourseSectionSerializer(serializers.ModelSerializer):
    offering__course = CourseSerializer(read_only=True)

    class Meta:
        model = CourseSection
        fields = ('section_id', 'section_name', 'offering__course')


class ProfileReadSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    location = DataTagSerializer(read_only=True)
    skills = DataTagSerializer(many=True, read_only=True)
    pic = serializers.ImageField(max_length=100, read_only=True)

    class Meta:
        model = Profile
        fields = ('courses', 'location', 'skills', 'bio', 'pic')


class ProfileWriteSerializer(serializers.ModelSerializer):
    pic = serializers.ImageField(max_length=100, allow_null=True)

    class Meta:
        model = Profile
        fields = ('student', 'courses', 'location', 'skills', 'bio', 'pic')


class UserSerializer(serializers.ModelSerializer):
    profile__pic = serializers.ImageField(max_length=100, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'profile__pic', 'last_login', 'date_joined')


class NotificationSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    receiver = UserSerializer(read_only=True)
    category__course = CourseSerializer(read_only=True)

    class Meta:
        model = Notification
        fields = ('id', 'sender', 'receiver', 'category__course', 'text', 'is_invite')


class UserSearchDataSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    course_section = CourseSectionSerializer(read_only=True)
    location = DataTagSerializer(read_only=True)
    desired_skills = DataTagSerializer(many=True, read_only=True)

    class Meta:
        model = UserSearchData
        fields = ('id', 'user', 'course_section', 'location', 'desired_skills')


class UserSearchSerializer(serializers.ModelSerializer):
    host = UserSearchDataSerializer(read_only=True)
    category__course = CourseSerializer(read_only=True)
    required_section = CourseSectionSerializer(read_only=True)

    class Meta:
        model = UserSearchEntry
        fields = ('id', 'host', 'category__course', 'title', 'description', 'capacity', 'required_section')


class GroupSearchSerializer(serializers.ModelSerializer):
    members = UserSearchDataSerializer(many=True, read_only=True)
    category__course = CourseSerializer(read_only=True)
    required_section = CourseSectionSerializer(read_only=True)

    class Meta:
        model = GroupSearchEntry
        fields = ('id', 'members', 'category__course', 'title', 'description', 'capacity', 'size', 'required_section')


class GenericSearchSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        if GroupSearchEntry.objects.filter(id=instance.id).exists():
            return GroupSearchSerializer(instance=instance.groupsearchentry).data
        elif UserSearchEntry.objects.filter(id=instance.id).exists():
            return UserSearchDataSerializer(instance=instance.usersearchentry.host).data

        else:
            return {}

    class Meta:
        model = SearchEntry
        fields = '__all__'


class ResultsCacheSerializer(serializers.ModelSerializer):
    result = GenericSearchSerializer(read_only=True)

    class Meta:
        model = SearchResultsCache
        fields = ('result', 'match_coefficient')
