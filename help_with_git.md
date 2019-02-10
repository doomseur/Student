# Lab 1: Introduction to Git and GitHub

In this lab we will learn how to setup and use the open-source version control software Git and the online repository storage from Github.

Git is basically used by developers to keep track of their code changes, different versions, and updates and changes from other developers who might also be working on the same project, while GitHub is basically just an online server where we can store our projects and allow easy access to other developers who might be working on the same project.
___

## Lab Contents

1. Create a GitHub account.
2. Installing Git.
3. Configuring Git.
4. Cloning a repository.
5. Initialising / creating a new repository.
    + Creating a new repository on GitHub.
    + Installing hub.
6. Some examples
7. Fine tuning our workflow.
8. More information.
9. Lab Summary / Cheat-Sheet.

___

### Create a GitHub account

Start by creating a free GitHub account for ourselves.
> Hint: We don't actually need GitHub to use Git, we could just store our files and projects on our own servers, but GitHub handles all this for us and allows users world wide to contribute to out project.

So go to the GitHub home page and sign-up for a [new account today](https://github.com).
> Hint: Your GitHub account can often act as a portfolio for potential employers so choose a username that isn't embarrassing on a CV etc.

> Hint: You might want to check out and sign-up for the free [Student developer Pack](https://education.github.com/pack). If you just sign-up as normal for a free account it will ask you to confirm if you are a student during the sign-up process.

### Installing Git

Git is not installed by default on our Ubuntu VM so we need to install it. So while connected to the Internet run the following command in your terminal to install Git on your system.

```bash
sudo apt-get install git
```

We can verify we have Git successfully installed by using the version option.

```bash
$ git --version
git version 2.17.1
```

### Configuring Git

Once our installation has successfully completed, the next thing to do is to set up the configuration details for our GitHub account. To do this we need to set some values in our config file, using the commands shown below.
> Hint: Replace "user_name" and "email_id" with your own GitHub username and email.

```bash
git config --global user.name "user_name"
git config --global user.email "email_id"
```

### Cloning a repository

Now that we've created a GitHub account, installed and configured Git, we can start to actually use Git. With Git we can clone (or copy) existing repositories onto our system so we can use or edit the code locally. Lets try this now by cloning a copy of the securecomms repository from my public GitHub repository. This public project / repository will contain all of the module lab notes and resources for the term, so you'll need to check back regularly to get the latest updates.

So to download a project and it's entire version history:

```bash
mkdir College
cd College
git clone https://github.com/MarkCumminsIRL/securecomms.git
```

>Hint: The previous command will create a securecomms folder inside the College folder. Feel free to create whatever directory structure to prefer personally.

If you ever want to update this repository, to make sure you have the latest version of the notes for example. you just need to change into the project folder and run the pull command to pull down all the latest updates.

```bash
cd securecomms
git pull
```

### Initialising / creating a new repository

Downloading existing repos is great for getting the source code of tools etc. but eventually you will want to create and upload your own projects (or repos). The following section will step you through the steps required to create and update your own projects.

The first thing you are going to want to do is create a folder on your system. This will serve as a local repository which will later be pushed onto the GitHub website. We can do this using the following commands:

```bash
$ git init MyFirstProject
Initialized empty Git repository in /home/al/MyFirstProject/.git/
```

>Hint: This output line may vary depending on your system.

So here, MyFirstProject is the folder that is created and "init" makes the folder a GitHub repository. Now change into your new project folder and create a README file and enter some text like "this is my first git project". The README file is generally used to describe what the repository contains or what the project is all about. 

```bash
cd MyFirstProject
echo "This is my first git project" >> README
```

Once we have finished our work in a particular project we want to upload or commit all the changes so that the version saved on GitHub is the same as our local version. To do this we normally want to add any files we've updated to a list of files for Git to commit to the online master copy. We can add files to the list one by one by using the command:

```bash
git add Filename1
git add Filename2
etc.
```

Or we can simply add all files to the list that we need to commit using:

```bash
git add --all
```

It also best practice to add a message with each update, just a short message that highlights what changed in this update. 'Fixed bug in login' or similar. Again we can do this using the command:

```bash
git commit -m "updated readme.md"
```

So once we have updated our list for all files that have changed or have been created, the last step is for us to actually upload those files to GitHub so that everything is up to date and in sync. We do this using the following commands.

> Hint: Change the URL in the following command to match your own account

```bash
git remote add origin https://github.com/doomseur/MyFirstProject
git push -u origin master
```

> Hint: This won't work.. check out the next sections for solutions.

#### Creating a new repository on GitHub

The previous commands will actually cause us an error. Why? Well GitHub doesn't actually allow you to create a new repo on GitHub from the command line. What we need to do is log-in to GitHub and create the new repo there before we try to upload to it. The name must also match our folder name exactly.

So log-in to GitHub and create a new repository called 'MyFirstProject' then try upload our project files again.

> Hint: Do not initialize the repository with a README, .gitignore or License. Keep it blank

```bash
git remote add origin https://github.com/doomseur/MyFirstProject
git push -u origin master
```

> Hint: Once you have set the origin for a repo you can simply use the git push, or git pull commands to upload and download repos.

#### Installing hub

Having to log-into GitHub every time we want to create a new project can be a bit of a pain. There is however a solution that will allow us work completely on the command line and not have to go into GitHub to create every new repo. We will use the [Git Wrapper 'hub'](https://hub.github.com/) to extend the Git commands available to us by adding some GitHub functions. We will need to install the hub update using the following:


```bash
sudo snap install hub
git config --global hub.protocol https
```

Once installed we now have some extra command line GitHub functionality. So to create a new repo from the command line and eliminate the need to manually do so in GitHub we simply change into the our new project folder and run the following:

```bash
hub create
```

> Hint: We still need to perform all the other steps described earlier.

### Some examples

OK, We covered a lot of detail very quickly so lets recap by doing some exercises. In this section we will complete three short exercises, and hopefully by the end of them you will have a much better understanding of working with Git and GitHub.

#### Exercise 1

Create a new repository called 'Lab_1', add a README and a test.txt file and upload it to your GitHub account. So change out of our early repositories and lets create a new one.

```bash
git init Lab_1
cd Lab_1
echo "some stuff" > README
echo "a test file" > test.txt
git add --all
git commit -m "Initial commit: README and test.txt file"
hub create
git push -u origin master
```

#### Exercise 2

Log into your GitHub account, and confirm that the new repo has been created and that the two files have been uploaded. Edit one of the files on GitHub and also create a third file called test2.txt. Once done, update your local repository with any updates from GitHub.

```bash
git pull
```

#### Exercise 3

Finally Lets update and change some of the files locally and then push back up to the GitHub Server one last time.

```bash
git add --all
git commit -m "some updates"
git push
```

### Fine tuning our workflow

Using Git can seem very confusing and long winded at first but once you use it regularly it will become second nature to you. You should try to develop a workflow that allows you to check-out the latest version of a project, do your updates and then push the updated files back online once you are finished.

Below I've given a few small hints and tips that might help make your transition to Git and GitHub a bit easier.

#### Caching your GitHub password with Git
If you're cloning GitHub repositories using HTTPS, you can use a credential helper to tell Git to remember your GitHub username and password every time it talks to GitHub. This saves you having to enter your username and password every time you interact with a repository.

Turn on the credential helper so that Git will save your password in memory for some time. By default, Git will cache your password for 15 minutes.

In Terminal, enter the following:

```bash
git config --global credential.helper cache
```

To change the default password cache timeout, enter the following:

```bash
git config --global credential.helper 'cache --timeout=3600'
# Set the cache to timeout after 1 hour (setting is in seconds)
```

#### Switching remote URL's from SSH to HTTPS

You may sometimes need to switch the remote URL for a project. List your existing remotes in order to get the name of the remote you want to change.

```bash
$ git remote -v
origin  git@github.com:USERNAME/REPOSITORY.git (fetch)
origin  git@github.com:USERNAME/REPOSITORY.git (push)
```

Change your remote's URL from SSH to HTTPS with the git remote set-url command.

```bash
git remote set-url origin https://github.com/USERNAME/REPOSITORY.git
```

### More information on using and getting started with GitHub

There is plenty more that you can do with Git and GitHub, especially when it comes to teams of people editing the same code, this is where version control really becomes useful. For now we can use it for syncing our project folders as a form of backups for our files. To find out more of the features of Git and GitHub check out the following [resources for learning Git](https://try.github.io/)

### Lab Summary / Cheat-Sheet

