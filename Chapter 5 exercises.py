'''
Chapter 5 Exercises

Exercise 1

Asdiscussed in the cahpter, string formatting could be used to simplify the
dateconvert2.py program. Go back and redo this program making use
of the string-formatting method.

Original program:

#--------------------------------------------------------------------------
def dateconvert2():

    # get the day, month, and year

    day, month, year = eval(input("Enter day, month, year >>> "))

    date1 = str(month)+"/"+str(day)+"/"+str(year)

    #months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']
    months = ['January','February','March','April','May',
               'June', 'July', 'August', 'September', 'October', 'November', 'December']


    monthStr = months[month-1]
    date2 = monthStr + " " + str(day) + ", " + str(year)

    print(date1)
    print(date2)
    print("First date: {0}/{1}/{2}".format(day, month, year))
    print("Second date: {0} {1}, {2}".format(monthStr, day, year))

#--------------------------------------------------------------------------
'''

def date():

    # get the day, month, and year

    day, month, year = eval(input("Enter day, month, year >>> "))

    months = ['January','February','March','April','May','June', 'July', 'August', 'September',
              'October', 'November', 'December']

    monthStr = months[month-1]
    
    print("First date: {0}/{1}/{2}".format(month, day, year))
    print("Second date: {0} {1}, {2}".format(monthStr, day, year))

'''
Exercise 2

A certain CS professor gives 5-point quizzes that are graded on the
scale 5-A, 4-B, 3-C, 2-D, 1-F. Write a program that accepts a quiz score
as an input and prints out the corresponding grade.
'''

def qs():

    score = int(input("Enter quiz score >>> "))
    # Store all scores in list in ascending order
    possible_scores = ['1-F', '2-D', '3-C', '4-B', '5-A']
    grade = possible_scores[score-1][2] # Use double index to identify grade
    print("Quiz grade: ", grade)

'''
Exercise 3

A certain CS professor gives 100-point exams that are graded on the
scale 90-100:A, 80-89:B, 70-79:C, 60-69:D, <60:F. Write a program that
accepts an exam score as input and prints out the corresponding grade
'''

def quiz():

	score = int(input("Enter quiz score >>> "))

    # 11 copies of 'A' to include the score 100
    # 'F' included as last item in string to accomodate score of 0

    # This was the only non-decision statement method of
    # attacking this problem that I could think of
    string = 'F'*59 + 'D'*10 + 'C'*10 + 'B'*10 + 'A'*11 + 'F'

    grade = string[score-1]

    print(grade)

'''
Exercise 4

An acronym is a word formed by taking the first letters of the words in
phrase and making a word from the. For example, RAM is an acronym for
"random access memory." Write a program that allows the user to type in a
phrase and then outputs the acronym for that phrase. Note: the acronym
should be all uppercase, even if the words in the phrase are not
capitalized.

'''


def e4():

    word = input("Enter phrase >>> ")
    wordStr = word.split() # Split phrase into separate strings

    acronym = ''

    # Loops through words in the phrase, adds the first letter to
    # each string to the acronym variable, and then capitalizes it
    for i in wordStr:
        acronym = acronym + i[0].capitalize() 

    print(acronym)

'''
Exercise 5

Numerologists claim to be able to determine a person's character traits
based on the "numeric value" of a name. The value of a name is
determined by summing up the values of the letters of the name where "a" is
1, "b" is 2, "c" is 3, etc., up to "z" being 26. For example, the name
"Zelle" would have the value 26 + 5 + 12 + 12 + 5 = 60 (which happens
to be a a very auspicious number, by the way).

Write a program that calculates the numeric values of all the names.
'''

def name_calc():

    # Set entire alphabet as string
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # Capitalize all characters because I didn't want
    # to type the alphabet out again lol
    alphabet = alphabet.upper()
    enter_name = input('Enter name >>> ') 
    new_variable = 'test'

    # This is the answer to exercise 6. Just had to employ an additional
    # strong method to remove any spaces between names

    name = enter_name.replace(' ', '')
    name = name.upper()
    

    # Standard accumulator pattern
    name_value = 0
    for i in name:
        # Add to name_value the index position of each letter in the name
        # Also, add 1 each time as well, since a is equal to index 0, and the
        # exercise requires that a be equal to 1
        name_value = name_value + alphabet.index(i)+1
        
    return name_value

'''
Exercise 6

Expand your solution to the previous problem to allow the calculation
of a complete name shc as "John Marvin Zelle" or "John Jacob Jingleheimer
Smith". The total value is just the sub of the numeric values of all the names.
'''

# See comments in exercise 5 for the answer

'''
Exercise 7

A Caesar cipher is a simple substitution cipher based on the idea of shifting
each letter of the plaintext message a fixed number (called the key) of positions
in the alphabet. For example, if the key value is 2, the word "Sourpuss" would be
encoded as "Uqwtrwuu". The original message can be recovered by " reenconding" it
using the negative of the key.

Write a program that can encode and decode Caesar ciphers. The input to
the program will be a string of plaintext and the value of the key. The out-
put will be an encoded message where each character in the original message
is replaced by shifting it KEY characters in the Unicode character set.
For example, if ch is a character in the string and key is the amount to shift,
then the character that replaces ch can be calculated as: chr(ord(ch)) + key.
'''

# I'm going to skip writing out problem 8, because it addresses the obvious
# issue with the problem listed above, in that what happens when the shift
# moves past 'z'. The below output indicates how to constantly iterate over
# the alphabet string loop, so that if the shift is 1 and the letter is 'z',
# then the encoded version should be 'a'.

def ceasar_cipher():

    word = input('Enter word >>> ' )
    key = int(input('Enter key >>> ' ))
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
  
    code_word = ''

    for i in word:
        
        # Conditional logic maintains integrity of spaces
        if i != ' ':

            # Using remainder division to have loop move over
            # entire string
            shift = alphabet[(alphabet.index(i) + key) % 26]
            code_word = code_word + shift
        else:
            code_word = code_word + ' '

    return code_word

'''
Exercise 9

Write a program that couts the number of words in a sentence entered
by the user.
'''

def word_count():

    sentence = input('Enter sentence >>> ')

    # Split method divides string into list of string based on where
    # spaces are, and then counts length of list.
    return len(sentence.split())

'''
Exercise 10

Write a program that calculates the average word length in a sentence
entered by the user.
'''

def avg_word_length():

    sentence = input('Enter sentence >>> ')

    # See logic in exercise 9
    word_list = sentence.split()

    # Standard accumulator pattern
    total = 0
    for i in word_list:
        total = total + len(i) 
                
    return total / len(word_list)

'''
Exercise 11

Write an improved version of the Chaos program from Chapter 1 that allows
a user to input two initial values and the number of iterations and
then prints a nicely formatted table showing how the values change over
time. For example, if the starting values were .25 and .26 with 10
iterations, the table might look like this (didn't feel like typing it
out lol)
'''
# chaos.py

##def main():
##
##    print("This program illustrates a cahotic function")
##    x = eval(input("Enter a number between 0 and 1: "))
##    for i in range(10):
##        x = 3.9 * x * (1 - x)
##        print(x)
##
##main()

def chaos():

    # print("This program illustrates a cahotic function")
    x = eval(input("Enter a number between 0 and 100: ")) / 100
    y = eval(input("Enter a second number between 0 and 100: ")) / 100
    k = int(input("Enter number of iterations >>> "))
    
    print('\nIndex', '     ', x, '         ', y)
    print('--------------------------------------\n')

    for i in range(k):

        x = 3.9 * x * (1 - x)
        
        y = 3.9 * y * (1 - y)   

        print("{0:2}".format(i+1), '     ', "{0:6f}".format(x),
              '     ', "{0:6f}".format(y))

'''
Exercise 12

Write an improved version of the future value program from Chapter 2.
Your program will prompt the user for the amount of the investment, the
annualized interest rate, and the number of years of the investment. The
program will then output a nicely formatted table that tracks the value of
the investment year by year.
'''

##def futval():
##
##    print("This program calculates the future value")
##    print("of a ten year investment.")
##
##    principal = eval(input("Enter the initial principal: "))
##    apr = eval(input("Enter the annual interest rate: "))
##
##    for i in range(10):
##        principal = principal * (1 + apr)
##
##    print("The value of the investment in 10 years is: ", principal)

def futval():

    print("This program calculates the future value")
    print("of a ten year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))

    # The "^" symbol centers the string in the specified width
    print("\n{0:^}".format('Year'),  "{0:^20}".format('Principal'))
    print('------------------------------------------\n')

    for i in range(10):
        
        principal = principal * (1 + apr)
        print("{0:2}".format(i), "{0:^23.2f}".format(principal))

'''
Exercise 13

Redo any of the previous programming problems to make them batch-oriented
(using text files for input and output)
'''

def ceasar_cipher_batch():

    # Gather inputs for the batch file process

    #input_file = input('Input file path >>> ' )
    #output_file = input('Output file path >>> ')
    input_file = 'C:/Users/Cole/Documents/Read files/the number of the beast.txt'
    output_file = 'C:/Users/Cole/Documents/Read files/Write here.txt'

    key = int(input('Enter key >>> ' )) # This is serious encryption

    # Open input files
    infile = open(input_file, 'r')
    outfile = open(output_file, 'w')
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    code_word = '' # Set empty string for encrypted message
    for line in infile: # First loop processes each line in the file
        for char in line: # Process each character in each line
            if char != ' ' and char != '\n': # Ignore new line characters and spaces
                # See original program for explanation of encryption logic
                shift = alphabet[(alphabet.index(char) + key) % 26] 
                code_word = code_word + shift        
            elif char == ' ': # Maintain integrity of words by keeping spaces
                              # in the same locations
                code_word = code_word + ' '
 
    print(code_word, file=outfile) # Print the competed string to the write file
    
    infile.close() # Close both files for bookkeeping purposes
    outfile.close()

    print('Process complete, please see: ', output_file)

'''
Exercise 14

Word count. A common utility on Unix/Linux systems is a small program
called "wc." This program analyzes a file to determine the number of
lines, words, and characters contained therein. Write your own version of
wc. The program should accept a file name as input and then print three
numbers howing the count of lines, words, and characters in the file.
'''

def wc():

    # Can be modified to accept any filepath
    input_file = 'C:/Users/Cole/Documents/Read files/the number of the beast.txt'
    #input_file = input('Input file path >>> ' )  

    # Open file
    f = open(input_file, 'r')

    # Returns each line of the file as item in a list
    contents = f.readlines() 

    # Line count
    line_count = len(contents)
    
    # Character Count
    # Loop through each line of the file to remove newline characters
    # Uses standard accumulator pattern

    newline_removed = ''
    for i in contents:
        newline_removed = newline_removed + i.rstrip('\n')

    character_count = len(list(newline_removed))            

    # Word count
    # Split method creates list of words in a string

    word_count = len(newline_removed.split())

    # Close file

    f.close()

    # Print output for user
    print('\n')
    print('LINE COUNT: ', line_count, '\n')
    print('CHARACTER COUNT (with spaces): ', character_count, '\n')
    print('WORD COUNT: ', word_count, '\n')
    
'''
Exercise 15

Write a program to plot a horizontal bar chart of student exam scores.
Your program should get input from a file. The first line of the file contains
the count of the number of students in the file, and each subsequent line
contains a student's last name followed by a score in the range 0 to 100.
Your program should draw a horizontal rectangle for each student where
the lenghth of the bar represents the student's score. The bars should all
determine the size of the window and its coordinates. Bonus: label the
bars at the left end with the student name.
'''

from graphics import *

def e():

    # Graphics library
    
    
    # Get input from file, first line contains number of students in file,
    # all lines after contains the student's last name followed by a score
    # in range 0 - 100

    # -----------
    # File format must be as specified below:
    # <header>
    # <blank line>
    # Student-<name>-<score>
    # Student-<name>-<score>
    # <1etc>

    
    f = 'C:/Users/Cole/Documents/Read files/Exam scores.txt'


    file = open(f, 'r')

    # First line of file contains count of students, loop through it to identify
    # digits and append to new string. Then, convert string to int for math.

    # readline() operation reads next line of the file, so I saved this to
    # a new string for analysis.

    student_count_line = file.readline()
    count_str = ''

    
    for i in student_count_line:
        if i.isdigit():
            count_str = count_str + i

    # Final saved count value
    count = int(count_str)

    # get student scores
    # Step 1: Identify where student scores begin

    line = file.readline()
    while line != '\n':
       line = file.readline()
        
    # Variable line is now equal to the first line with a student's score in
    # it.


    # Step 2: Assign each student's last name

    # exam_scores will be a list of lists containing the student's name
    # and score
    exam_scores = []
       
    for line in file:
        
        # The name and score for each student will be appended to the
        # below list
        name_and_score = []

        # Remove newline character
        line = line.rstrip('\n')

        # Student names and scores are located between hyphen characters,
        # so string slicing was used to isolate the necessary indexes of
        # the string
        name = line[(line.find('-')+1):line.rfind('-')]      
        score = line[line.rfind('-')+1:]

        # Append both the name and score to the inner list
        name_and_score.append(name)
        name_and_score.append(score)                                

        # Append the inner list to the list of list
        exam_scores.append(name_and_score)

    # Create window to diplay grade output
    win = GraphWin("Exam Scores", count*120, count*120)
    win.setCoords(-25, -25, 110, 110)
    win.setBackground("white")

    # Draw student names and bars

    x = -13
    y = -3
    
    for i in exam_scores:

        # Draw each student's name (first index in the list of list)
        Text(Point(x,y), i[0]).draw(win)

        # Draw a rectange corresponding to student's grade (second
        # index in the list of list)
        Rectangle(Point(x+15,y-3), Point(i[1], y+4)).draw(win)

        Text(Point(int(i[1])+3, y), i[1]).draw(win)
        y = y + (120/count)

    # Draw axis
    L1 = Point(2, -8)
    L2 = Point(2,102)
    L3 = Point(2, -8)
    L4 = Point(102, -8)

    Line(L1, L2).draw(win)
    Line(L3, L4).draw(win)

    print(exam_scores)

    # Draw labels for the number of students
