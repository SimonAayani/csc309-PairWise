# PairWise


## Iteration 02

 * Start date: Feb. 12, 2018
 * End date: Mar. 11, 2018

## Process

> One of the aims of this iteration was to find a suitable workflow and organizational structure for development. We intend to test various systems and refine our process, settling on an optimally productive process for future iterations. In particular, finding times to hold group meetings is still an issue, as there is no time during weekdays that the group can all be present. By breaking up responsibilities into discrete sections, we will minimize the need for developers on different sections to interact with those on other sections, thus reducing the need for all members of the team to meet at once regularly. Additionally, we were intending to use this deliverable to find an ideal organization system, by choosing between GitHub's project taskboard and a custom-designed project ladder. Settling on the best options will leave the team well-prepared for the upcoming final iteration.

#### Roles & responsibilities

> In this deliverable, the roles and responsibilities were more focused on the analysis of requirements, design and development of the product. Group members were assigned multiple roles that provided experience in both design and development. Since it was decided that this iteration would be more focused on client-side interaction, the majority of group members were assigned front-end development tasks. Tasks were split up in such a way that had each group member create and deploy different pages/views in the PairWise web application. Back-end development looked into the setting up of database schemas, and use of web frameworks to make the contents of the database available from a server.


>* **Requirements Analysts:**
> Analysts will be responsible of collecting and analyzing brainstormed project ideas and turning them into clear technical specifications that the group can consult. Expectations for this role include gathering and maintaining information about functional requirements, communicating the requirements to group members and provide necessary documentation that describe the features and scope of the PairWise product. Questions worth asking include:  
> - What features will exist for the MVP and why they should exist?
> - What goals will a user accomplish with a certain feature?
> - What is the ultimate goal/purpose of the product?
> - What architecture/software development tools will be used to create the product?
>* Contributors: Evan Wallace (epwallace), Alex Hurka (ahurka)

>* **UX Designers:**
> This role requires gathering functional user requirements to specify how product features can and should be implemented. UX designers must decide the web application structure, design the layout between the different user pages and the placement of the features throughout the product. They may write user stories and review use cases to describe user behaviour when the application is use, while also deciding whether the product’s structure is efficient and helps resolve problems the target audience faces.
>* Contributors: Simon Aayani (SimonAayani), Deanne Madulid (deannemadulid), Priyanka Narasimhan (PriyankaNarasi)

>* **UI Designers:**
> Responsibilities cover all visual aspects of the web application including colour scheme, font, and overall style. The UI designer may also design logo, include animations and make decisions about using different fonts for differentiating sections of the application.
>* Contributors: Yuhua Li (NaClSalt), Cindy Wang (cwang0802)  

>* **HTML and CSS Developers:**  
> Transform the product visuals and design into code. Create HTML and CSS files for each page view of the web application. All features part of the design must be visually present, with or without functionality. All pages/views in the web application must be correctly formatted as described by the UI.
>* Contributors: Yuhua Li (NaClSalt), Cindy Wang (cwang0802), Simon Aayani (SimonAayani), Deanne Madulid (deannemadulid), Evan Wallace (epwallace), Priyanka Narasimhan (PriyankaNarasi)

>* **Frontend Developers:**
> Responsibilities include implementing functionality solely for the front end/client-side. The product consists of many pages that must acquire and submit information (ie. Registration, Login, Profile Creation, etc). The click of a button should submit information through a contact form through the use of JavaScript. Front-end developers must ensure fully-functioning buttons and forms in the web application’s interface.
>* Contributors: Yuhua Li (NaClSalt), Cindy Wang (cwang0802), Simon Aayani (SimonAayani), Deanne Madulid (deannemadulid), Evan Wallace (epwallace), Priyanka Narasimhan (PriyankaNarasi)

>* **Backend Developer:**
> Though this deliverable is not heavily focused on backend development, the responsibilities of the backend developer in this iteration are focused on preparing the basis for a fully-functional backend server in the next deliverable. This includes settling on a database management system and object-relational framework, preparing a database schema and server logic such as partner matching and group management, and designing the specifications of an API that the client will be access in future iterations.
>* Contributor: Alex Hurka (ahurka)


#### Events

>* **Meetings:**
>We will meet twice in person for this phase, and code sessions if it is needed. We have decided to meet at February 17th, and March 3rd. In the first meeting, we will decide what technologies, languages, and frameworks we may for frontend and backend development, and assign everyone a role for this deliverable. In the second meeting, we will discuss the progress that had been made during the reading week and plan the rest of the iteration accordingly.

>* **Code Session:**
>We will have a code session right after the second meeting if required, to be able to collaboratively work on problems that span multiple people's components. The code session should help team members to accomplish more challenging tasks and to assess the needs of the group.

>* **Other Events:**
>During the reading week, we will cooperate with each other by using Slack, and inform each other about important changes that are made in the repository. We will have online meeting throught Slack if it is necessary.

#### Artifacts

> For this iteration we will be using GitHub's Project Board as a task board to organize tasks within the team. We decided to use the project board over the ticket ladder system mentioned in deliverable 1. This is to keep all matters for the project concentrated in our GitHub repository as well as to avoid confusion as most team members were unsure of how to use the ticket ladder system. Once tasks are assigned, an issue will be created for each task, which will then automatically be added to the task board. More information on how we will be using the task board can be seen under ***Git / GitHub workflow***.

> During the first in-person meeting we will decide on tasks that need to be completed for this iteration. We will also discuss the priority of each task, with the core tasks being assigned to different team members first. We identify core tasks as the components that need to be implemented in order to show the main functionalities of Pairwise. Tasks are assigned to team members based on how experienced and comfortable team members are with completing them. The more difficult tasks will be assigned to multiple team members.

> During future team meetings, whether in-person or through Slack, tasks can be moved around amongst team members if needed, and new tasks can be created. Any tasks regarding bug fixes will be prioritized before any non-core tasks. Ideally, bug fixes should be completed as soon as possible.    


#### Git / GitHub workflow

> The team prepared a document describing [git workflows](https://github.com/csc301-winter-2018/project-team-15/blob/master/deliverables/git-workflow.md), which each member could refer to at any time to brush up on our standards.

>* **Task Board:**
>Before beginning to work on a component of the project, developers will note it as an issue in the GitHub project taskboard and assign it to themself, or simply assign it to themself if the issue is already present. Later, this issue can be linked to commits and pull requests, and its status can be updated automatically so that we can accurately track the progress of each feature.

>* **Branches:**
>The group will use the upstream master branch on the repository as the branch for deployable features, and use other branches on the upstream for testing. Each user may create one or more personal test branches, which other users may clone from to test and integrate multiple people's work before incorporating it into the master branch. The full developer workflow for pushing a new feature to the public repository is to push their work to any branch of their choice on their personal fork of the upstream, send a pull request to merge their fork with one of their personal branches on the upstream, and merge the pull request themselves. Only after the feature has been tested can a pull request be made to the upstream master branch. This workflow allows all developers to interact with everyone's features through their branches, while keeping a clean and deployable master branch at all times Additionally, there are never any merge conflicts in this phase because only one developer pushes to their own branch.

>* **Pull Requests:**
>After testing their feature, a developer may create a pull request from their personal branch on the upstream repository to the master branch on the same repository. This pull request must be reviewed by at least one or two other members before being merged. Who reviews  the request is different in different cases, but it should generally be someone who was working on a similar or related component. After being approved, the developer is free to merge their own pull request into master. Merge conflicts are generally avoided through assigning different team members to different components. This workflow is light on peer reviews, to let team members continue to work on their own features without being pulled aside to figure out someone else's code; meanwhile, it encourages thorough testing of each feature before the request is merged. The pull request's intial comment should have an in-depth description of how the new feature should be used by other components, so that other team members can see how to use the feature without having to search through multiple separate files for documentation.



## Product

#### Goals and tasks

> **Goals:**
> Our main goal for this iteration is to allow the user to view and navigate through most areas of the application. We plan to implement the frontend user interface for the majority of the screens, using the proper layout and design. As such, the majority of the team effort will be focused on the frontend for this iteration. For the backend, we aim to have the schemas and models of the database set up as well as implement the logic behind partner searching. Below are the detailed goals and tasks we are planning for this iteration:
>
>* **View the home screen**
>	* Create a splash screen with the PairWise name, description, and options to register and log in.
>
>* **View and navigate using the navigation bar**
>	* Create a navigation bar that is shown across the top of the page, with buttons linking to inbox, profile, and sign out.
>
>* **Set up initial database schema**
>	* Create the database schema, with models for courses, users, groups, searches, search results, and user profiles.
>
>* **Create a new user account**
>	* As a student, I want to click on “register” on the main page and be taken to the registration page so I can create an account. This page should include a form with the following fields:
>		* Email
>		* First name
>		* Last name
>		* Password
>		* Confirm password
>
>* **Log in with an existing user account**
>	* As a student, I want to click on “login” on the main page and be taken to the login page so I can log in to my account. This page should include a form with the following fields:
>	* Email
>	* Password
>
>* **Fill in their user profile**
>	* As an advanced fourth-year student, I want to list all of my proficient programming languages and current courses on my profile so that other students looking to work with these languages/topics can find me in a search and can more accurately gauge the full extent of my experience.
>	* As a commuter student, I want to indicate my preferred meeting location on my profile so that students with similar preferences can identify those preferences in a search.
>
>* **View notifications for any activity occurring while logged out**
>	* As a returning user, I want to be notified of any activity that occurred while I was away, so that I know if I need to check my searches for new results or if I have a new message.
>	* Note: The sidebar should have "dashboard" as its first entry.
>
>* **View and fill in their search criteria**
>	* As a commuter student and new user, I want to be able to search for a teammate for one of my courses with the condition that they can meet at a specific location, so that I can work with students near my home and away from campus.
>	* As a database-proficient student who lacks web design experience, I want to be able to search for a teammate for one of my courses with the condition that they are skilled in HTML, CSS, and JavaScript so that my group will have experience for different areas of the stack.
>
>* **View their active searches and existing groups**
>	* As a returning user, I want to see on the sidebar a list of the searches that I have already performed, so that I can access them to check the results again after navigating away.
>	* As a returning user, I want to see on the sidebar a list of the groups that I have already formed, so that I can see my teammates for each group that I am currently a part of.
>
>* **Implement the logic for partner searching**
>	* Determine the process for matching the search criteria to the information in a user’s profile. For example, a user specifying that they want to find a partner who has experience with Python should have a high match rate with a student who has chosen “Python” as a skill in their profile.
>
>* **View the search results screen**
>	* Create the search results screen, which will be displayed after the user performs a teammate search and should show a list of student cards, ordered from best (100%) match to worst (0%) match with regards to the user’s search criteria.
>
>* **View profiles**
>	* As a commuter student, after performing a search and being on the search results screen, I want to be able to view the preferred meeting location for a student that matched my search by looking at their profile.
>	* As a student with proficiencies that are deep but not broad, after performing a search and being on the search results screen, I want to be able to view the profile of a student that matched my search so that I can read about their skillset in more detail to see the extent of their experience in my areas of inexpertise.
>
>* **View information about a specific group**
>	* As a student who has formed a group, I want to see the members of my group, so that I can view their names and profiles.
>
>* **View the messages screen**
>	* Create the Inbox screen, which will be displayed when the user clicks the Inbox button on the top navigation bar. This screen contains a history of the messages sent between the current user and other users.

#### Artifacts

>**Website View Mockups**
  >* A set of images drawn to show what the layout of our user interface will look like. These images will help us get a general idea of what we want our website to look like and will guide every member of the team to strive for the same outcome. Using these images will also avoid confusion of which functionality is to be present on each page/view.
>
>**Walkthrough Video**
  >* A video which will show all the functionality and the workflow of our application step by step. This will allow users to better understand how the application works, and how to access everything.
>
>**User Interface**
  >* The purpose of the user interface is to allow users to seemlessly navigate through our web application without trouble. Creating a polished user interface allows us to store a large amount of information on the screen while not confusing anyone who is using our service.
>
>**React App**
  >* The purpose of the React App is to be able to communicate between the front-end and the back-end. It is important for our application as it allows us to register and store user information in a database which we can access on login to create user specific sessions. As a result of creating sessions we are able to deliver user specific information (Such as profile, and groups).
>
>**Django Database**
  >* Set up a database to store all of the users pertinent information. Setting up such a databse allows us to fetch user specific data for our users as well as a directory to iterate through when creating our search results.
