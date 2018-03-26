from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, permissions
from .permissions import IsOwnerOrReadOnlyIfAuthenticated, IsNotAuthenticated, IsAuthenticatedAndHasProfile
from PairWise_Server.models import LanguageTag, ConceptTag, FrameworkTag, LocationTag,\
                                   Course, User, Notification, Profile, SearchResultsCache, AvailableSearchEntry
from PairWise_Server.serializers import DataTagSerializer, CourseSerializer, NotificationSerializer,\
                                        ResultsCacheSerializer,\
                                        ProfileWriteSerializer, ProfileReadSerializer, SearchEntrySerializer
from .search_form_builder import SearchFormBuilder
from .search_ops import update_cache
from .group_ops import send_invite, add_to_group, remove_from_group
from .fetch import fetch_term_by_time_of_year, fetch_offering_by_term, fetch_course_by_course_code, fetch_search_by_user,\
                   fetch_most_recent_term

from traceback import format_exc


class LanguageList(generics.ListAPIView):
    """
    Retrieval endpoint for all language tags. Returns a list of expanded tag objects, containing tag ID and
    the tag's label (e.g. JavaScript). Used to populate language options in a profile creation page or a
    search form.
    """
    permission_classes = (permissions.AllowAny,)

    queryset = LanguageTag.objects.all()
    serializer_class = DataTagSerializer


class ConceptList(generics.ListAPIView):
    """
    Retrieval endpoint for all concept tags. Returns a list of expanded tag objects, containing tag ID and
    the tag's label (e.g. Machine Learning). Used to populate concept options in a profile creation page or a
    search form.
    """
    permission_classes = (permissions.AllowAny,)

    queryset = ConceptTag.objects.all()
    serializer_class = DataTagSerializer


class FrameworkList(generics.ListAPIView):
    """
    Retrieval endpoint for all framework tags. Returns a list of expanded tag objects, containing tag ID and
    the tag's label (e.g. MongoDB). Used to populate framework options in a profile creation page or a
    search form.
    """
    permission_classes = (permissions.AllowAny,)

    queryset = FrameworkTag.objects.all()
    serializer_class = DataTagSerializer


class LocationList(generics.ListAPIView):
    """
    Retrieval endpoint for all location tags. Returns a list of expanded tag objects, containing tag ID and
    the tag's label (e.g. Downtown). Used to populate location options in a profile creation page.
    """
    permission_classes = (permissions.AllowAny,)

    queryset = LocationTag.objects.all()
    serializer_class = DataTagSerializer


class CourseList(generics.ListAPIView):
    """
    Retrieval endpoint for all courses. Returns a list of expanded course objects, containing ID, course
    code (e.g. CSC309) and course title (e.g. Programming on the Web). Used to populate course options in
    a profile creation page.
    """
    permission_classes = (permissions.AllowAny,)

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def data_tag_root(request, format=None):
    """
    Function-based retrieval endpoint for all kinds of tags. Returns the output from the language tags endpoint,
    within a "languages" key; concepts tag endpoint output within a "concepts" key; framework tags endpoint
    output within a "frameworks" key; and course endpoint output within a "courses" key.

    Can be used while building a search form or profile page to get tags with which to populate all skill type
    options, while only having to send a single request.

    :param request: A parsed HTTP request that arrived at this endpoint
    :type request: rest_framework.request.Request
    :return: A serialized string containing all kinds of data tags, segregated by tag type
    :rtype: rest_framework.response.Response
    """
    return Response({
        'languages': LanguageList.as_view()(request=request._request, format=format).data,
        'concepts': ConceptList.as_view()(request=request._request, format=format).data,
        'frameworks': FrameworkList.as_view()(request=request._request, format=format).data,
        'courses': CourseList.as_view()(request=request._request, format=format).data,
    })


class RegistrationView(APIView):
    """
    API endpoint for creating new accounts in the system. A successful request to this endpoint will
    create a user instance in Django's pre-provided user table in the database, with critical fields
    such as username, password hash, and first and last names. See POST request function for more
    details on required request fields.

    Registration is only allowed to unauthenticated users, so that signed in users cannot create
    additional accounts (that would be silly).
    """
    permission_classes = (IsNotAuthenticated,)

    def post(self, request):
        """
        Create a new account, according to the username and password provided through the request data.
        Repeat: A request to create a profile must be sent with attached data fields, one of which has
        a key "username" and the other of which has a key "password". Passwords can be sent unencrypted.

        Additional fields in the request data include "email", "firstname", and "lastname". These fields
        are mandatory now, but may be changed to be optional in the future.

        :param request: A parsed HTTP request that arrived at this endpoint
        :type request: rest_framework.request.Request
        :return: A HTTP status response reporting on whether the request was successfully carried out
        :rtype: rest_framework.request.Request
        """
        username = request.data['username']
        password = request.data['password']

        if len(username) < 0 or len(password) < 1:
            # Neither username or password should be empty strings
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        elif User.objects.filter(username=username).exists():
            # An account already exists with the same username; require unique usernames.
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            email = request.data['email']

            # Load validated user data into the database. Currently assumes all request
            # data fields are present without checking. Not providing these fields will
            # lead to unsuccessful POST operations.
            new_user = User.objects.create_user(username=username, email=email, password=password)
            new_user.first_name = request.data['firstname']
            new_user.last_name = request.data['lastname']
            new_user.save()

            return Response(status=status.HTTP_201_CREATED)


class CourseListByUser(APIView):
    """
    Returns a list of course objects in which this user has an active search ongoing. Used to populate
    the ongoing searches links at the top of the sidebar.

    Bug note: Currently only returns courses in which a group has not been formed, if the user has not formed
    any groups at all. If a user has formed at least one group, this endpoint will only report the courses
    the user has unfilled groups in.
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        courses = Course.objects.filter(courseoffering__searchentry__members__user=request.user)

        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class GroupListByUser(APIView):
    """
    Returns a list of group data for all groups the request sender has formed. Used to populate a groups page,
    or the group links at the bottom of the sidebar.
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        groups = AvailableSearchEntry.objects.filter(members__user=request.user, size__gte=2)

        serializer = SearchEntrySerializer(groups, many=True)
        return Response(serializer.data)


class NotificationsByUser(APIView):
    """
    Returns a list of notifications received by the user. Currently deprecated as we decide how and whether
    to move into Firebase. May be repurposed for group invites.
    """
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

        send_invite(request.user, invitee, course)
        return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticated,))
def user_categories_root(request):
    """
    Function-based retrieval endpoint for user state information. Returns the output from the user courses
    endpoint, within a "course" key; user groups endpoint output within a "groups" key; and notications
    endpoint output within a "notifications" key.

    Can be used to set up the main landing page, and gather resources to populate the sidebar and
    notifications alerts while only needing to make one request.

    :param request: A parsed HTTP request that arrived at this endpoint
    :type request: rest_framework.request.Request
    :return: A serialized string containing all kinds of data tags, segregated by tag type
    :rtype: rest_framework.response.Response
    """
    return Response({
        'courses': CourseListByUser.as_view()(request=request._request).data,
        'groups': GroupListByUser.as_view()(request=request._request).data,
        'notifications': NotificationsByUser.as_view()(request=request._request).data
    })


class ProfileWriter(generics.CreateAPIView):
    """
    Endpoint for writing new profiles. Nested objects such as the users with which the profiles are associated
    only need to be specified by integer keys, without the need to fill in a whole user object as in the profile
    reading serializer.

    This endpoint does not support other operations, namely GET, and can only allow POST requests to create
    a new profile. For this reason, both the read and write serializers for profiles are used for a full range
    of operations.
    """
    permission_classes = (IsOwnerOrReadOnlyIfAuthenticated,)

    queryset = Profile.objects.all()
    serializer_class = ProfileWriteSerializer


class ProfileReader(generics.RetrieveUpdateAPIView):
    """
    Endpoint for reading and editing existing profiles. Profiles can be read with a GET request by any user,
    but can only be modified through a PUT request by the profile's owner. Nested objects such as the users
    with which the profiles are associated are expanded, and full details are provided such as the user's
    username, email, etc. This allows each user's information to come with the profile in a single request,
    instead of accessing only the user's ID and needing to send another request as in the profile write serializer.

    This endpoint does not support POST requests to create new profiles, because filling in all user fields would
    by complicated or sometimes impossible. For this reason, both the read and write serializers for profiles
    are used for a full range of operations.
    """
    permission_classes = (IsOwnerOrReadOnlyIfAuthenticated,)

    queryset = Profile.objects.all()
    serializer_class = ProfileReadSerializer


class SearchDetails(APIView):
    """
    API endpoint for retrieving or creating search entries. A user must provide a course code in the
    URL they send the request to, which is considered to be the course associated with the search
    entry the user is accessing or posting. The letters in the course code must be capitalized or
    else the course will not be found properly.

    Before creating a search entry, a user must have a profile found in the database. Otherwise, upon
    sending a request to this endpoint they will get a 403 error. This is to ensure that all users
    have profiles that can be accessed when matching them with search results.
    """
    permission_classes = (IsAuthenticatedAndHasProfile,)

    def post(self, request, course_code):
        """
        Launch a new search in the specified course. Requires a number of request data fields, which would
        be pulled from the search form. These fields include:

        "section": Course section the user is registered in, starting with L instead of LEC: e.g. L0101.
        "require_same_section": True if the user is only looking for partners in their section of the
                                course, such as when the course requires partners to be in the same section.
        "desired_skills": A list of skill tags corresponding to the capabilties the user wants in a partner.
        "location": The location where the user would prefer to work on this project. May be removed in favor
                    of the home location stored in the profile.
        "group_capacity": The number of people the user wants in their group.
        "title": An optional description of what the group will be making, e.g. CSC369 Assignment 4
        "description": An optional text field in which the user can specify additional information about their
                       search, such as desired meeting times and their goals in the assignment, etc.
        "quality_cutoff": A numeric value that marks the minimum matching coefficient for another user to
                          show up as a result for the course. For example, if quality_cutoff is set to 100,
                          then only results that completely match the user's criteria will be shown in search
                          results.

        :param request: A parsed HTTP request that arrived at this endpoint
        :type request: rest_framework.request.Request
        :return: A HTTP response indicating the success or failre of the operation
        :rtype: rest_framework.response.Response
        """
        request.user.id = request.user.id
        course = _get_course(course_code)

        section = request.data['section']
        samesection = request.data['require_same_section']
        print(samesection)
        skills = request.data['desired_skills']
        location = request.data['location']
        cap = request.data['group_capacity']
        title = request.data['title']
        desc = request.data['description']
        cutoff = request.data['quality_cutoff']

        # Try to create a builder, which checks if the user and course are valid.
        try:
            builder = SearchFormBuilder(request.user, course)
        except ValueError:
            return Response({'error': format_exc()}, status=status.HTTP_409_CONFLICT)

        # Load and validate the other fields through the builder.
        try:
            builder = builder.set_course_section(section)\
                             .add_location(location)\
                             .set_capacity(cap)\
                             .set_title(title)\
                             .set_description(desc)\
                             .set_quality_cutoff(cutoff)

            #  Load and validate required section field, if required.
            if samesection:
                builder = builder.require_same_section()

            # Load and validate each of multiple skill tags.
            for skill in skills:
                builder = builder.add_skill(skill)
        except ValueError:
            return Response({'error': format_exc()}, status=status.HTTP_206_PARTIAL_CONTENT)

        # Attempt to create the search entry with the informatio provided.
        new_search_entry = builder.build()
        if new_search_entry is None:
            # Builder has not received all of its required fields.
            return Response(status=status.HTTP_206_PARTIAL_CONTENT)
        else:
            # Search entry was successfully created. It is matched beforehand, and the results are cached
            # to be used when the user next accesses their search results.
            update_cache(new_search_entry)
            return Response(status=status.HTTP_201_CREATED)

    def get(self, request, course_code):
        """
        Retrieve some information about the status of an ongoing search in the provided course, which
        may either have formed a group or not. Group searches report information about all members.

        :param request: A parsed HTTP request that arrived at this endpoint
        :type request: rest_framework.request.Request
        :return: A serialized string containing data about the user's search in the specified course
        :rtype: rest_framework.response.Response
        """
        course = _get_course(course_code)
        my_search = fetch_search_by_user(request.user, course)

        if my_search is None:
            return Response({})
        else:
            search_entry = fetch_search_by_user(request.user, course)
            serializer = SearchEntrySerializer(search_entry, allow_null=True)
            return Response(serializer.data)


class SearchList(APIView):
    """
    API endpoint for mass operations on search results. Namely, the endpoint through which to request
    a user's search results in a specified course. A user must provide a course code in the
    URL they send the request to, which is considered to be the course associated with the search
    entry the user is getting results from. The letters in the course code must be capitalized or
    else the course will not be found properly.

    Before creating a search entry, a user must have a profile found in the database. Otherwise, upon
    sending a request to this endpoint they will get a 403 error. This is to ensure that all users
    have profiles that can be accessed when matching them with search results. Similarly, getting
    results from a search can only be done if the user has a profile registered in the database.
    """
    permission_classes = (IsAuthenticatedAndHasProfile,)

    def get(self, request, course_code):
        """
        Retrieve a user's search results in this course with a GET request to the endpoint, returning
        a serialized list of other users and groups that were found to be good matches. The list of
        results is ordered according to the quality of the match, which is itself provided in the
        match_coefficient field of the result.

        :param request: A parsed HTTP request that arrived at this endpoint
        :type request: rest_framework.request.Request
        :param course_code: The course string (e.g. CSC301) that identifies which course the user
                            wants results from
        :type course_code: str
        :return: A serialized string of search results, containing information about the users that
                 were found to be adequate matches
        :rtype: rest_framework.response.Response
        """
        course = _get_course(course_code)

        search_entry = fetch_search_by_user(request.user, course)
        if search_entry is None:
            return Response({})

        # Results are taken from the cache without triggering any further matching algorithm calls
        results = SearchResultsCache.objects.filter(searcher=search_entry)

        serializer = ResultsCacheSerializer(results, many=True)
        return Response(serializer.data)


class GroupForm(APIView):
    """
    API endpoint for group operations. This includes creating a group, leaving a group, and getting
    group details for use in the messages page. Leaving a group is currently not implemented. To
    access group information, a user must report which course the group is in, using a course code
    in the URL they send the request to. The letters in the course code must be capitalized or
    else the course will not be found properly.

    A user can only request group information if they have a profile registered in the database.
    The scenario in which a user is denied from accessing group information based on not having a
    profile should never come up, since the group formation also requires a profile. However,
    it seems sensible to restrict access to this endpoint to those whom it can properly serve.
    """
    permission_classes = (IsAuthenticatedAndHasProfile,)

    def get(self, request, course_code):
        """
        Retrieve group data by sending a GET request to this endpoint.

        :param request: A parsed HTTP request that arrived at this endpoint
        :type request: rest_framework.request.Request
        :param course_code: The course string (e.g. CSC301) that identifies which course the user
                            wants results from
        :type course_code: str
        :return: A serialized string of data about the group, including state information as well
                 as data about all members of the group
        :rtype: rest_framework.response.Response
        """
        course = _get_course(course_code)

        group = fetch_search_by_user(request.user, course)
        if group is None or group.size < 2:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = SearchEntrySerializer(group)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, course_code):
        """
        Join a group by sending a POST request to this endpoint. The request must include a field
        in the request data, with the key "inviter": this is the user ID of the person who sent
        the group invite. The user who sends the request to this endpoint is the newcomer to the
        group, should it already exist.

        The newcomer always abandons their old search, and joins the existing search without
        modifying its parameters extensively. The search retains the same title, description,
        capacity, and some other fields. However, the new user's preferences (desired skills,
        location, section) will be taken into account when the group is matched again.

        :param request: A parsed HTTP request that arrived at this endpoint
        :type request: rest_framework.request.Request
        :param course_code: The course string (e.g. CSC301) that identifies which course the user
                            wants results from
        :type course_code: str
        :return: A HTTP response indicating the success or failre of the operation
        :rtype: rest_framework.response.Response
        """
        inviter = User.objects.get(id=request.data['inviter'])
        course = _get_course(course_code)

        # The newcomer joins the inviter's group should it exist. If the inviter is not in a
        # group, then a new group is formed which inherits the inviter's search information
        # such as title and capacity.
        add_to_group(newcomer=request.user, inviter=inviter, offering=course)
        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request, course_code):
        """
        Drop a user out of a group, dividing the one search into two. The leaving user gets back
        the search details they lost when they joined the group; that is, the options they selected
        when filling out the search form are recovered, and the user continues that search again.
        The group's parameters (except for size) are unchanged.

        A user can also send a DELETE request to this endpoint if they have not formed a group,
        in which case their search will be cancelled and destroyed irrecoverably.

        :param request: A parsed HTTP request that arrived at this endpoint
        :type request: rest_framework.request.Request
        :param course_code: The course string (e.g. CSC301) that identifies which course the user
                            wants results from
        :type course_code: str
        :return: A HTTP response indicating the success or failre of the operation
        :rtype: rest_framework.response.Response
        """
        course = _get_course(course_code)

        # The newcomer joins the inviter's group should it exist. If the inviter is not in a
        # group, then a new group is formed which inherits the inviter's search information
        # such as title and capacity.
        remove_from_group(request.user, course)
        return Response(status=status.HTTP_202_ACCEPTED)


def _get_course(course_code):
    """
    Utility function used in many view classes that require course codes. Converts the course code
    into the corresponding course offering object from the most recent term. It is a reasonable
    assumption that anyone launching a search will be doing so in the most recent term (i.e. no-one
    would want to form groups for course projects after the course ends).

    :param course_code: The course code send through a request
    :type course_code: str
    :return: The course offering associated with the given course code
    :rtype: PairWise_Server.models.course.CourseOffering
    """
    course = fetch_course_by_course_code(course_code)
    current_term = fetch_most_recent_term()

    course_offr = fetch_offering_by_term(course, current_term)

    return course_offr
