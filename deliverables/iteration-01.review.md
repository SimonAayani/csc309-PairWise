# PairWise

## Iteration 01 - Review & Retrospect

 * When: 4:15 pm, Friday February 9th 2018
 * Where: Bahen Centre for Information Technology, Room 3200 

## Process - Reflection


### Decisions that turned out well

#### Slack

> Slack allowed us to communicate with each other all at once without any hassle, and since everyone is able to see all messages, we were able to speed up our review times by announcing whenever we submitted a pull request. Most communications happened on the group channel, and so the whole team was able to easily stay up-to-date on the status of the project, as is desirable in an agile development environment. This particular advantage will become even greater when the development phase of the project begins, further advertising Slack as a valuable tool for our team.
 
#### In-Person Meetings

> In-person meetings were held mainly during tutorial times, and were effective as an end-of-week review/role assignment session. Using this time we avoided a lot of miscommuncation in assigned material, and were able to keep everyone on track, as well as provide feedback on completed tasks. An additional impromptu in-person meeting was held on Saturday, followed by the review on Friday. As expected, the in-person meetings allowed for much better focused dialogue and productivity between team members than could be achieved over Slack.
 
#### Assignment to Different Tasks

> By assigning individual team members to different smaller jobs we were able to finish larger tasks more efficiently since everyone could work on a smaller part and then merge. Even though many people worked on the same files at the same times, git conflicts were largely avoided because each person was assigned a particular location in the file. Additionally, assigning each person to a single task helped to spread out work and to make progress in all aspects of the iteration at once. Team members found they preferred working individually rather than in pairs, and we will try to tailor our jobs to support individual development.


### Decisions that did not turn out as well as we hoped

#### Meeting Times

> A Doodle poll on the availablility of our team members made it clear that there was no time during
> a work week when all members of the team could attend a meeting. This caused problems in arranging
> the online standup over Slack (which ended up not happening at all) as well as the review session.
> Meetings tended to be scheduled on-the-fly and tended to fall toward the end of the iteration. During
> those meetings we did hold outside of tutorial, at least one member was unable to attend every time.
> Currently there is no ongoing schedule of meetings, a problem we hope to solve next iteration.
 
#### GitHub Task Board

> We were planning on using Github's project taskboard to manage work for the first iteration of the
> project. The taskboard works much like a scrum board, tracking tickets through a To-Do list tab, a
> In Progress tab, and a Done tab. We thought it would be useful for organizing responsibilities and
> tasks in our project, and wanted to test out the service to see how we could use it for upcoming
> iterations. However, in the end we did not use the project taskboard majorly in the first iteration.
 
#### Uploading Notes from Google Docs

> During the planning meeting for this iteration, our notes were kept in a Google doc file. Later on,
> these notes needed to be transferred to GitHub and into the iteration plan file on the repository.
> During the process of uploading the notes, we ran into few synchronization problems in which is one
> team member was uploading a section of the notes while another was editing the notes. This led to
> inefficiencies in creating the plan file. If we are to take notes in Google docs in future iterations,
> it may be more efficient to transfer the notes to the corresponding file on the repository immediately
> after the meeting, and perform all subsequent edits through GitHub.


### Planned Changes

#### Improve Meeting Arrangements

>We have been unable to find a time during the week, other than tutorial, where all group members are available for a meeting. Ideally, we want all group members to be present for planning and review meetings. This is to ensure that everyone is on the same page and knows their responsibilities, as well as to track the progress of the project. To achieve this, we will conduct meetings through Slack and consider conducting meetings over the weekend.

#### Using GitHub Integration in Slack

> As described in the previous section, choosing Slack as our primary means of communication has been successful. To further improve our workflow, we planned to use Slack's GitHub integration to automatically notify team members about commits and pull requests. We have not yet been able to accomplish this as we are waiting for approval from the GitHub organization administrators, but we hope to take advantage of this feature in the next iteration.

#### Compare Organization Systems

> The team currently uses communication over Slack for organization of responsibilities and management of task progress. Ultimately this method is inefficient because it is easy to lose a small message in the huge numbers of posts, and not everyone will be active at any given time. We had two different ideas for long-term organization of tasks, monitoring their progress, and registering their completion. The first uses GitHub's project board, which is unfamiliar to most team members, but offers smoother integration with GitHub (connecting tasks to issues and pull requests, etc.). The second is a ticket ladder document using Google Docs, which has been proven effective in other contexts. No group members had experienced both systems, and so we could not accurately judge which system would be best suited for out project. We decided to try to deploy both during a future iteration and evaluate which organization system is most effective and should be used further. This means that both GitHub's taskboard and the ladder will be in use for the next iterations, and the group will select one system later on for exclusive use.

#### Using a task management system

> We had two different ideas for planning tasks, monitoring their progress, and registering their completion. The first is a ticket ladder document using Google Docs, which Alex has used effectively in other contexts. The second is using a GitHub project board, which is unfamiliar to most team members, but offers smoother integration with GitHub (connecting tasks to issues and pull requests, etc.). We intended to try both methods, but we did not take the time to plan a standard task workflow that everyone should adhere to. As such, we found ourselves communicating primarily over Slack about who was working on a task at a given time. This was ineffective, as people didn't always know if certain tasks had been delegated or completed. We agree that we should try each system, come to consensus on the most effective option, and utilize that system going forward.

## Product - Review


### Goals and/or tasks that were met/completed:

#### Feature List

> The final features list describes which features must be implemented in a MVP,
> and which additioanl features can be put off until after the core functionality
> is present. This list, alongside the use case diagram, will be used as a
> springboard for designating roles and responsibilities in the coming iterations.
>
```markdown
# Features required for MVP
- web interface with user accounts (need active searches to be persistent)
- user profiles: can include profile picture, bio, skills, etc.
- allow searching for partners using (at least) these core criteria:
  - course
  - time investment
  - meeting location (on campus/online/suburbs)
- allow users to view their list of potential matches for a given search;
  should be able to click to see profile, send message, send invitation, etc.
- allow users to create multiple searches (probably one per class; this might
  be restrictive for some use cases, but I think it makes sense for MVP)
- must accommodate individuals searching for groups, groups searching for
  individuals, individuals forming pairs, etc.
- show email so people can get in touch (ideally we implement chat later so
  we can bypass email altogether)
- provide methods for users to form/disband groups, send invitations,
  accept/reject invitations
- when a group reaches its desired capacity, the group members should removed
  from the active search pool

# Bonus features
- allow chat between potential partners
  - need to look into implementation overhead for realtime chat vs. sending
    email-style messages; if there are good libraries out there, we should aim
    for chat
- mobile app (or ensure mobile-friendliness)
- search based on additional criteria; some old and new ideas include:
  - skill set, such as specific languages, frontend/backend, databases, etc
  - GPA
  - personality traits
  - schedule
- notifications when new matches are found (mobile, email, etc)
- search for teammates for side projects (easy to implement)
- search for services: tutoring, textbooks, etc. (would require more work;
  probably outside the scope of this project)
- allow use by other departments/schools/groups
- rating partners
- hide people from searches (e.g. you read their profile and don't want to
  work with them, so you can remove them from your list of matches)
```

#### Use Case Diagram

> The finished use case diagram displays all actions that can
> be performed by users of the PairWise product. It provides a detailed visual of all interactions
> and functions to be implemented, and the interactions between different parts of the program.
>
> ![use case diagram](../img_src/use_case_diagram.png)

#### Main Webpage UI Mockup

> The UI mockup helped to make clear exactly which options would be available to a user from
> the main page of the website. The page's art style uses a colour scheme inspired by current
> web services available at the university, such as ACORN and Blackboard.
>
> ![main webpage mockup](../img_src/PairWise_Main_Webpage_Mockup.png)

#### Survey Information

> Toward the end of the iteration a Google Forms survey was opened to Computer Science students
> at UofT, which gathered information about students opinions on Piazza's partner finding feature.
> Questions in the survey asked if students had experienced inadequate service from Piazza group
> finder, including poor communication, difficulty of forming groups, or inability to find
> compatible partners. The results of the survey, which was answered by 23 students, indicate
> that other students recognize the same problems in Piazza group finder that PairWise aims to
> solve, supporting the motivation behind building the application.
>
> ![survey question 1](../img_src/Survey_01.png)

> ![survey question 2](../img_src/Survey_02.png)

> ![survey question 3](../img_src/Survey_03.png)

> ![survey question 4](../img_src/Survey_04.png)


### Goals and/or tasks that were planned but not met/completed:

#### Ticket List

> One of the original goals of the first iteration was to break down the features list into a product backlog, containing all the necessary tickets to construct a MVP for the project. Although the features list was completed several days before the end of the iteration, the ticket list was not assigned to anyone and was not made. GitHub’s project taskboard and the project’s ticket ladder both depend on having a defined set of tickets beforehand, and so not having a product backlog will interfere with any organization system(s) we use. We may take steps towards a product backlog at the beginning of upcoming iterations.


## Meeting Highlights

Going into the next iteration, our main insights are:

#### Scheduling Group Meetups 
> Finishing the first deliverable (which was mainly a planning phase) was manageable without many in person meetings, because of other communication methods like Slack. We were also able to accomplish most of the group brainstorming in weekly tutorials. However for upcoming deliverables (which will involve the actual creation of the product), we will look into finding better communication methods (perhaps a separate channel on Slack) to post progress, to-do lists and incomplete tasks in order for all groups members to be updated with project decisions. More in person meetings will be scheduled throughout weekends when everyone is available to discuss major design decisions and implementation.

#### Messaging/Chat Feature
> One of the most important features of PairWise is a messaging service which allows students to send requests and responses when forming groups. The chat feature is what sets PairWise apart from alternatives such as Piazza group finder. Ideas about having something similar to an email messenger, live-messaging tools like chat rooms as well as the complexity of the messaging feature were briefly discussed. The group is yet to decide on a messaging service for the MVP that is more convenient than what current course discussion boards provide. We plan on deciding on how to incorporate this feature for the next deliverable. 

#### Development of Features 
> The UI mockup and use case diagram will be used in future iterations as references for implementing the project. Both artifacts have been developed quite thoroughly and can remain useful for most of the project’s implementation. Perhaps by creating a UML Class Diagram we can describe the different classes involved and their specific responsibilities in the application, as well as to show the communication with its users. 

#### Delegating Tasks 
> Upcoming iterations of the project will be focused mostly on development of the PairWise application. As such, more long-term developer responsibilities will need to be assigned to group members. Delegation of front-end and back-end tasks will be based on the group member’s experience and interest. In particular, we found that almost all of the team had experience in web development in modern frameworks. This knowledge will influence the assignment of responsibilities during development.

