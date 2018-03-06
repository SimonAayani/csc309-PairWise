# PairWise


## Iteration 02

 * Start date: Feb. 12, 2018
 * End date: Mar. 9, 2018

## Process

> One of the aims of this iteration was to find a suitable workflow and organizational structure for development. We intend to test various systems and refine our process, settling on an optimally productive process for future iterations. In particular, finding times to hold group meetings is still an issue, as there is no time during weekdays that the group can all be present. By breaking up responsibilities into discrete sections, we will minimize the need for developers on different sections to interact with those on other sections, thus reducing the need for all members of the team to meet at once regularly. Additionally, we were intending to use this deliverable to find an ideal organization system, by choosing between GitHub's project taskboard and a custom-designed project ladder. Settling on the best options will leave the team well-prepared for the upcoming final iteration.

#### Roles & responsibilities

> In this deliverable, the roles and responsibilities were more focused on the analysis of requirements, design and development of the product. Group members were assigned multiple roles that provided experience in both design and development. Since it was decided that deliverable 2 would be more focused on client-side interaction, the majority of group members were assigned front-end development tasks. Tasks were split up in such a way that had each group member create and deploy different pages/views in the PairWise web application. Back-end development looked into the setting up of database schemas and exploring the Django framework.


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
> Transform the product visuals and design into code. Create HTML and CSS files for each page view of the web application. All features part of the design must be visually present, without functionality. All pages/views in the web application must be correctly formatted as described by the UI.
>* Contributors: Yuhua Li (NaClSalt), Cindy Wang (cwang0802), Simon Aayani (SimonAayani), Deanne Madulid (deannemadulid), Evan Wallace (epwallace), Priyanka Narasimhan (PriyankaNarasi)

>* **Frontend Developers:**
> Responsibilities include implementing functionality solely for the front end/client-side. The product consists of many pages that must acquire and submit information (ie. Registration, Login, Profile Creation, Group Creation..etc). The click of a button should submit information through a contact form through the use of JavaScript. Front-end developers must ensure fully-functioning buttons and forms in the web application’s interface.
>* Contributors: Yuhua Li (NaClSalt), Cindy Wang (cwang0802), Simon Aayani (SimonAayani), Deanne Madulid (deannemadulid), Evan Wallace (epwallace), Priyanka Narasimhan (PriyankaNarasi)

>* **Backend Developer:**
> Though this deliverable is not heavily focused on backend development, the responsibilities of the backend developer in this iteration is to create a setup for backend development to use in the next deliverable. This includes understanding how to install and use the Django framework, exploring and integrating the different features Django provides including the login feature and basic setup of database schemas.
>* Contributor: Alex Hurka (ahurka)


#### Events

Describe meetings (and other events) you are planning to have:

> Salt
 * When and where? In-person or online?
 * What's the purpose of each meeting?
 * Other events could be coding sessions, code reviews, quick weekly sync' meeting online, etc.

#### Artifacts

List/describe the artifacts you will produce in order to organize your team.       

> Deanne
 * Artifacts can be To-do lists, Task boards, schedule(s), etc.
 * We want to understand:
   * How do you keep track of what needs to get done?
   * How do you prioritize tasks?
   * How do tasks get assigned to team members?

#### Git / GitHub workflow

> Evan
Describe your Git / GitHub workflow.     
Essentially, we want to understand how your team members share a codebase and avoid conflicts.

 * Be concise, yet precise.      
For example, "we use pull-requests" is not a precise statement since it leaves too many open questions - Pull-requests from where to where? Who reviews the pull-requests? Who is responsible for merging them? etc.
 * If applicable, specify any naming conventions or standards you decide to adopt.
 * Don't forget to **explain why** you chose this workflow.



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
>	* Create the database schema, with models for course, course section, group, results, searches, time of section, and user.
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
>	* As Harry (a high-achieving student), I want to list all of my proficient programming languages and current courses on my profile so that other students looking to work with these languages/topics can find me in a search and can more accurately gauge the full extent of my experience.
>	* As Lisa (a commuter student), I want to indicate my preferred meeting location on my profile so that students with similar preferences can find me in a search.
>
>* **View notifications for any activity occurring while logged out**
>	* As a returning user, I want to be notified of any activity that occurred while I was away, so that I know if I need to check my searches for new results or if I have a new message.
>	* Note: The sidebar should have "dash" as its first entry.
>
>* **View and fill in their search criteria**
>	* As Lisa (a commuter student and new user), I want to be able to search for a teammate for one of my courses with the condition that they can meet at a specific location, so that I can work with students near my home and away from campus.
>	* As Benny (a database-proficient student who lacks web design experience), I want to be able to search for a teammate for one of my courses with the condition that they are skilled in HTML, CSS, and JavaScript so that my group will have experience for different areas of the stack.
>
>* **View their active searches and existing groups**
>	* As Harry (a returning user), I want to see on the sidebar a list of the searches that I have already performed, so that I can access them to check the results again after navigating away.
>	* As Harry (a returning user), I want to see on the sidebar a list of the groups that I have already formed, so that I can see my teammates for each group that I am currently a part of.
>
>* **Implement the logic for partner searching**
>	* Determine the process for matching the search criteria to the information in a user’s profile. For example, a user specifying that they want to find a partner who has experience with Python should have a high match rate with a student who has chosen “Python” as a skill in their profile.
>
>* **View the search results screen**
>	* Create the search results screen, which will be displayed after the user performs a teammate search and should show a list of student cards, ordered from best (100%) match to worst (0%) match with regards to the user’s search criteria.
>
>* **View profiles**
>	* As Lisa (a commuter student), after performing a search and being on the search results screen, I want to be able to view the profile of a student that matched my search so that I can see their preferred meeting location.
>	* As Benny (a database-proficient student who lacks web design experience), after performing a search and being on the search results screen, I want to be able to view the profile of a student that matched my search so that I can read about their skillset in more detail to see the extent of their web language experience.
>
>* **View information about a specific group**
>	* As Harry (a student who has formed a group), I want to see the members of my group, so that I can view their names and profiles.
>
>* **View the messages screen**
>	* Create the Inbox screen, which will be displayed when the user clicks the Inbox button on the top navigation bar. This screen contains a history of the messages sent between the current user and other users.

#### Artifacts

> Simon
List/describe the artifacts you will produce in order to present your project idea.

 * Artifacts can be text, code, images, videos, interactive mock-ups and/or any other useful artifact you can think of.
 * Make sure to explain the purpose of each artifact (i.e. Why is it on your to-do list? Why is it useful for your team?)
 * Be concise, yet precise.         
   For example: "Build the website" is not precise at all, but "Build a static home page and upload it somewhere, so that it is publicly accessible" is much clearer.
