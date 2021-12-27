## This are the steps on how to install or the requirements needed of the app using the github file creation facility


### Create Remote Repository on GitHub.com

If you don't already have an account go ahead to github.com, signup, and create a repository, this is where our files will be added. 
You can create your repository by going to “repositories” and by clicking “new”



### Download Git

1. Download Installer - Got to https://git-scm.com/ and select the downloader for your machine, I will be using windows
2. Install git - Once the installer is downloaded go ahead and follow the steps to get things set up, I tend to just leave the default settings so if you don't have a preference just let it guide you.
3. Check Git version - Once things are installed do a quick search on your computer for git bash and open it. To check the version of git you have installed go ahead and type “git --version”

You can also do this from your command prompt, in fact I will be using the command prompt from now on so go ahead and close git bash and open up a new terminal.If you already had your terminal open you may need to close and reopen to get the updates.

* git init - Initialize local a new repository
* git status -shows what you have in you staging area
* git add <file> -  adds files and folders to the staging area
* git commit - commits files in staging area to local repository
* git push - Takes a local repository and pushes to a remote repository (Github).
    - Create a repo on github
    - set a remote 
    - Add your github credentials
* git pull - Pull latest changes from remote repository
* git clone - Clone repo from github
  
### Create Local Repository

1.  Initialize new git repo | git init
    
  Now that you have git installed, cd into your project folder and initialize a local repo. 

  *cd projectname

  *git init

When you run git init a new folder will be added to your project files, these files visibility are set to “hidden” by default so you will not see them but rest assured they are there. If you want to see these files open up your folder and select “view”
 

2. Check your staging area | git status
  This step is not necessary before we add our files but for the sake of seeing the difference and showing exactly what happens lets run “git status”
  
3. Add files | git add .
  To add a particular file or folder to your staging area you can run “git add <filename>”. In our case we want to add all the files highlighted in red so lets run “git add .”.   In case you can't see it there is a period after “add” indicating we want ALL the files.

  After running git status I typically like to run git status again to ensure all changes we made.
  
4. Commit Changes  | git commit -m “Your custom note”
  Now that we added files to our staging area we need to commit them to our local repository. 

  * git commit -m “first commit”.
 
5. Set remote |  git remote add origin <repo url>
  Now that all the files are set locally we are ready to push them to our remote repository. We set the remote so when we run “git push”, git knows which remote repo to send       these files to.

  Ex: git remote add origin https://github.com/rbustalino/my_project.git
  
6.  Push to remote | git push -u origin <branch name>
  Now that we have our remote set, we can push our local github repo live. The default branch on github is called “master” unless you set your own. When you first create a         repository on github you will see steps to rename this branch to “main”, if you decided to rename the default branch then use that name instead of master.

  * git push -u origin master
  
  Now if you refresh your repository on github.com you should see all your local files here.


  
