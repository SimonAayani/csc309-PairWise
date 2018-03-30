# PairWise


## Iteration 3

 * Start date: Mar. 18, 2018
 * End date: Mar. 30, 2018

## Process

>Looking back at the last two iterations, and comparing the process methods for both, we are able to see vast improvements in the project workflow and organizational structure for development. Notably, the software tools that were used for communication and organization purposes including Slack’s GitHub integration and GitHub issues turned out to be extremely useful as it provided us with updated information about assigned tasks, file changes and code bugs. We plan to continue using these tools during this deliverable. In regards to the group’s organization, our plan for the last deliverable was to assign the major role of Frontend Developer to multiple group members, where each group member had the responsibility to implement a certain user view in the webpage. However, because we had not outlined clear standards for code, it lead to incredibly different unmergeable implementations. This strategy was indeed inefficient as it lead to a lot of unused code, wasted time and the group having to re-implement much of the frontend work in the little time that was left. Clearly, group organization is still an issue, and we plan to find an optimal strategy to divide up work within the given time frame.

#### Changes from previous iteration

>* **Delegation of Roles:**
>Delegation of roles is a main priority in this deliverable, as our strategy to delegate multiple group members to a single role in the previous deliverable was not as successful as it could have been. Although splitting up frontend tasks by the different user pages may have been a good idea, the strategy was not successful because the members were not provided clear enough specifications about how to implement the user page they were given. Hence delegation in the final deliverable will focus on assigning responsibilities and authority to group members in order to complete a clearly defined and agreed upon task, which will be followed up upon by other group members to track progress, successes and failures. Specifications for each task will be decided by all group members including which software/tools to build with, goals, functionalities and outcomes.

>* **Meetings:**
>In the last deliverable we found having in-person coding sessions over the weekends to be quite useful as we were able to ask questions to each other and solve code bugs quicker. However we were not able to have enough coding sessions as we wanted to. We are planning to have more in-person coding sessions spread throughout the next few weeks to ensure that group members have ample time to discuss/assign tasks, work on tasks, and share progress. If necessary, we also aim to have a few coding sessions on weekdays.

>* **Create a Measurable Organization System:**
>It would be unreasonable to assign major tasks like implementing a search algorithm, or connecting frontend with backend to a single group member to complete. Not only does it risk failure to complete the task, but also does not allow enough time for learning. So we have decided to create a step-by-step system that outlines the small steps and processes needed to be completed to ensure the desired outcome. Group members will be assigned smarter and measurable tasks, and will be given earlier deadlines for said tasks spread throughout the next few weeks. This way, we will have a steady flow of development of new features; this process will allow time for any errors/problems faced or learning curves and avoid last minute work, while still keeping the project on track.

#### Roles & responsibilities

>* **Project Supervisors:**
>Supervisors have the responsibility of collecting group decisions from the planning meeting and keeping track of the product’s progress. They will collect and maintain information about tasks, including tasks that have been assigned to group members, completed and incomplete tasks. Expectations of the Supervisor is to host weekly meetings to review each individual’s progress and check if they have been keeping up with their deadlines, discuss solutions/problems that arose, and re-distribute tasks if necessary. 
>* Contributors: Evan Wallace (epwallace), Alex Hurka (ahurka)

>* **Frontend developers:**
>Frontend developers will continue to implement views in the application that were not completed in the previous iteration. They will remove the dummy code and make changes where necessary to follow best React practices. These developers will also be involved in enhancing the product to be more visually appealing, in terms of colour scheme and layout, using Semantic UI and custom CSS.
>* Contributors: Yuhua Li (NaClSalt), Cindy Wang (cwang0802), Simon Aayani (SimonAayani), Deanne Madulid (deannemadulid), Evan Wallace (epwallace), Priyanka Narasimhan (PriyankaNarasi)

>* **Backend developers:**
>Backend developers will improve existing server logic, providing new database support and logic for new features such as user messaging. They will solidify a login and registration system, as well as access restrictions such as requiring a user to create a profile before they can launch a search, and work on improving partner matching logic using additional criteria from the search form and user profiles.
>* Contributor: Alex Hurka (ahurka)

>* **Middle end:**
>This role involves figuring out how to integrate frontend and backend to ensure proper communication and response between the two. 
>* Contributors: Yuhua Li (NaClSalt), Cindy Wang (cwang0802), Simon Aayani (SimonAayani), Deanne Madulid (deannemadulid), Evan Wallace (epwallace), Priyanka Narasimhan (PriyankaNarasi), Alex Hurka (ahurka)


#### Events

>* Continuing from previous iterations, we plan to have in-person meetings and coding sessions on Fridays (March 23) and weekends (March 24), in BA3200, to allow for easier direct communication and discussion.
>* On Wednesdays March 21 and 28 at 8pm, our Project Supervisor will facilitate a quick meeting on Slack to review our weekly deadlines. These meetings will keep everyone aware of the current state of the project, and will provide an opportunity to reprioritize tasks and redistribute workloads if necessary.
>* We will also continue to update each other over Slack throughout the week to ensure that the team is aware of each member’s activities.
>* Review meeting and video production will be held on Thursday March 29. Review meeting will be held during tutorial time at noon; video production will begin at 4:00 pm.


#### Artifacts

>* **GitHub Issues and Task Board**
> After discussing the features left to implement and the tasks associated with them, we will create each task as an issue on GitHub and assign them to the most appropriate member, based on which features they have previously worked on. The issues help us to keep track of our remaining tasks for the iteration, and also have labels to help with indicating which part of the stack they are associated with and the priority they should take. As this is our final iteration, any tasks related to the application’s core functionality will take high priority.
>
> Throughout the iteration developers can refer to the project task board, which shows the progress of our issues, to see which components need work and which have already been assigned. Moreover, issues can be linked to pull requests so that the task board remains up to date automatically whenever they are resolved. Over the course of the iteration, as other issues and bugs emerge, these can be added to the board as necessary.

> The [git workflow](https://github.com/csc301-winter-2018/project-team-15/blob/master/deliverables/git-workflow.md) document created in the previous iteration explains the processes followed by the team, from task creation, to code commits, to push requests.


#### Git / GitHub workflow

>* **Branches:**
>The group will restrict the upstream master branch on the repository to contain only tested and deployable features, and use other branches on the upstream for testing. Each developer may create one or more personal test branches on the upstream, from which other developers may clone to test, correct, and integrate multiple people's work before merging them into the master branch. The full developer workflow for pushing a new feature to the master branch is to push their work to any branch of their choice on their personal fork of the repository, send a pull request to merge their fork with one of their personal testing branches on the upstream, and merge the pull request into the personal branch themselves. We chose this workflow because it allows all developers to interact with everyone's features through their branches, while keeping a safe, clean, and deployable master branch at all times. Additionally, the stages of merging features into people's personal branches tend to be free from merge conflicts, as these branches contain the work of only one developer at most times.

>* **Pull Requests:**
>After testing their feature(s), a developer may create a pull request from their personal test branch on the upstream repository to the upstream master branch. This pull request must be reviewed by at least one or two other developers before being merged. Ideally the reviewer should also be shown a demonstration of the feature working successfully. Which developer reviews the request is different in different cases, but it should generally be someone who was working on a similar or related component. After having their work approved, a developer is free to merge their own pull request into the master branch. In this iteration we want to place more focus on peer reviews, to catch situations in which multiple people working on the same component, or are making separate components incompatible. This will also help to avoid or resolve merge conflicts, by allowing the authors of the conflicting commits to work on a solution through the code review. The pull request's initial comment should have an in-depth description of how the new feature should be used by other components, so that other team members can see how to use the feature without having to search through multiple separate files for documentation.



## Product

#### Goals and tasks
>Our goal in this iteration is to finish implementing the features for the MVP of the PairWise product. We will be focusing mostly on completing core MVP functionality in the backend, and the required webpages to access those backend services; polishing frontend display with new CSS components; and making the frontend components dynamically update themselves by sending requests to the backend servers.

>Priority of features was decided by the group during the plan meeting. We decided to give most attention to creating a good user experience, which led us to give highest priority to the tasks of making the frontend dynamic and aesthetically pleasing. Leaving any static components of important sections like the search results page would make the application completely worthless to users who wanted to use those features, and so the task of making the frontend dynamic was given highest priority. After that, the application's current appearance is not polished and different pages lack a unified design style. The group decided that a smooth and unified appearance is extremely important in user attraction and retention, and an application with useful features but with a rough appearance would not be likely to become successful. On these grounds we decided that improving the application's appearance was also among the top priorities. Otherwise, the most important factor in the prioritization of features was how strongly they connected with core MVP features as specified in the features list made in the first deliverable. For example, creating user accounts and profiles and performing searches were high priority with respect to non-core features such as messaging. For the most part, the logic was to give higher priority to parts of the application that appear earier in most use cases. Creating a user account is a prerequisite for almost any use case, and so it was given higher priority than other features such as group invitation management, which occurs in later and fewer use cases. Additionally, convenience features like user messages and deleting searches were designated as bonus features for the project, and thus were given lowest priorities. Users can get the full experience of the application's main use cases, and form groups from our services, without those features. For example, messaging allows users to communicate with each other, which they can already do (albeit less conveniently) using email addresses we provide within user accounts and profiles.

>* **Connect frontend to backend**
>* Learn how to connect a React frontend with a Django REST Framework backend to be able to send and retrieve data from the database. Gather information from the backend with which to populate areas such as the dashboard's sidebar and search results page, to give each user the information that they input previously, or that is associated with their account.
>	  * As a returning user, I want to have my account information and activity saved after leaving the website or logging out, so that I can visit the website sometime in the future and have it remember my profile, my ongoing searches, and my groups, so that I do not need to retrace my previous steps next time I log in.
>   * As a first-time user, when I launch a search I want my new account and profile to become immediately visible to other users in their searches so that I can receive invitations or messages from them right off the bat.
>   * As a student with high requirements, I want the search results I receive to reflect the input other users provided, so I receive accurate information by which to judge potential partners.
>   * As a new member of several groups in the PairWise application, I want the list of groups I can view from the sidebar to reflect the groups I have joined, so I can quickly access information about my own groups without having the interface crowded with groups that are not my own.

>* **Improve frontend appearance**
>* Remove static HTML elements and frontend components that were put in place during the previous deliverable. Improve the layout and of the website using new CSS components, and match the website's style and colour scheme to the UI design from the previous deliverable. Add the PairWise logo and other visuals to the splash screen.

>* **Create new user accounts**
>* Allow a user to create a new account, which contains basic information such as names, password hash, and email, that is stored in the database. This information will be used to allow the users to authenticate later on, and to associate user profiles, searches, groups, and messages with the user that created them.
>   * As a newcomer to the PairWise application, I want to click on “register” on the main page and be taken to the registration page so I can create an account and be able to access the application through that account. This page should include a form with the following fields:
>		  * Email
>		  * First name
>		  * Last name
>		  * Password
>		  * Confirm password

>* **Implement partner searching logic**
>* Determine the process for matching the search criteria to the information in a user’s profile. For example, a user specifying that they want to find a partner who has experience with Python should have a high match rate with a student who has chosen “Python” as a skill in their profile. Find a way to store and access this information, and develop a scheme by which multiple criteria can be assessed to produce an overall estimate of how well partners match.
>   * As a student in a open-ended project course, I want to be able to search for developers that are proficient in the languages I know, so that the group will settle on a language that they all like and avoid conflicts about which language to use.
>   * As a commuter student, I want to be able to search for other students that live in my neighborhood, so we can work in a local place instead of commuting to campus for meetings and work sessions.

>* **Send and accept/reject invites from other users**
>* Provide a means for users to send group invites to other users, which the other user can accept in order to form a group. Allow users to view a list of invitations they have, from which point they can accept or reject any of these invites. Also allow users to view all the invites they have sent, so they can track the status of those invites.
>	  * As a user, I want to click on “send invite” after selecting a user on the search results page, so that the other user can be informed that I want to work with them.
>	  * As a user, I want to see my invitations to join groups, and be able to respond to the invitation by clicking “accept” or “reject”, so that I can .
>   * As an extroverted user, I want to see all the many invitations I have sent out, so I can remember which users I have previously contacted.

>* **View existing groups**
>* Allow users to access a list of the groups that they have become members of, containing links to pages from which they can view more information about these groups and their other members. From this page, they can perform operations on the groups, such as sending messages to other members of the groups, viewing a thread of group messages, and leave the group if desired.
>	  * As a returning user, I want to see on the sidebar a list of the groups that I have already formed, so that I can see my teammates for each group that I am currently a part of.

>* **Send messages to other users**
>* Create the Inbox screen, which will be displayed when the user clicks the Inbox button on the top navigation bar. This screen contains a history of the text messages sent between the current user and other users. Text messages are distinct from group invites, and contain only sentences and other communications between users. The purpose of these messages is to let users learn about each other beyond their profiles, and to allow coordination of group activities without requiring users to leave the PairWise app.
>   * As a new first-year student, I want to be able to talk to classmates I haven't met so I can learn more about their personalities before I agree to work with them.

>* **View notifications for any activity on the dashboard**
>* Display new activity, such as new received messages or invites, all in one place on the dashboard page. These notifications should reflect eveything that has happened since last time the user logged in, so that they can quickly catch up on new activity without having to look through all their searches and message feeds.
>	  * As a returning user, I want to be notified of any activity that occurred while I was away, so that I know if I need to check my searches for new results or if I have a new message.
>   * As a user with pending invites, I want to be able to quickly see if any of those invites have been accepted, so I can take action communicating with members of the new groups as soon as they form.

>* **Delete groups and searches**
>* Allow users to back out of searches and groups, so that their previous choices are not permanent, and they can reset their webpage to a clean state after finishing all their group projects.
>	  * As a student beginning the second assignment of a course, I want to delete an existing search for the course's first assignment to be able to launch a new search for the second assignment, with a different set of criteria to match the new assignment.

#### Artifacts

>* **PairWise Logo:**
>The PairWise product logo will be displayed in the corner of most pages, as well as in a central position on the splash page.
> * Purpose: Gives our product a unique symbol which users will be able to easily identify, and affiliate with PairWise, which will in turn improve brand recognition.

>* **Splash Page:**
>Upon loading the PairWise website, users will be greeted by a splash page that describes the product, allows them to register for an account or log in with an existing account, and presents the logo and other visual elements. This page must be accessible from a browser, to allow users access to login and registration before they are able to access core website features.
> * Purpose: Allows users to get familiarized with the concept of the application, and also provide an access point for unregistered or unauthenticated users to authenticate to the website (through registration).

>* **Login and Registration Tab:**
>Upon trying to log in from the splash page, a user will see a pop-up on top of the splash page that prompts them for their username and password, which will allow them to log in if they enter recognized credentials. First-time registering users will be prompted for a username, a password and password confirmation, as well as name and email to be used in search results. If the user logs in successfully they will be taken to the main page. Otherwise they will receive a message explaining why they were unable to log in.
> * Purpose: Allows us to gather information the user has submitted and by connecting to our database we are able to authenticate or register the users credentials.

>* **Main Page:**
>After logging in, the user will see a summary page which shows their newest activity, including invites and messages from other users. From the main page a user will be able to respond to messages, and see a sidebar that lists their ongoing searches and active groups. The sidebar will also give an option to launch a new search.
> * Purpose: The main page gives us the ability to display all relevant information in a manner that is easily accessible by the user.

>* **Profile Pages:**
>Creating a profile is required to use most features of the PairWise website. A view/edit/create profile option will be available at all times. Upon clicking this button, a user will be able to view their own profile, including a profile picture, bio, (optional) home neighborhood, current and previous courses, and a list of their skills. They will also be given an option to edit the profile. Users will also be able to view the profiles of other users through search results and groups, which will present the same profile viewing page without the option to edit.
> * Purpose: Viewing other users’ profiles allows a user to judge someone’s experience and personality before requesting to join their group, which is important to let users decide which group partner is best for them. As such, each user must be able to create a profile and view someone else’s profile through the profile page.

>* **Search Form:**
>Upon launching a new search, a user will be presented with a list of fields to specify criteria of their search such as the course with which the search is associated, required skills, project name and description, desired meeting times and expected weekly work hours. The user will be able to submit this search, which will gather results according to their criteria and show them a list of results.
> * Purpose: To gather all search criteria the user is searching for and use this information with our implemented search algorithm to get other users who meet the criteria.

>* **Search Results Page:**
>Search results are displayed as a list of search result components, which prominently display the profile picture, usernames, names, and email addresses of all users that matched the search’s criteria. Joinable groups will also be displayed in this results section, although they will typically have a default group image instead of a profile picture, and will list all members’ usernames instead of a group name. Results are ordered according to how well they matched the criteria, although that value will not be presented to users. Users may view the profiles of other users that matched their search criteria, and send group invites to them. The profiles of group members can be viewed through a link to their group page.
> * Purpose: To give a user a suggestion of which other users and groups best meet the criteria they set in a search, so the user can quickly see the profiles of other users who meet their specifications.

>* **Group Page:**
>The group page displays components containing profile pictures, usernames, and names of all members of a group. Through this page a user can view their own group and access group-specific messages and notifications, and leave the group if they wish. The search results page also gives users access to the group pages of groups they are not yet part of, allowing them to send messages to the group and request to be added to the group.
> * Purpose: To allow a user to see more details about the members of a group and engage in group-wide chat with them, whether the user is already a member of the group or looking to become a member.

>* **Final Product Demo:**
>A short video presenting the purpose of the PairWise app and its problem domain. The video will present a tutorial of standard product use, from logging in to an account to launching a search to viewing search results to group formation, and demonstrate the main features of the app. Further product details including possible future developments will also be discussed.
> * Purpose: Provides users with a walkthrough of the application workflow and purpose, which will assist users in finding and utilizing all the functionality of PairWise in a straightforward manner. Also gives a brief introduction to standard use cases of the application and the problems it solves, which could help attract new users.
