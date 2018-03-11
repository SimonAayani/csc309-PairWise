# GitHub Workflow
## Preface
This document will hopefully be something we can use to standardize our
GitHub usage throughout the project.
I've reviewed a lot of StackOverflow pages, GitHub documentation, and articles
to figure out best practices for collaborating using GitHub, and these are the
standards I think we should follow to minimize merge conflicts and similar
headaches.
If you have any questions, suggestions, concerns, or disagreements, let us know
on Slack and we can adjust this document.

## Task Management: Using the task board and ticket ladder
### Task board (GitHub Projects)
The workflow for planning/assigning tasks using GitHub is pretty simple:
creating an "issue" creates a comment thread that we can use to discuss features
and bugs in depth.
An issue page looks a lot like a pull request page, and we'll use them
similarly: they'll help us keep focused discussion in one place for easy
reference (instead of getting lost in Slack).
Issues can be "open" or "closed": being open implies that further action is
required.
They can also be tagged with labels and assigned to teammates.

Issues integrate well with the project board we talked about before: when issues
are opened, a card is automatically added to the "to-do" column; when they are
closed, the associated card moves to the "complete" column.
Note that pull requests can also be added to the project board. Here's an
example project board from the GitHub docs:

![example project board](https://user-images.githubusercontent.com/7321362/31255877-102f6e12-a9e4-11e7-8d67-ec8cfdc32f5a.png)

#### Workflow
1. Create an issue by clicking on the green **New Issue** button on our
   [issues page](https://github.com/csc301-winter-2018/project-team-15/issues).
   Make sure you use a descriptive title; if more detail is required, provide it
   in the comment area.
   On the right hand side, select the appropriate label(s) and projects. If the
   task has already been delegated to somebody, specify them in the "assignees"
   section as well.

2. Creating an issue will automatically create a ticket in the "to-do" column of
   the [project board](https://github.com/csc301-winter-2018/project-team-15/projects/2).

3. When you begin working on a ticket, drag it from the "to-do" column to the
   "doing" section. If you're not already listed as an assignee, visit the
   associated issue page and add yourself.

4. When the issue has been resolved, we close the issue. If this resolution
   involves merging code into master, then that pull request should be completed
   before the issue is closed. You can do this manually by clicking on the
   "close issue" button at the bottom of the issue page, or you can include
   "Fixes issue #X" in the pull request body, where X is the issue number. See
   [here](https://github.com/blog/1506-closing-issues-via-pull-requests) for
   more details.

### The ticket ladder
*coming soon*

## Collaborating with branches and pull requests
### Some Git terminology and basic commands
- **clone**: creating a local copy of an existing Git repository on your local
  machine; when you clone, you may or may not have permissions to push back to
  the original repository
- **fork**: creating a remote copy of someone's existing GitHub repository on
  your GitHub account; if you clone a fork you made, you definitely have
  permissions to push back to your fork, but usually not the original repo
- **remote**: a repository stored outside of your local repository that you
  can pull from (and maybe push to); when you clone, the default remote
  repository is known as the *origin*
- **origin**: the repository which `git pull` and `git push` interact with; if
  your repository was cloned, this defaults to the original repository
    - if you clone from someone else's repository, their repository is your
      origin
    - if you clone from your fork, **your fork** is the origin; the original
      repository is not a remote until you specify it
- **upstream**: generally, upstream refers to the repository from which you
  forked; you typically need to specify the upstream repository yourself

To list all remotes your local repository knows about (I'm in my local repo
from deliverable 1):
  ```bash
  > git remote -v
  origin	https://epwallace@github.com/epwallace/project-team-15.git (fetch)
  origin	https://epwallace@github.com/epwallace/project-team-15.git (push)
  ```
As expected, my fork is the origin.
If I wanted to update my fork's master branch to match the current state of
the group's master branch, I'd need to tell my repo that the group's branch
is *upstream*:
  ```bash
  > git remote add upstream https://epwallace@github.com/csc301-winter-2018/project-tram-15.hit
  > git remote -v
  origin	https://epwallace@github.com/epwallace/project-team-15.git (fetch)
  origin	https://epwallace@github.com/epwallace/project-team-15.git (push)
  upstream	https://epwallace@github.com/csc301-winter-2018/project-team-15.git (fetch)
  upstream	https://epwallace@github.com/csc301-winter-2018/project-team-15.git (push)
  ```
  Now I can pull from the group repo by telling Git to pull from *upstream*:
  ```bash
  > git checkout -b master
  > git pull upstream master
  ```

### The master branch
The master branch (i.e. `upstream master`) should be deployable at all times.
This means that if code is in the master branch, we should be confident that
the feature has been tested, that it will work as intended, and that the app
won't crash.
To keep the master branch clean and functional, don't push directly to master;
use branching and pull requests instead.

### Developing features using branches
Branching allows you to make changes to the code without affecting the master
branch. When you want to make a new branch, follow these steps:
1. Make sure your local `master` matches the upstream `master` (the parent
   in the GitHub organization).
   ```bash
   > git checkout master
   > git pull upstream master
   ```

2. Now that your master branch is up to date, you can start on your feature.
   Create a local branch with a descriptive name (for example, if you're
   implementing searching for partners by schedule, `search-by-schedule` might
   be a good name).
   ```bash
   > git checkout -b search-by-schedule
   ```
   You'll also need to create the branch remotely so that you can push to your
   fork:
   ```bash
   > git push --set-upstream origin search-by-schedule
   ```

3. Commit your work as you go, using concise, descriptive, and informative
   commit messages.
   ```bash
   # bad
   > git commit -m "fixed bug"
   # good
   > git commit -m "fixed null pointer exception in func()"
   ```

### Merging into master
When your feature is ready to be merged into the master branch, follow these
steps.

1. Since other features may have been merged into the master branch since you
   started working on your feature, it's a good idea to check for merge
   conflicts that may have arisen:
   ```bash
   > git checkout your-feature-branch
   > git pull upstream master
   ```

2. Once you've cleaned up the conflicts and committed your changes, push the
   branch to your fork.

3. Now that your fork has the up-to-date, conflict-free version of your feature,
   you can create a pull request.
   Note that on the pull request page, you can specify the following criteria:
   - **base fork**: the group repository
   - **base**: the branch you're requesting to pull your work into (probably
     master)
   - **head fork**: your fork
   - **compare**: the branch of your fork where your changes are (i.e.
     `your-feature-branch`
   ![example](https://help.github.com/assets/images/help/pull_requests/choose-head-fork-compare-branch.png)

4. Wait for feedback from others. If everyone agrees that your code looks
   correct, merge it into the master branch. Otherwise, make changes to address
   the team's concerns until ready for merging.

