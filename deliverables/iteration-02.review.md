# PairWise/Group 15



## Iteration 02 - Review & Retrospect

 * When: Saturday March 10th, 2018
 * Where: BA3200

## Process - Reflection

#### Decisions that turned out well

  > Using GitHub Issues for Task Management
  >* 'Issues' are a GitHub feature and are a great way to keep track of tasks, improvements, and code issues for projects. They are similar to emails except that they can be shared and discussed with other team members. This decision to use GitHub Issues was extremely useful, as it allowed our group to claim certain tasks to let others know what each member was working on. This was an easier communication method rather than having to ask other group members repeatedly about which tasks were already being worked on. Since we could assign each task to a group member there was no confusion as to who was doing what.

  > Using Slack’s GitHub Integration for Project Updates
  >* Using Slack’s GitHub bot allowed us to see when important events occurred, such issues and pull requests being opened and closed, in real time. This kept everyone informed of changes to files and emerging bugs. We found that it’s easy to overlook emails from GitHub (especially when they get bundled together), but desktop and mobile notifications from Slack were easier to notice.

  > Removing the Task Ladder
  >* We decided against using both the task ladder and the GitHub task board for organizing our task list because we discovered that Github issues and their project task board served our purposes well enough on their own. We thought there would be too much overhead in simultaneously using two task management systems to find the best fit, and that synchronization issues between the two systems might occur.


#### Decisions that did not turn out as well as we hoped


  > Communication over Reading Week
  >* We had hoped to hold in-person meetings in our smaller frontend/backend groups over reading week, however this did not work out as many of our team members ended up being away from Toronto. We did a lot of brainstorming before the break, but didn’t come up with concrete ideas about who needed to accomplish what, and by what date. We all had many overlapping midterms and due dates upon returning from reading week, so it was difficult for us to meet, make decisions, and start making actual progress. As a result, finishing this deliverable was rushed, and we could not implement all the features we wanted.

  > Developing Clear Standards for Code
  >* When we developed the frontend, we delegated different views to different team members. This divide-and-conquer approach allowed us to create many different pages in a short period of time, but some of us used conflicting frameworks (React and jQuery, Bootstrap and Semantic UI, etc.). As a result, we had to spend a great deal of time combining code and debugging. Our development process would have been smoother if we ensured that everyone was using the same frameworks and the same coding conventions.

  > Separating Frontend and Backend Slack Channels
  >* We decided to have separate channels in Slack for the frontend and backend, with the purpose of being able to better organize our discussions according to different parts of the stack. We had split the team up into their roles and intended for the channels to allow for easier communication, but ended up having most of our discussions with the whole team just in case anyone else had valuable input.

 #### Planned changes

> Keep Track of Code Conventions
>* In the next iteration, we will maintain a document outlining the frameworks and practices that should be adhered to when developing. We believe following this set of guidelines will minimize the amount of time we spend combining code. To ensure we adhere to these guidelines, we will open pull requests early so that we can receive and offer feedback on one another’s work, and document new standards as they emerge.

> More Coding Sessions
>* We plan to have more in-person coding sessions as we found them very useful for this iteration. Coding sessions were productive and allowed for instant communication between team members. In the next iteration we are planning to have weekly coding sessions on the weekends, as that is when all team members are generally available to attend.

  > Stop Segregating Frontend/Backend Communication in Slack
  >* We plan to move away from this format of segregated channels so that we can create a workflow that is constantly moving through each end of development. It will increase our efficiency if we are able to properly communicate with the other end so that our implementations are compatible.


## Product - Review

#### Goals and/or tasks that were met/completed:
  >* Views
  		>* [View 1](../img_src/view1.jpg)
  		>* [View 2](../img_src/view2.jpg)
  		>* [View 3](../img_src/view3.jpg)
  		>* [View 4](../img_src/view4.jpg)
  >** [Search page](https://github.com/csc301-winter-2018/project-team-15/issues/40)
  >* [Search results page + viewing other users’ profiles](https://github.com/csc301-winter-2018/project-team-15/issues/32)
  >* [Profile page](https://github.com/csc301-winter-2018/project-team-15/issues/31)
  >* [Initial Database Schema](https://github.com/csc301-winter-2018/project-team-15/pull/26)
  >* [Dashboard (with sidebar + notifications)](https://github.com/csc301-winter-2018/project-team-15/issues/25)
	>* [Sidebar](https://github.com/csc301-winter-2018/project-team-15/issues/39)
  >* [Navigation Bar](https://github.com/csc301-winter-2018/project-team-15/issues/33)

#### Goals and/or tasks that were planned but not met/completed:

> Connecting Frontend to the Database
>* We originally planned to have the website send and receive data from the database. While we did create the database schema and get our Django project running, we ran into issues with cross-origin resource sharing between our development servers, and decided to use dummy data to make developing the frontend more efficient. In the next deliverable, we will assign a role for integrating the frontend and backend.

> Implementing the Partner Match Algorithm
>* We made some effort in implementing the partner match algorithm, but found that we needed more extra help with the frontend as the deadline approached. Interestingly, we found that the more developed the frontend became, the more we needed to refine how matching should work: for instance, questions about what search criteria should be mandatory, what information should be stored in user profiles, and how that information will be available to the matching algorithm arose from our implementation of the frontend. We’ll use our insights from the frontend development to refine our schema and matching in the next deliverable.

## Meeting Highlights

Going into the next iteration, our main insights are:

#### Finish up user pages/views (Frontend):

> Since it was decided by the group members that this deliverable would be mostly focusing on frontend development, the creation of the user pages, that is, all the views/screens on the web page the user can visit, was important to complete in this deliverable. Though we were able to accomplish most of the views within the user’s account, features like the Group tab (in the sidebar) and the Inbox (in the navigation bar), are not functional and are yet to be implemented. On top of that, a proper login system using React as opposed to our existing login system (built with JQuery) must be created for the next deliverable to integrate with the rest of the frontend code.

#### Connect frontend to backend (fetch from database)

> The next deliverable will heavily focus on backend development. Which includes removing all hard code and extracting and storing user information in and out of the database system. Implementing the features on the MVP that heavily rely on calculations, algorithms, communication between multiple users as well as the login system will be our main priority. One of the group members was able to create a setup of the database which will be the foundation to how the group approaches the third deliverable.

#### Search algorithm/matching system

> The most important characteristic of the Pairwise application, with no doubt is its complex algorithmic feature which performs a search and matches potential partners to the user based on profile similarities and personalities. In this deliverable we were able to come up with a simple structure of how the search feature will be presented to the user. The search feature created is purely frontend, as it reads data from the [Cobalt API](https://github.com/cobalt-uoft/cobalt) and presents a list of courses and programming languages the user can select from. In the backend, the search feature must use the user’s input and traverse through its stored list of other user profiles the output a list of results in order of best to worst match.

#### Delegation of Roles

> Since the focus of the next deliverable is going to be much different than that of this one, the delegation of tasks specific to the goals of the next deliverable is important. Roles and Responsibilities in this deliverable were not specific to one person, as many people had a chance to develop in the frontend. In the next deliverable, we plan to assign specific roles to every member so we are able to monitor every group member's progress which will allow more tasks for backend, as well as the culmination of the entire product to be completed in advance.
>
>
	>*backend: implementing authentication/session persistence
	>*middle: finalizing the Django server’s RESTful API and ensuring the frontend communicates with it properly
	>*backend: implementing user messaging
	>*backend: designing and implementing the matching algorithm
	>*frontend: creating the search results page
	>*frontend: integrating messaging and groups requests with the current views
