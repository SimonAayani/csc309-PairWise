from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, permissions
from .permissions import IsOwnerOrReadOnlyIfAuthenticated
from PairWise_Server.models import LanguageTag, ConceptTag, FrameworkTag, LocationTag,\
                                   Course, User, Group, Notification, NewNotification, Profile, NewNotification
from PairWise_Server.serializers import DataTagSerializer, CourseSerializer, UserSerializer, GroupSerializer,\
                                        NotificationSerializer, UserSearchSerializer, GroupSearchSerializer,\
                                        ProfileWriteSerializer, ProfileReadSerializer
from .search_ops import enter_search, cancel_search, measure_matches
from .group_ops import send_invite, add_to_group
from .fetch import fetch_term_by_time_of_year, fetch_offering_by_term, fetch_course_by_course_code, fetch_search_by_user,\
                   fetch_profile_by_user, fetch_user_by_username


class LanguageList(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = LanguageTag.objects.all()
    serializer_class = DataTagSerializer


class ConceptList(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = ConceptTag.objects.all()
    serializer_class = DataTagSerializer


class FrameworkList(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = FrameworkTag.objects.all()
    serializer_class = DataTagSerializer


class LocationList(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = LocationTag.objects.all()
    serializer_class = DataTagSerializer


class CourseList(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


@api_view(['GET'])
def data_tag_root(request, format=None):
    permission_classes = (permissions.AllowAny,)

    return Response({
        'languages': LanguageList.as_view()(request=request._request, format=format).data,
        'concepts': ConceptList.as_view()(request=request._request, format=format).data,
        'frameworks': FrameworkList.as_view()(request=request._request, format=format).data,
        'courses': CourseList.as_view()(request=request._request, format=format).data,
    })


class CourseListByUser(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        courses = Course.objects.filter(courseoffering__group__members=request.user)

        if not courses.exists():
            courses = Course.objects.filter(courseoffering__usersearchentry__host=request.user)

        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class GroupListByUser(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        groups = Group.objects.filter(members=request.user)

        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)


class NotificationsByUser(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        new = Notification.objects.filter(receiver__id=request.user.id, newnotification__isnull=False)
        old = Notification.objects.filter(receiver__id=request.user.id, newnotification__isnull=True)

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

    def post(self, request):
        invitee = User.objects.get(id=request.data['invitee'])
        course = self._get_course(request.data['course'])

        if 'text' in request.data:
            message = request.data['text']
        else:
            message = None

        send_invite(request.user, invitee, course, message)
        return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
def user_categories_root(request):
    permission_classes = (permissions.IsAuthenticated,)

    return Response({
        'courses': CourseListByUser.as_view()(request=request._request).data,
        'groups': GroupListByUser.as_view()(request=request._request).data,
        'notifications': NotificationsByUser.as_view()(request=request._request).data
    })


class ProfileWriter(generics.CreateAPIView):
    permission_classes = (IsOwnerOrReadOnlyIfAuthenticated,)

    queryset = Profile.objects.all()
    serializer_class = ProfileWriteSerializer


class ProfileReader(generics.RetrieveUpdateAPIView):
    permission_classes = (IsOwnerOrReadOnlyIfAuthenticated,)

    queryset = Profile.objects.all()
    serializer_class = ProfileReadSerializer


class GroupForm(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def _get_course(self, course_code):
        course = fetch_course_by_course_code(course_code)
        current_term = fetch_term_by_time_of_year(2018, 'S')

        course_offr = fetch_offering_by_term(course, current_term)

        return course_offr

    def get(self, request, course_code):
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

    def post(self, request, course_code):
        invitee = request.data['invitee']
        course = self._get_course(course_code)

        add_to_group(newcomer=invitee, inviter=request.user, offering=course)
        return Response(status=status.HTTP_201_CREATED)


class SearchDetails(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def _get_course(self, course_code):
        course = fetch_course_by_course_code(course_code)
        current_term = fetch_term_by_time_of_year(2018, 'S')

        course_offr = fetch_offering_by_term(course, current_term)

        return course_offr

    def post(self, request, course_code):
        course = self._get_course(course_code)

        sub = request.data['subhead']
        desc = request.data['description']

        enter_search(request.user, course, headline=sub, descr=desc)
        return Response(status=status.HTTP_201_CREATED)

    def get(self, request, course_code):
        course = self._get_course(course_code)
        my_search = fetch_search_by_user(request.user, course)

        if my_search is None:
            return Response({})
        else:
            serializer = UserSearchSerializer(fetch_search_by_user(request.user, course))
            return Response(serializer.data)


class SearchList(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def _get_course(self, course_code):
        course = fetch_course_by_course_code(course_code)
        current_term = fetch_term_by_time_of_year(2018, 'S')

        course_offr = fetch_offering_by_term(course, current_term)

        return course_offr

    def get(self, request, course_code):
        course = self._get_course(course_code)
        results = measure_matches(request.user, course, 30)

        serializer = UserSerializer(results, many=True)
        return Response(serializer.data)


class RegistrationView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        if User.objects.filter(username=username).exists():
            return Response(status=status.HTTP_403_FORBIDDEN)
        elif (len(password) < 1):
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            email = request.data['email']

            newUser = User.objects.create_user(username=username, email=email, password=password)
            newUser.first_name = request.data['firstname']
            newUser.last_name = request.data['lastname']
            newUser.save()

            return Response(status=status.HTTP_201_CREATED)
