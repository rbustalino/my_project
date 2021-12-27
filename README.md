This are the steps on how to install or the requirements needed of the app this must be created using the github file creation facility


## Create Remote Repository on GitHub.com

If you don't already have an account go ahead to github.com, signup, and create a repository, this is where our files will be added. 
You can create your repository by going to “repositories” and by clicking “new”



## Download Git

1. Download Installer - Got to https://git-scm.com/ and select the downloader for your machine, I will be using windows
2. Install git - Once the installer is downloaded go ahead and follow the steps to get things set up, I tend to just leave the default settings so if you don't have a preference just let it guide you.
3. Check Git version - Once things are installed do a quick search on your computer for git bash and open it. To check the version of git you have installed go ahead and type “git --version”
  
## Create Local Repository

1. git init -  Initialize local a new repository
2. git status - shows what you have in you staging area
3. git add . - adds files and folders to the staging area
4. git commit -m “Custom message” - commits files in staging area to local repository
5. git remote <remote url> - Takes a local repository and pushes to a remote repository (Github)
   * Create a repo on github
   * set a remote 
   * Add your github credentials
6. git push -u origin <branch name>
