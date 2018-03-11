from rest_framework import serializers
from .models import DataTag, Course, Profile, User, Group, Notification, UserSearchEntry, GroupSearchEntry
from .profile_builder import ProfileBuilder


class DataTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataTag
        fields = ('id', 'tag_text')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('course_id', 'course_code', 'name')


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
# class ProfileWriteSerializer(serializers.Serializer):
#     student = serializers.IntegerField()
    # courses = serializers.ListField(child=serializers.CharField(max_length=10), min_length=1)
    # location = serializers.CharField(max_length=30)
    # languages = serializers.ListField(child=serializers.CharField(max_length=50))
    # concepts = serializers.ListField(child=serializers.CharField(max_length=50))
    # frameworks = serializers.ListField(child=serializers.CharField(max_length=50))
    # # skills = serializers.ListField(child=serializers.CharField(max_length=50))
    # bio = serializers.CharField(max_length=5000)
    # pic = serializers.ImageField(max_length=100, allow_null=True)

    # class Meta:
    #     model = Profile
    #     fields = ('student', 'courses', 'location', 'skills', 'bio', 'pic')
        # student = serializers.Field(source='student')

    # def create(self, validated_data):
    #     # user =
    #     builder = ProfileBuilder(validated_data['student']).set_bio(validated_data['bio'])
    #     if 'location' in validated_data:
    #         builder = builder.set_location(validated_data['location'])
    #
    #     if 'courses' in validated_data:
    #         for course in validated_data['courses']:
    #             builder = builder.add_course(course)
    #         validated_data.pop('courses')
    #
    #     if 'languages' in validated_data:
    #         for language in validated_data['languages']:
    #             builder = builder.add_prg_language(language)
    #         validated_data.pop('languages')
    #
    #     if 'concepts' in validated_data:
    #         for concept in validated_data['concepts']:
    #             builder = builder.add_prg_language(concept)
    #         validated_data.pop('concepts')
    #
    #     if 'frameworks' in validated_data:
    #         for framework in validated_data['frameworks']:
    #             builder = builder.add_prg_language(framework)
    #         validated_data.pop('frameworks')
    #
    #     return builder.build()
    #     # super(ProfileSerializer, self).create(validated_data)
    # #
    # def update(self, instance, validated_data):
    #     pass
        # if validated_data['location'] is not None:
        #     builder = validated_data['location'])
        #
        # for course in validated_data['courses']:
        #     builder = builder.add_course(course)
        #
        # for language in validated_data['languages']:
        #     builder = builder.add_prg_language(language)
        #
        # for concept in validated_data['concepts']:
        #     builder = builder.add_prg_language(concept)
        #
        # for framework in validated_data['framework']:
        #     builder = builder.add_prg_language(framework)

    # class Meta:
    #     model = Profile
    #     fields = ('student', 'courses', 'location', 'skills', 'bio')


# class ProfileReadSerializer(serializers.ModelSerializer):
#     student = UserSerializer(read_only=True)
#     courses = CourseSerializer(many=True, read_only=True)
#     location = DataTagSerializer(read_only=True)
#     languages = DataTagSerializer(many=True, read_only=True)
#     concepts = DataTagSerializer(many=True, read_only=True)
#     frameworks = DataTagSerializer(many=True, read_only=True)
#     pic = serializers.ImageField(max_length=100, allow_null=True)
#
#     class Meta:
#         model = Profile
#         fields = ('student', 'courses', 'location', 'languages', 'concepts', 'frameworks', 'bio', 'pic')


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileReadSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'profile', 'is_active', 'date_joined')


class GroupSerializer(serializers.ModelSerializer):
    offering__course = CourseSerializer(read_only=True)
    members = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Group
        fields = ('group_id', 'offering__course', 'members', 'capacity', 'size')


class NotificationSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    receiver = UserSerializer(read_only=True)
    category__course = CourseSerializer(read_only=True)

    class Meta:
        model = Notification
        fields = ('id', 'sender', 'receiver', 'category__course', 'text', 'is_invite')


class UserSearchSerializer(serializers.ModelSerializer):
    host = UserSerializer(read_only=True)
    category__course = CourseSerializer(read_only=True)
    desired_fields = DataTagSerializer(many=True, read_only=True)

    class Meta:
        model = UserSearchEntry
        fields = ('id', 'host', 'category__course', 'description', 'subhead', 'desired_fields', 'active_search')


class GroupSearchSerializer(serializers.ModelSerializer):
    host = GroupSerializer(many=True, read_only=True)
    desired_fields = DataTagSerializer(read_only=True)

    class Meta:
        model = GroupSearchEntry
        fields = ('id', 'host', 'description', 'subhead', 'desired_fields', 'active_search')
