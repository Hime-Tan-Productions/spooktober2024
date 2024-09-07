# Developer Workspace Setup

## First Time Setup

### Download the Project from GitHub

#### Install a Git Glient
There are many options! Mac comes with `git` installed and usable in terminal, but you probably want a GUI like [GitHub Desktop](https://desktop.github.com/download/), [Fork](https://git-fork.com/), or whatever else you prefer!

The following instructions refer to various git commands like `fetch`, `pull`, `commit`, etc. Refer to your client's documentation for how to do each of those things in your client.

#### Set Up Authentication
Your git client will have documentation on how to set up authentication. Some will allow you to authenticate with github.com through the click of the button, while others will make you set up an SSH key. Reach out to TJ if you need help!

#### Clone the Repo
Your git client will have documentation on how to clone a repository. The repo URL is https://github.com/Hime-Tan-Productions/spooktober2024 . Clone it wherever you want, but preferably to a folder like `C:/git/` or `~/git/`.

### Download Ren'Py
Our project uses Ren'Py version [8.3.1](https://www.renpy.org/release/8.3.1), which is a preview version. Make sure you don't download 8.3.0 - it has a bug that makes the web build unplayable.

### Open the Project in Ren'Py
Open `renpy.exe` on Windows or `renpy.app` on Mac. Select `preferences`. Set Projects Directory to the parent folder of the checked out project. For instance, `C:/git/` or `~/git/`.

When you refresh or relaunch Ren'Py, you should see "spooktober2024" listed among the Projects. Highlight it, then select `Launch Project` to play it locally!

## Feature Development
If you have a new image to upload, want to make changes to dialog, or anything else except a bugfix, follow these instructions.

First, make sure you have the latest code. Open your git client. `commit` or `stash` any ongoing work to your current branch, then swap your branch to `main`, which is the default branch that all changes get committed to. `fetch` and `pull` to get the latest changes. Then `create a new branch` called `feature/<feature-description>`, like `feature/corpse-flower-images`.

Make your changes, then test them in the Ren'Py launcher.

After you're happy with your changes, commit your changes to your bugfix branch, then [open a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) on github.com. Once it's been approved and merged, your branch will be automatically deleted!

## Fixing a Bug
Follow the instructions under Feature Development, but name your branch `bugfix/<issue-number>-<description>`, like `bugfix/issue-5-crash-on-launch`.
Make sure you can reproduce the issue locally before you make any changes!
