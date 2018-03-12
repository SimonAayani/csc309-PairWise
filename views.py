from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from PairWise.models import LanguageTag, ConceptTag, FrameworkTag, LocationTag,\
                            Course, User, Group, Notification, NewNotification, Profile, NewNotification
from PairWise.serializers import DataTagSerializer, CourseSerializer, UserSerializer, GroupSerializer,\
                                 NotificationSerializer, UserSearchSerializer, GroupSearchSerializer,\
                                 ProfileWriteSerializer, ProfileReadSerializer
from .search_ops import enter_search, cancel_search, measure_matches
from .group_ops import send_invite, add_to_group
from .fetch import fetch_term_by_time_of_year, fetch_offering_by_term, fetch_course_by_course_code, fetch_search_by_user,\
                   fetch_profile_by_user


class LanguageList(generics.ListAPIView):
    queryset = LanguageTag.objects.all()
    serializer_class = DataTagSerializer


class ConceptList(generics.ListAPIView):
    queryset = ConceptTag.objects.all()
    serializer_class = DataTagSerializer


class FrameworkList(generics.ListAPIView):
    queryset = FrameworkTag.objects.all()
    serializer_class = DataTagSerializer


class LocationList(generics.ListAPIView):
    queryset = LocationTag.objects.all()
    serializer_class = DataTagSerializer


class CourseList(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


@api_view(['GET'])
def data_tag_root(request, format=None):
    return Response({
        'languages': LanguageList.as_view()(request=request._request, format=format).data,
        'concepts': ConceptList.as_view()(request=request._request, format=format).data,
        'frameworks': FrameworkList.as_view()(request=request._request, format=format).data,
        'courses': CourseList.as_view()(request=request._request, format=format).data,
    })


class CourseListByUser(APIView):
    def get(self, request, user):
        courses = Course.objects.filter(courseoffering__group__members__id=user)

        if not courses.exists():
            courses = Course.objects.filter(courseoffering__usersearchentry__host__id=user)

        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class GroupListByUser(APIView):
    def get(self, request, user):
        groups = Group.objects.filter(members__id=user)
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)


class NotificationsByUser(APIView):
    def get(self, request, user):
        new = NewNotification.objects.filter(receiver__id=user).select_related('notification_ptr')
        old = Notification.objects.filter(newnotification__isnull=True)

        new_serializer = NotificationSerializer(new, many=True)
        old_serializer = NotificationSerializer(old, many=True)

        return Response({
            'new': new_serializer.data,
            'old': old_serializer.data
        })

    def _get_course(self, course_code):
        course = fetch_course_by_course_code(course_code)
        current_term = fetch_term_by_time_of_year(2018, 'S')

        course_offr = fetch_offering_by_term(course, current_term)

        return course_offr

    def post(self, request, user):
        me = User.objects.get(id=user)
        invitee = User.objects.get(id=request.data['invitee'])
        course = self._get_course(request.data['course'])

        if 'text' in request.data:
            message = request.data['text']
        else:
            message = None

        send_invite(me, invitee, course, message)
        return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
def user_categories_root(request, user):
    return Response({
        'courses': CourseListByUser.as_view()(request=request._request, user=user).data,
        'groups': GroupListByUser.as_view()(request=request._request, user=user).data,
        'notifications': NotificationsByUser.as_view()(request=request._request, user=user).data
    })


class ProfileWriter(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileWriteSerializer


class ProfileReader(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileReadSerializer


class GroupForm(APIView):
    def _get_course(self, course_code):
        course = fetch_course_by_course_code(course_code)
        current_term = fetch_term_by_time_of_year(2018, 'S')

        course_offr = fetch_offering_by_term(course, current_term)

        return course_offr

    def get(self, request, user, course_code):
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

    def post(self, request, user, course_code):
        me = User.objects.get(id=user)
        invitee = request.data['invitee']
        course = self._get_course(course_code)

        add_to_group(newcomer=invitee, inviter=me, offering=course)
        return Response(status=status.HTTP_201_CREATED)


class SearchDetails(APIView):
    def _get_course(self, course_code):
        course = fetch_course_by_course_code(course_code)
        current_term = fetch_term_by_time_of_year(2018, 'S')

        course_offr = fetch_offering_by_term(course, current_term)

        return course_offr

    def post(self, request, user, course_code):
        me = User.objects.get(id=user)
        course = self._get_course(course_code)

        sub = request.data['subhead']
        desc = request.data['description']

        enter_search(me, course)
        return Response(status=status.HTTP_201_CREATED)

    def get(self, request, user, course_code):
        me = User.objects.get(id=user)
        course = self._get_course(course_code)
        my_search = fetch_search_by_user(me, course)

        if my_search is None:
            return Response({})
        else:
            serializer = UserSearchSerializer(fetch_search_by_user(me, course))
            return Response(serializer.data)


class SearchList(APIView):
    def _get_course(self, course_code):
        course = fetch_course_by_course_code(course_code)
        current_term = fetch_term_by_time_of_year(2018, 'S')

        course_offr = fetch_offering_by_term(course, current_term)

        return course_offr

    def get(self, request, user, course_code):
        me = User.objects.get(id=user)
        course = self._get_course(course_code)
        results = measure_matches(me, course, 30)

        serializer = UserSerializer(results, many=True)
        return Response(serializer.data)
