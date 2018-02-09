# PairWise

#### Q1: What are you planning to build?

> We plan to build a webapp named **PairWise** that helps Computer Science students at the University of Toronto find compatible partners for course projects. Currently, students struggle to find partners that complement their abilities and work strategies, and have to rely mainly on guesswork to find an appropriate group. Many partners end up being incompatible for a variety of reasons, from preferring to work in different languages to being unable to work around each other's schedules, leading to inefficient teamwork. PairWise will allow students to construct a profile describing themselves, their schedule, and their technical skill set. A user can search for a partner based on the criteria like time commitment, availability, and meeting location. Upon searching, the profiles of students meeting the search criteria will be displayed to the user. The searcher can look at these profiles for more information, send a group invite, or contact their potential partner. When a user receives an invite, they can choose to accept it or reject it. When a user accepts an invitation, a group is formed. A group can then continue to look for more members if required. With our PairWise, students will find teammates that a share their interests, schedules, and goals, leading to smoother collaboration and a better experience for all those involved.

#### Q2: Who are your target users?

> Our target users are students taking Computer Science courses at the University of Toronto’s St. George Campus. Specifically, our users are students who need to form groups for coursework, but do not personally know any potential partners in their courses. They have concrete ideas about the grades they wish to receive and the time they’re willing to invest, and they want to find collaborators with similar goals and schedules. We developed some personas to describe the types of users we hope to reach with PairWise.
>
> Take, for example, **High-achiever Harry**, who puts a lot of effort into his courses and school in general. He wants to maintain his 4.0 GPA in his a Computer Science Specialist degree and is also involved in many clubs and events around campus. Due to his busy schedule, the times he is available to do group work is limited, but he still strives to obtain high grades for all of his projects. Harry wants to find a partner or group that meets his work expectations while being able to accommodate his time restraints.
>
> On the other hand, there are students like **Lazy Lisa**, who merely wants a respectable mark in her courses, ideally with minimal effort. She lives far away from campus and her commute takes 1.5 hours, so she would also prefer to group up with people closer to her area for easier meetups, or who prefer meeting online.
>
> **Backend Benny** is a third type of user, who is looking for a specific skillset in his project partners. Benny has not been exposed very much to front-end development, but has a wealth of experience in back-end. With this in mind, he wants a group that will balance out his skillset with front-end focused teammates for a project in web development. He would like to find partners who would be willing to teach him the basics of front-end, as well.

#### Q3: Why would your users choose your product? What are they using today to solve their problem/need?

> Students at UofT, especially those in computer science, currently use Piazza’s teammate search function or Blackboard’s discussion board to find partners for their assignments and projects. Our web application will improve on the poor communication media used in those two group-forming services. Whereas on Piazza one would have to make a post in the group finder and wait for an email response, our application will implement a chat interface that allows potential partners to create a smoother communication flow to see if they are compatible.
>
> Users would also get a better partner match in our app than in alternatives, as it will actively search and sort results based on the partner criteria provided by the user, whereas group forming on Piazza is pure guesswork as users get little or no information on the person they are contacting. Students cannot easily access information about prospective partners, and would prefer to know more about the partner before they form the group. Many students randomly form groups with strangers through Piazza, in classes, or in tutorials. As a result, students may experience unpleasant work atmosphere due to incompatible matchups. The product will provide information for users to find suitable partners, through search criteria as well as the profiles of prospective group members. Users can find information about each other and match skill sets, work habits, and schedules.

----

### Highlights

#### The Project Idea
> The group finder product was one of the last ideas formed amongst another 8-10 ideas. The other main idea was a scheduling app that would compare the schedules of a list of people and suggest meeting times at which the most people have no conflicts. Many scheduling apps exist for various problems, but very few properly address the need for all members of a group to actively contribute in deciding a time. This schedule-comparing app would also be useful for checking available times for doctor’s appointments. The team decided on the group finder idea because finding a group tends to be more of a struggle than finding time to work. Additionally, the group finder could be better adapted to serve a small area, namely the University of Toronto, and would thus be more suited to MVP deployment.

#### Website vs. Mobile App
> The group decided to create a website instead of a mobile app mainly because more of the team has experience in web design than Android or iOS or other mobile services. Additionally, users of the product would likely be looking for partners while looking at an assignment handout or syllabus on their laptop, making it appropriate to have the group finder nearby in their browser.

#### Communication and Meetings
> The team decided to use Slack for communication due to its integration with GitHub and its flexible communication options. It would serve as a good base for organization as well as online group meetings. We decided to have such meetings twice a week as analogues of scrum standups, to keep track of the progress and needs of every team member while not requiring in-person meetings every day. One of these meetings is online to prevent it from being interfered with by other courses. The other meeting is in person, and allows for greater efficiency of communication. The combination strikes a medium between avoiding time conflicts with other courses and allowing the team to stay up-to-date on the progress of its members.

#### Limited Project Domain
> The team decided not to restrict the functionality of PairWise to group
> formation, and not include features to manage group workflow such as
> project management. We believe other services such Slack and GitHub are
> widely used by our target users and handle these aspects of collaboration
> well. Restricting the product to group formation greatly reduces the number of
> features we need to implement for our MVP, and saves us from competing with
> popular and well-designed services.
>
> The team also decided that the implementation of certain features, such as
> real-time chat, partner rating, and notifications about new matches, will
> be postponed until a functional MVP has been created. While these features
> will certainly improve the usefulness of the service, they are not required
> for delivering the core functionality of PairWise: if a user cannot find a
> suitable partner, then real-time chat doesn't add anything useful. We imagine
> the overhead involved in implementing these features is significant, and we
> would rather direct all of our efforts into the core functionality first.

#### Progress Tracking
> The team decided to use GitHub project taskboard as a primary means of tracking ticket status. This system has the advantage of being connected to git and being able to automatically update, for instance when an issue is marked as resolved. The team will also be testing out a 'ladder' for ticket tracking. The ladder is a public digital file that records the status of each ticket through colour codes, as well as which developer has been assigned to it. It cannot update automatically, but it presents its information in neat rows that make it possible to see the status of the whole project at a time. The team will decide which system to keep in a later iteration.
