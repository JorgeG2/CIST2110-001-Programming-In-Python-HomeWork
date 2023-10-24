# HW2.py
# Author:


# Question 1:
# Write some code that prompts the user for their age. Depending on the input:
print("Whats youre age?")
age=int(input())

# If the age is less than 13, print "You are a child."
# If the age is between 13 and 19, print "You are a teenager."
# If the age is 20 or older, print "You are an adult."
if age<13:
    print("You are a child.")
elif age>=13 and age<=19:
    print("You are a teenager.")
else:
    print("You are an adult.")


# Question 2:
# Write some code to display the following pattern using a for or while loop:
# 1
# 12
# 123
# 1234
# 12345

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end="")
    print("")

# Question 3:
# Write a Python program that prompts the user to input 10 numbers. After all the numbers are inputted, the program should display:

# The highest number.
# The lowest number.
# The average of all the numbers.
lowest_num=0
highest_num=0
total=0

for i in range(1,11):
    num=int(input("Enter a number: "))
    if i==1:
        lowest_num=num
        highest_num=num
    else:
        if num<lowest_num:
            lowest_num=num
        if num>highest_num:
            highest_num=num
    total+=num

average=total/10
print("The lowest number is " + str(lowest_num))
print("The highest number is " + str(highest_num))
print("The average of all the numbers is " + str(average))

# Question 4:
# Vowel Counter - Write some code that prompts the user to enter a string. The program should then display the number of vowels in the string. IE. If the user enters "Hello World", the program should display 3.
# the vowels are a, e, i, o, u
# Hint: convert the string to lowercase and use a for loop with a counter variable and an if statement

vowels=0
string=input("Enter a string: ")
string=string.lower()

for i in range(0,len(string)):
    if string[i]=="a" or string[i]=="e" or string[i]=="i" or string[i]=="o" or string[i]=="u":
        vowels+=1

print("There are " + str(vowels) + " vowels in the string.")

