from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, permissions
from .permissions import IsOwnerOrReadOnlyIfAuthenticated, IsNotAuthenticated, IsAuthenticatedAndHasProfile
from PairWise_Server.models import LanguageTag, ConceptTag, FrameworkTag, LocationTag, GroupSearchEntry,\
                                   Course, User, Notification, NewNotification, Profile, NewNotification,\
                                   SearchResultsCache, UserSearchEntry, SearchEntry
from PairWise_Server.serializers import DataTagSerializer, CourseSerializer, UserSerializer, NotificationSerializer,\
                                        UserSearchSerializer, GroupSearchSerializer, ResultsCacheSerializer,\
                                        ProfileWriteSerializer, ProfileReadSerializer, GenericSearchSerializer
from .search_form_builder import SearchFormBuilder
from .search_ops import cancel_search, measure_matches_user_to_user
from .group_ops import send_invite, add_to_group
from .fetch import fetch_term_by_time_of_year, fetch_offering_by_term, fetch_course_by_course_code, fetch_search_by_user,\
                   fetch_profile_by_user, fetch_user_by_username, fetch_most_recent_term, fetch_group_by_member

from traceback import format_exc


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
        courses = Course.objects.filter(courseoffering__searchentry__groupsearchentry__members__user=request.user)

        if not courses.exists():
            courses = Course.objects.filter(courseoffering__searchentry__usersearchentry__host__user=request.user)

        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class GroupListByUser(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        groups = GroupSearchEntry.objects.filter(members__user=request.user)

        serializer = GroupSearchSerializer(groups, many=True)
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
    permission_classes = (IsAuthenticatedAndHasProfile,)

    def _get_course(self, course_code):
        course = fetch_course_by_course_code(course_code)
        current_term = fetch_term_by_time_of_year(2018, 'S')

        course_offr = fetch_offering_by_term(course, current_term)

        return course_offr

    def get(self, request, course_code):
        course = self._get_course(course_code)

        group = fetch_group_by_member(request.user, course)
        if group is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = GroupSearchSerializer(group)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, course_code):
        inviter = User.objects.get(id=request.data['inviter'])
        course = self._get_course(course_code)

        add_to_group(newcomer=request.user, inviter=inviter, offering=course)
        return Response(status=status.HTTP_201_CREATED)


# {
#     "section": "L0101",
#     "require_same_section": "False",
#     "desired_skills": [52, 48, 41, 38, 37, 32, 9, 7],
#     "location": 54,
#     "group_capacity": 7,
#     "title": "PairWise",
#     "description": "I need six frontend developers to assist me in making a product for student group matching. I can handle database and backend servers. Require high commitment levels to make a good-looking interface",
#     "quality_cutoff": 30
# }


# {
#     "section": "L5101",
#     "require_same_section": "False",
#     "desired_skills": [8, 38],
#     "location": 56,
#     "group_capacity": 2,
#     "title": "YB Mugs Reader",
#     "description": "Require a moderately experienced Java developer to create a program to assist yearbook development. Help smooth out our mugs page process by automatically spellchecking names from a page against an index file.",
#     "quality_cutoff": 20
# }


class SearchDetails(APIView):
    permission_classes = (IsAuthenticatedAndHasProfile,)

    def _get_course(self, course_code):
        course = fetch_course_by_course_code(course_code)
        current_term = fetch_most_recent_term()

        course_offr = fetch_offering_by_term(course, current_term)

        return course_offr

    def post(self, request, course_code):
        request.user.id = request.user.id
        course = self._get_course(course_code)

        section = request.data['section']
        samesection = request.data['require_same_section']
        skills = request.data['desired_skills']
        location = request.data['location']
        cap = request.data['group_capacity']
        title = request.data['title']
        desc = request.data['description']
        cutoff = request.data['quality_cutoff']

        try:
            builder = SearchFormBuilder(request.user, course)
        except ValueError:
            return Response({'error': format_exc()}, status=status.HTTP_409_CONFLICT)

        try:
            builder = builder.set_course_section(section).add_location(location)\
                             .set_capacity(cap).set_title(title).set_description(desc).set_quality_cutoff(cutoff)

            if samesection:
                builder = builder.require_same_section()

            for skill in skills:
                builder = builder.add_skill(skill)

        except ValueError:
            return Response({'error': format_exc()}, status=status.HTTP_206_PARTIAL_CONTENT)

        new_search_entry = builder.build()
        if new_search_entry is None:
            return Response(status=status.HTTP_206_PARTIAL_CONTENT)
        else:
            measure_matches_user_to_user(new_search_entry, cutoff=cutoff)
            return Response(status=status.HTTP_201_CREATED)

    def get(self, request, course_code):
        course = self._get_course(course_code)
        my_search = fetch_search_by_user(request.user, course)

        if my_search is None:
            return Response({})
        else:
            serializer = UserSearchSerializer(fetch_search_by_user(request.user, course))
            return Response(serializer.data)


class SearchEntryFieldsMixin(object):
    def get_queryset(self):
        return SearchEntry.objects.select_subclasses()


class SearchList(SearchEntryFieldsMixin, APIView):
    permission_classes = (IsAuthenticatedAndHasProfile,)

    def _get_course(self, course_code):
        course = fetch_course_by_course_code(course_code)
        current_term = fetch_term_by_time_of_year(2018, 'S')

        course_offr = fetch_offering_by_term(course, current_term)

        return course_offr

    def get(self, request, course_code):
        course = self._get_course(course_code)
        if UserSearchEntry.objects.filter(host__user=request.user, category=course).exists():
            search_entry = UserSearchEntry.objects.get(host__user=request.user, category=course)
        elif GroupSearchEntry.objects.filter(members__user=request.user, category=course).exists():
            search_entry = GroupSearchEntry.objects.get(members__user=request.user, category=course)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

        results = SearchResultsCache.objects.filter(searcher=search_entry)

        serializer = ResultsCacheSerializer(results, many=True)
        return Response(serializer.data)


class RegistrationView(APIView):
    permission_classes = (IsNotAuthenticated,)

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
