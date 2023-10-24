# Project1.py
# Author:


# This project is meant to test your ability from everything we have learned so far in class
# You will need to use variables, if statements, loops, and functions

# Quiz Game:
# Create a simple console-based quiz game where the user answers a series of questions.
# The game should keep track of the user's score and provide feedback based on the answers given.
points=0 
user_name=input("What is your name: ")

if user_name=="":
    print("Please enter a valid name")
    while user_name=="":
        user_name=input("What is your name: ")



# Write a function that displays a welcome message to the user and explains the rules of the game
def welcome():
    print("\nWelcome to the Quiz game " + user_name + "!")
    print("You will be asked a series of questions and you will have to answer them correctly to get points!")
    print("Each question is worht 1 point and there are 5 questions in total!")

print(welcome())

# Implement at least 5 questions, each with 4 answer options (a, b, c, d). Each question should be worth 1 point.


# For each question, display the question and the answer options to the user.
# Use input() to get the user's answer.
# Use if or if-else statements to check if the answer is correct.
# If the answer is correct, display a positive feedback message and add points to the user's score.
# If the answer is incorrect, display a negative feedback message and provide the correct answer.
# Score Tracking:

# Keep track of the user's score throughout the game.
# After all questions have been answered, display the user's total score and a farewell message.
# Function Utilization:

# Create a function to ask a question and check the answer. This function should accept parameters like the question, options, and the correct answer, and return whether the user was correct.
# an example would be def 
# the return value should be a boolean (True or False) for whether the user was correct

def ask_question(question, option_1, option_2, option_3, option_4, correct_answer):
    global points
    print(question)
    print("a. " + option_1)
    print("b. " + option_2)
    print("c. " + option_3)
    print("d. " + option_4)
    answer=input("Enter your answer: ")
    if answer==correct_answer:
        print("Correct!")
        points+=1
        return True
    else:
        print("Incorrect! The correct answer was " + correct_answer)
        return False


Question1 = ask_question("What is the capital of Canada?", "Toronto", "Ottawa", "Montreal", "Vancouver", "b")
print(points)
Question2 = ask_question("What is the capital of the United States?", "New York", "Washington D.C.", "Los Angeles", "Miami", "b")
print(points)
Question3 = ask_question("What is the capital of France?", "Paris", "Marseille", "Lyon", "Toulouse", "a")
print(points)
Question4 = ask_question("What is the capital of England?", "Manchester", "Birmingham", "London", "Liverpool", "c")
print(points)
Question5 = ask_question("What is the capital of Germany?", "Berlin", "Munich", "Hamburg", "Frankfurt", "a")
print(points)

def final_score(points):
    print("Your final score is " + str(points) + " out of 5!")

print(final_score(points))
# Create a function to display the final score, which takes the score as a parameter and displays a message.
# Loops:uyggygyu



# Use a for or while loop to iterate through the questions.
# Variable Casting:
# Ensure that user input is cast and checked appropriately to avoid errors during execution.
# Error Handling:
# Implement basic error handling to manage invalid inputs from the user (e.g., an answer other than a, b, c, or d).
