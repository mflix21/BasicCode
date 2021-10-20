"""
# Task-1
age = int(input("What is your age: "))
if (age >= 18) and (age<=60):
    salary = int(input("What is your current salary: "))
    print("You are Eligible for Major Account")
    if salary >= 40000 and salary <= 99000:
        print("You are eligible for Credit Card and your card type is SILVER")
    elif salary >= 100000 and salary <= 199000:
        print("You are eligible for credit card and your card type is GOLD")
    elif salary >= 200000:
        print("Your are eligible for credit card and your card type is PLATINUM")
    else:
        print("You are eligible for Debit Card")
elif (age>=12 and (age<=17)):
    print("You are Eligible! for Minor Account")
else:
    print("You are not eligible for any account")
"""



"""
# Task-2
# Scoring or Grading System
# Take user Input of 6 subjects
# Score them according average marks A++(90-100), A+(75-89), A(60-74), B(45-59), C(30-44),D(0-29)

math = int(input("Math Markst: "))
scien = int(input("science Markst: "))
english = int(input("English Markst: "))
bangla = int(input("Bangla Markst: "))
religion = int(input("Religion Markst: "))
phsycology = int(input("Phsycology Markst: "))
average = (math + scien + english + bangla + religion + phsycology) / 6
print(int(average))

if (average >= 90) and (average <= 100):
    print("You got AA")
elif (average >= 75) and (average <= 89):
    print("You got A+")
elif (average >= 60) and (average <= 74):
    print("You got A")
elif (average >= 45) and (average <= 59):
    print("You got B")
elif (average >= 30) and (average <= 44):
    print("You got C")
else:
    print("You just failed...Better luck next time")
"""


# Task3: 
"""
Take 5 question from the users
Give 4 answers for each question
Take ansers from users
Give points to the users
In this waay count total points
check points and give them task for the next step using if..else
"""

"""
quest1 = input("Anything write string value : ")
ans1 = "A"
ans2 = "B"
ans3 = "C"
ans4 = "D"
if quest1 == ans1:
    a = 1
else:
    a = 0

quest2 = input("Anything write string value : ")
ans5 = "A"
ans6 = "B"
ans7 = "C"
ans8 = "D"
if quest2 == ans6:
    b = 1
else:
    b = 0


quest3 = input("Anything write string value : ")
ans9 = "A"
ans10 = "B"
ans11 = "C"
ans12 = "D"
if quest3 == ans11:
    c = 1
else:
    c = 0


total = int(a) + int(b) + int(c)
print(int(total))

"""

"""
Task-4:
Take numbers from input
check the value either it is even or odd number
"""

"""
num = int(input("Enter a number: "))
if (num % 2 == 0):
    print("Your entered number is EVEN")
else:
    print("Your entered number is ODD")

"""


"""
Task-5:
Taking 3 questions from users input
giving result from users
At the end showing questions and answers in the console screen
"""
"""
question1 = input("Write down your first question: ")
answer1 = input("What would be your answer ?: ")
print("First Question: ", question1)
print("First Answer: ", answer1)

question2 = input("Write down your second question: ")
answer2 = input("What would be your answer ?: ")
print("Second Question: ", question2)
print("Second Answer: ", answer2)

question3 = input("Write down your third question: ")
answer3 = input("What would be your answer ?: ")
print("Third Question: ", question3)
print("Third Answer: ", answer3)

question4 = input("Write down your forth question: ")
answer4 = input("What would be your answer ?: ")
print("Forth Question: ", question3)
print("Forth Answer: ", answer3)

"""

"""
Task-6:
Give 5 songs to choose user's
Take input from user and choose one song
print and play the song that user chose
"""

"""
song01 = "Hello World"
song02 = "He is coding"
song03 = "He is writing something"
song04 = "He is learning"
user_choice = input("Select A B C D: ")

if (user_choice == "A"):
    print("I am playing this song for you")
    print("I am playing this song: ", song01)

elif (user_choice == "B"):
    print("I am playing this song for you")
    print("I am playing this song: ", song02)

elif (user_choice == "C"):
    print("I am playing this song for you")
    print("I am playing this song: ", song03)

elif (user_choice == "D"):
    print("I am playing this song for you")
    print("I am playing this song: ", song04)

else:
    print("You did not select any desired value")
"""


"""
Task-7:
Take input from users
Decide whether it is odd or even
On the basis of odd or even
Go to right direction or left direction
and do something automatic
"""

"""
numb = ""
num = int(input("Enter a number: "))
if (num % 2 == 0):
    numb = "EVEN"
    if (numb == "EVEN"):
        print("Go to Right")
        print("Follow the instruction")
        prt = input("Pick a number between 1 to 4: ")
        print("You are the lucky one")

else:
    numb = "ODD"
    print(" Try again for the coming future")
"""


"""
Task-8:
Quiz Game
"""
"""
print("Welcome to Quiz Game")

answer = input("Do you want to play? ")
if answer.lower() != "yes":
    quit()
else:
    print("Lets play the quiz game :)")

score = 0

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct !")
    score += 1
else:
    print("Incorrect !")

answer = input("What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("Correct !")
    score += 1
else:
    print("Incorrect !")

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct !")
    score += 1
else:
    print("Incorrect !")

answer = input("What does ROM stands for? ")
if answer.lower() == "read only memory":
    print("Correct !")
    score += 1
else:
    print("Incorrect !")

print("You got " + str(score) + " correct answers")
perct = ((score / 4) * 100)
print("You got " + str(perct) + "%")

if perct >= 50 and perct <= 100:
    print("You are qualified for the next round")
else:
    print("Lets play again")
"""

"""
Task-9:
Guess a number
compare it to the random number
if it is matched or not
"""
"""

import random
r = random.randrange(0, 11)
# print("Generated random number is: ", r)
num =int(input("Enter a number between 0 to 10: "))
if r == num:
    print("You are the lucky one")
else:
    print("oops! try again")
"""


"""
# Task-10:
# Guess a number

import random

top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("please type a number larger than 0 for the next tiime")
        quit()
else:
    print("please type a number for the next tiime")
    quit()

rand_number = random.randint(0, top_of_range)
while True:
    guess_number = input("guess a number: ")
    if guess_number.isdigit():
        guess_number = int(guess_number)
    else:
        print("Type a number for the next time")
        continue
    if guess_number == top_of_range:
        print("You are the lucky one")
        break
    else:
        print("You are not lucky one")
"""


"""
Task-11: Rock-Paper-Scissors


import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock Paper scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2

    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1
    
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Good Bye!")

"""

"""
Task-12: Adventure Game

name = input("Type your name: ")
print("Welcome ", name, "to this adventure")

answer = input("you are on a dirt road, it comes to an end or You can go left or right, Which way would like to go left/right? ").lower()
if answer == "left":
    print()
elif answer == "right"
print()

else:
    print()
"""

"""
Task-13:
Take password from user
check password that given a value
open the door. take input what he wants to do
Take actiontions for the user
else terminate the system when time pf password exceeds
message through


password = "open@door"
times_of_password = 0
while True:
    user_password = input("Type your password: ").lower()
    if user_password == password:
        print("The door is opening")
        next_step = input("what you want to do? business/meetings: ").lower()
        if next_step == "business":
            print("You have to wait for few moments")
            break
        elif next_step == "meetings":
            print("this way please and welcome to this meetings")
            break
    else:
        times_of_password += 1
        if times_of_password == 3:
            print("Come 30 minutes later")
            quit()
"""

"""
Task-14: password change


user_password = "***$$$111"
user_email = "abc@gmail.com"
print("Hello user ! How can I help you?")
user_task = input("If you want to change your password, please type yes at any format: ").lower()
if user_task == "yes":
    current_password = input("Type your current password: ")
    if current_password == user_password:
        while True:
            new_password = input("Type your new password: ").lower()
            retype_password = input("Confirm your password: ")
            if retype_password == new_password:
                user_password = retype_password
                print("You password has been changed")
                print("Your new password is ", user_password)
                break
            else:
                print("Password mismatch !")
                continue

    else:
        print("You forgot your password and there is another way to change password")
        user_email_input = input("Type your email address: ").lower()
        if user_email_input == user_email:
            print("password changing link has been provided to your email address")
        else:
            print("This email is not registered")
            quit()

"""


"""
Task-15: smart home
01. entering an apps by checking password
02. no of lights on/off if on, make it off
03. no of AC on/off, if it is on, make it off, select timer and make AC on at specific time
04. make coffee machine on/off according to user input
05. controlling refrigerator's temperature, on/off



passwords = "abc"
print("Welcome to smart home")
password_times = 0

while True:
    user_password = input("Type your password: ").lower()
    if user_password != passwords:
        print("Your password is incorrect")
        password_times += 1
        if password_times == 3:
            print("please try again after 30 minutes")
            break
    else:
        print("You just entered into smart home system")
        user_light_on_off =input("Is your light on or off: ").lower()
        if user_light_on_off == "on":
            print("Turning off the light")
        else:
            print("Your light is already off")

        user_ac =input("Is your AC on or off: ").lower()
        if user_ac == "on":
            print("Turning off the AC")
        else:
            print("Your AC is already off")
            quit()
        
"""
    





