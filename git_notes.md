# Class 3

`Ctrl+a`

goes to the beggining of the line

'`Ctrl+e`

goes to to end of the line

`Ctrl+d`

"dones" the process

In loops, naming the variable as "i"

`$i`

this calls the variable in the list

`${i}`

this calls the name of the variable

`!`

To reuse command, or use the number shown in history; ex:

`!308`

`2>`

this redirects the error messages

`&> `

redirects both stout and error

`Crtl+z`

puts a process to sleep

`fg`

resumes the process in the foreground

`bg`

resume in the background

`ps`

show the processes running

Adding "&" send the command to the background automatically

how to grep lines only with spaces:

`grep -v '\w'`

because the -v gets "everything but", and the \w means any alphanumeric character



# 24-Set
Using git  

`git diff`

shows the differences between the file in the staging area and in the last version

`git init`

initiates a repository in the current folder

`git -a`

: does both add and commit in the same step  

`ps`

shows the git processes running
to kill a process, do:

`kill -9 [#of the process]`

# 26-Set
When you create a new git repository in your computer, you need to link it to an origin repository in github. You then crate online a new repository in github.    
This will check the name of the central, if it exists.

`git remote -v `

This adds an origin repository

`git remote add git@github.com:your_user_name/your_repo_name.git`

This pushes your new repository to the origin you crested on github

`git push origin master`

If you are cloning, you don't need to git init a repository. Just make sure you are cloning into a folder that is not a git repository. The directory where you are cloning will not become a repository, but rather the cloned directory will become a git repository inside it.  

`git clone git@github.com:xxxxxxxxxxxx`

When two people linked to the same repository edit the same part of a file, git creates a branch. If you are editing and commit your file, then pulls the different file from the origin, git will show the conflict. You then have to manually solve the conflit, merge, then comit and push the merged file. THis will resolve the branch.

# 30-Set

Very useful thing for scripts: using **$1** as a variable will run the script with the first file you call in the command line.  You can also keep going and use $2, $3, etc...
If you don't want to define the number of varibles, you can use **$@**.

Other very useful thing is using the flag -x when running a bash. This shows each command that is being run and helps you debug your scripts.
also, remember to place variables in quots in case they have space in their names!!


