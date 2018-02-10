# PairWise

## Iteration 01 - Review & Retrospect

 * When: 4:15 pm, Friday February 9th 2018
 * Where: Bahen Centre for Information Technology, Room 3200 

## Process - Reflection

_This entire section is optional. Note that you will have to fill it out and more for the next 3 deliverables so it's good to start soon and get feedback._

### Decisions that turned out well

List process-related (i.e. team organization) decisions that, in retrospect, turned out to be successful.

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

#### Integrate GitHub into Slack

> Integrating GitHub into Slack will allow for easier communication over changes and issues that arise throughout the project. We are already using Slack to communicate with each other when making significant commits or pull requests, however having it automated would greatly improve workflow.

### Test out Organization System between Task Board and Ladder

> We are currently using Slack to communicate about current tasks that are being completed. Ultimately, this is inefficient because no one is always on active on Slack, and it is easy to miss a message when scrolling down the chat. We considered using two methods to organize tasks. The first was a task ladder located in Google Docs, and the second was GitHub's built in project board. We intend to test out both methods for future tasks, using one each for future deliverables and evaluating which organization system is most effective and should be used further.

## Product - Review

_This entire section is mandatory._

### Goals and/or tasks that were met/completed:

 * From most to least important.
 * Refer/link to artifact(s) that show that a goal/task was met/completed.
 * If a goal/task was not part of the original iteration plan, please mention it.

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

#### Using a task management system

> We had two different ideas for planning tasks, monitoring their progress, and registering their completion. The first is a ticket ladder document using Google Docs, which Alex has used effectively in other contexts. The second is using a GitHub project board, which is unfamiliar to most team members, but offers smoother integration with GitHub (connecting tasks to issues and pull requests, etc.). We intended to try both methods, but we did not take the time to plan a standard task workflow that everyone should adhere to. As such, we found ourselves communicating primarily over Slack about who was working on a task at a given time. This was ineffective, as people didn't always know if certain tasks had been delegated or completed. We agree that we should try each system, come to consensus on the most effective option, and utilize that system going forward.

#### Using GitHub integration in Slack

> As described in the previous section, choosing Slack as our primary means of communication has been successful. To further improve our workflow, we planned to use Slack's GitHub integration to automatically notify team members about commits and pull requests. We have not yet been able to accomplish this as we are waiting for approval from the GitHub organization administrators, but we hope to take advantage of this feature in the next iteration.

## Meeting Highlights

Going into the next iteration, our main insights are:
 * Figuring out optimal ways for everyone to meet, so everyone is updated with project decisions
 * Deciding about the messaging/chat feature for the product
 * Using the info from use cases/UI/features list to assist with development
 * delegate front-end/back-end tasks based on people's experience/interest
 
 * 2 - 4 items
 * Short (no more than one short paragraph per item)
 * High-level concepts that should guide your work for the next iteration.
 * These concepts should help you decide on where to focus your efforts.
 * Can be related to product and/or process.
