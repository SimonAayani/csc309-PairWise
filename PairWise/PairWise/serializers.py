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
