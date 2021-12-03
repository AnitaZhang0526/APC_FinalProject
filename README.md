# APC_FinalProject
XRD/FTIR data processing tool suite. Created by Alex Pirola, Agnes Robang, Shashank Gupta, Arjun Prihar, Jordan Hamel, and Anita Zhang.

#### Git Workflow
This section of the ReadMe outlines the git workflow that each team member will follow in order to collaboratively work on our project files. The goal is for all of us to be able to refer back to this document to responsibly upload our changes to source files, minimizing version control errors. To summarize, each feature of the project will be worked on in a seaparate branch by a single team member. With the approval of two other teammates, these features will be merged into a development branch and ultimately into the master branch:

1. Use �git clone� command to get the collaborative repository locally on your machine
2. Use �git checkout main� to make sure you�re on the main branch
3. Use �git checkout -b your_name-name_of_feature� to create AND checkout a new branch
     * You should see the command-line prompt �Switched to a new branch�
     * You can use the command: �git log --all --decorate --oneline --graph� to display the entire DAG and see where you are
     * You can see just the branch you�re on with the command: �git branch --show-current� to confirm you�re in the right place
4. Do your business on your branch. Right now this is only on your local machine, so do what you want. You won�t mess anything up for anyone else and no one can judge you for any dum dum things you want to test out� not that anyone would anyway ;)
5. When you are ready to send your work upstream�
     * Stage your files with �git add your_filename�
     * Commit with �git commit -m �your commit log� �
     * Do your best to make your commit log legible to more than just you :)
     * Finally push your files with �git push origin your_name-name_of_feature (i.e. the name of the branch you created for your work)�
6. Your push will NOT automatically create a pull request - you do this manually on GitHub. If you go to the github repository in your browser, you will see this under the �Pull request� tab (between �Issues� and �Actions�)
     * If you click on the pull request, you should be able to see the commit history, changelogs of all the files you pushed, and a text box that allows you to leave a comment. 
     * On the right side of the webpage, you will see �Assignees� (between �Reviewers� and �Labels�). Assign at least 2 other people to the pull request. These teammates will be responsible for reviewing your code and ultimately merging the changes into �develop�. Try to make fairly regular pushes, so that the code review for your teammates is more manageable. They will ultimately decide if it is okay to be merged into the development branch. There should be no reason for command-line level merges
     * Once you�ve completed Step 5b, click the green button �Create Pull Request.� NOTE: make sure the pull request correctly indicates that you want to merge into 'develop' - there is a drop-down menu in the upper left. 
7. After your pull request is approved, you can make another pull request (directly in GitHub) to merge your work into 'main.' 
8. When you want to update the files on your local machine, for example, to retrieve the work someone else has pushed to the repository, in your command prompt:
     * make sure you first switch to main with �git checkout main�
     * Type �git pull origin main�
 
