Class 3

Ctrl+a goes to the beggining of the line
Ctrl+e goes to to end of the line
Ctrl+d "dones" the process

In loops
$i ->this calls the variable inn the list
${i}
-> this calls the name of the variable
! to reuse command, or use the number shown in history; ex: !308

2>  ##this redirects the error messages
&>   ###redirects both stout and error

Crtl+z puts a process to sleep
fg resumes the process in the foreground
bg resume in the background

ps show the processes running

Adding "&" send the command to the background automaticlly

how to grep lines only with spaces:
##
grep -v '\w'

because the -v gets "everything but", and the \w means any alphanumeric character


####
24-Set
# Using git  
git diff : shows the differences between the file in the staging area and in the last version  

git init: initiates a repository in the current folder.
git -a: does both add and commit in the same step

ps:  shows the git processes running
to kill a process, do :
`kill -9 [#of the process]`
