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

# 07-Oct
sed uses
use of parenthesis to capture things in sed

# 08-Oct

How to go back in git
First check the branches:
`git log --graph`

`git checkout <codeOfTheVersion> --,name_of_file`

git branch -a to see all brnches

The workflow to branches is: Make a new branch, work there; then commit your changes; When you want to merge, go back to master, do the merge, and pull; the same if working with more people; 

# 10-Oct
awk:
***I have to go back to this***

# 17-Oct

## Python
Assigning variables in python is easy: just use =
When you assign a variable based on another, when you change the first one, the value in the second one is not updates.

Indexing in python starts with 0. For ex, for indexing the first line in first column you do [0,0]
To give a range, use :; [0:4, 9:20]

To run an operation across all lines from an array, use "axis 0"
`print(numpy.mean(data, axis=0))`

To run an operation across all columns from an array, use "axis 1"
`print(numpy.mean(data, axis=1))`

To plot a graph, you first need to save the output in a variable, then type the show function:
Ex:
`ave_inflammation = numpy.mean(data, axis=0)
ave_plot = matplotlib.pyplot.plot(ave_inflammation)
matplotlib.pyplot.show()`

To add subplots, use function add_subplot:

`axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)`

The first number is the number of lines, the second the total number of columns, and the last one is the position in the plot.

To make arrays:
`A = numpy.array([[1,2,3], [4,5,6], [7, 8, 9]])`
To stack arrays horizontally:
`B = numpy.hstack([A, A])`
To stack arrays vertically:
`C = numpy.vstack([A, A])`

**issue with range: why does not work outside loops?**
**study again the section about polinomial and enumerate http://swcarpentry.github.io/python-novice-inflammation/02-loop/**

Lists are different from numpy arrays. To define one, use brackets and commas. Ex:
`odds = [1, 3, 5, 7]`

A difference to arrays is that you can edit individual values in the list.

When you simply want to copy a variable, use:
`new_variable = lists(old_variable)`

If just using = the variables will change values if you modify one.
## Oct-24
What is pop() doing??

Regular expressions:

when defining a variable in a def function, the variable is only created in this session. However, in a for loop the variable created in mantained.

## Oct-26  
### **From Analyzing Data from Multiple Files**
The most important part is using the package "glob" and the function "glob", that is used for importing a list of file names. It finds a pattern; ex:

```
filenames = glob.glob('inflammation*.csv')
```  

I did not understand the last exercise in this section: Generate Composite Statistics  
I'm not sure what the =+ is doing to the composite_file; it looks like it is overwriting it with every new file that is called in the loop.  
Hm, I think then all new data is being summed to each line/row, as composite_file was created with the same (60,40) dimmension of each file.  

From Making Choices:

the line of code after an if/else statement does not work, why?!
I tried adding a space

>EXERCISE: In Place Operators:

```py
list=[-1, -2, 0, 1, 2]
positive_sum=0
negative_sum=0
for n in list:
    if n > 0:
        positive_sum+=n
    elif n < 0:
        negative_sum+=n
print(positive_sum)
print(negative_sum)
```

>EXERCISE: Sorting a List Into Buckets  

```py
files = ['inflammation-01.csv', 'myscript.py', 'inflammation-02.csv', 'small-01.csv', 'small-02.csv']
large_files = []
small_files = []
other_files = []

for file_name in files:
    if file_name.startswith("inflammation-"):
        large_files.append(file_name)
    elif file_name.startswith("small"):
        small_files.append(file_name)
    else:
        other_files.append(file_name)
```

>EXERCISE: Counting Vowels  

I cound not solve it at first, but I learned something good: if x **in** y.  
This is a good way of checking if something matches something. I was failling because I was using **==**; Maybe there is a was with **==** by using some sort or OR 

## Oct 28
### **From Writing Functions**

>EXERCISE: Combining Strings  

```py
def fence(original, wrapper):
    return print(wrapper+original+wrapper)
```

>EXERCISE: Selecting Characters From Strings

```py
def outer(string):
    return string[0]+string[-1]
```

>EXERCISE: Rescaling an Array

```py
def rescale(input_array):
    '''converts the input array into values between 0 and 1
    Examples:
    >rescale(numpy.linspace(1,10,9))
    array([0.   , 0.125, 0.25 , 0.375, 0.5  , 0.625, 0.75 , 0.875, 1.   ])
    '''
    import numpy
    min=numpy.min(input_array)
    max=numpy.max(input_array)
    return (input_array-min)/(max-min)
```

### **From Errors and Exceptions**  

** not sure if I understand the function ***float*** and ***tuples*** **

I don't understand how these assetions that use specific numbers for spotting errors will detect general errors in the functions, such as absence of overlap in other values.

>EXERCISE: Pre- and Post-Conditions
 I got stuck here because I did not understand the input format for these min/max values....

```py
def range_overlap(ranges):
    '''Return common overlap among a set of [low, high] ranges.'''
    lowest = numpy.min(ranges)
    highest = numpy.max(ranges)
    for (low, high) in ranges:
        lowest = numpy.max(lowest, low)
        highest = numpy.min(highest, high)
    return (lowest, highest)

    set=[-1,10],[2,8],[9,12]
```
## Oct-29
```
def logfactorial(n):
    '''Function to calculate the log of n!, by summing the log(1)...log(n).
    output=0
    Examples:
    >>>logfactorial(3)
    1.791759469228055
    '''
    assert n>0, 'Data should only contain positive values'
    assert n==int, 'Data should only contain integers'
    for i in range(1,n+1):
        output = output + math.log(i)
    return output
```

## Oct 30

### **From Debugging**  


patients = [[70, 1.8], [80, 1.9], [150, 1.7]]

def calculate_bmi(weight, height):
    return weight / (height ** 2)

for patient in patients:
    weight, height = patient
    bmi = calculate_bmi(weight, height)
    print("Patient's BMI is: %f" % bmi)


whats is this? : if __name__ == '__main__':
on readings_05.py, I still don't get how this assertion and the for loop are escaping the proble of if the user uses no flag and the indexing of sys.argv and how can I have "process"in this for loop if it is not yet defined in a function?

>EXERCISE: Arithmetic on the Command Line

import sys
import numpy


```py
def main():
    script = sys.argv[0]
    action = sys.argv[1]
    numbers = sys.argv[2:]
    assert numbers in [int,float], 'input is not a number'

    if action == 'add':
        result = numpy.sum(numbers)
    elif action ='subtract'
        result = numpy.subtract(numbers)
if __name__ == '__main__':
   main()

```