### Question: 1

Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
Use a sorting method



### Question: 2

Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
Use list and append



### Question: 3

Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
Use list and .join


### Question: 4

Write a password generator in Python.
Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.


Hint:
use Python’s random module,

```
This is your first exposure to using Python code that somebody else wrote.
In Python, these formally-distributed code packages are called modules.
The thing we want from a module in this exercise is the ability to generate random numbers.
This comes from the random module.

To use a module, at the top of your file, type
```

```python
    import random
```
```
This means you are allowing your Python program to use a module called random in 
the rest of your code.

To use it (and generate a random integer), now type:
```
```python

    a = random.randint(2, 6)
```
Once you run this program, the variable a will have a random integer that the computer made for you, between 2 and 6 (including 2 and 6).
![Python Docs - Random module](https://docs.python.org/3.3/library/random.html)

Bonus:
Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

Happy coding!


### Question 5

This is a feature phone keypad:
```

------- ------- -------
|     | | ABC | | DEF |
|  1  | |  2  | |  3  |
------- ------- -------
------- ------- -------
| GHI | | JKL | | MNO |
|  4  | |  5  | |  6  |
------- ------- -------
------- ------- -------
|PQRS | | TUV | | WXYZ|
|  7  | |  8  | |  9  |
------- ------- -------
------- ------- -------
|     | |     | |     |
|  *  | |  0  | |  #  |
------- ------- -------

```
Before predictive text entry systems like T9, you had to press a button
repeatedly to cycle through the possible values until you reached
the one you wanted.

For example, to type "V8" you would press the 8 key three times and then
again four times (pressing the 8 key cycles through T->U->V->8),
giving us a total of seven key presses.

Note: the 0 key handles spaces and outputs 0 when tapped twice.

Write a function that can calculate the amount of button presses required for any phrase.
Except for spaces, punctuation can be ignored.
Your function should accept both uppercase and lowercase letters and treat them the same.

Examples:
presses('V8') # 7
presses('LOL') # 9
presses('How R u 2day') # 23

Bonus:  Try to avoid hard-coding the number of button presses for each letter!

Resource:Use python [Dictionaries](http://www.learnpython.org/en/Dictionaries) in this exercise


### Question 6
##### List Comprehension

Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

The idea of a list comprehension is to make code more compact to accomplish tasks involving lists.
Take for example this code:

```python

  years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
  ages = []
  for year in years_of_birth: 
    ages.append(2014 - year)
```

And at the end, the variable ages has the list [24, 23, 24, 24, 22, 23].
What this code did was translate the years of birth into ages, and it took us a for loop and an append statement to a new list to do that.

Compare to this piece of code:

```python

  years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
  ages = [2014 - year for year in years_of_birth]

```

The second line here - the line with ages is a list comprehension.

It accomplishes the same thing as the first code sample - at the end,
the ages variable has a list containing [24, 23, 24, 24, 22, 23],
the ages corresponding to all the birthdates.

The idea of the list comprehension is to condense the for loop and the list appending into one simple line. Notice that the for loop just shifted to the end of the list comprehension, and the part before the for keyword is the thing to append to the end of the new list.

Happy coding! :)


### Question 6
#### List Overlap

Take two lists, say for example these two:
```python

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

```

And write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.

Bonus:

    Randomly generate two lists to test this
    Write this in one line of Python

List properties (In other words, “things you can do with lists.”)

One of the interesting things you can do with lists in Python is figure out whether something is inside the list or not. For example:

```python

  >>> a = [5, 10, 15, 20]
  >>> 10 in a
  True
  >>> 3 in a
  False

```

You can of course use this in loops, conditionals, and any other programming constructs.

```python

  list_of_students = ["Michele", "Sara", "Cassie"]

  name = input("Type name to check: ")
  if name in list_of_students:
    print("This student is enrolled.")

```
Happy coding! :)