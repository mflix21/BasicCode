"""
Loop:
There are two kinds of loops used in python (i) while loops (ii) for loops
(i) while loops: we are going to show (a) only while loops, (b) while loops with break, (c) while loops with continue

(a). example of only while loops:

01. print 1 to 10 using only while loops
i = 1
while i <= 10:
    # print(i)
    print(i, end=' ')    # print value in one line
    i += 1

02. print even number from 1 to 10
i = 1
while i <= 10:
    if i % 2 == 0:
        print(i, end=' ')    # print value in one line
    i += 1

03. ptint odd number 1 to 10:

i = 1
while i <= 10:
    if i % 2 == 1:
        print(i, end=' ')    # print value in one line
    i += 1

04. Taking start and end number input
and print from start to end

start_number = int(input("Type a start number: "))
destination_number = int(input("Type a ending number: "))
if start_number < destination_number:
    while start_number <= destination_number:
            print(start_number, end=' ')
            start_number += 1
else:
    print("start number is greater than destination number")
    exit()

05. Taking start and end number input
and print even number from start to end

start_number = int(input("Type a start number: "))
destination_number = int(input("Type a ending number: "))
if start_number < destination_number:
    while start_number <= destination_number:
        if start_number % 2 == 0:
            print(start_number, end=' ')
        start_number += 1
else:
    print("start number is greater than destination number")
    exit()

06. Taking start and end number input
and print odd number from start to end

start_number = int(input("Type a start number: "))
destination_number = int(input("Type a ending number: "))
if start_number < destination_number:
    while start_number <= destination_number:
        if start_number % 2 == 1:
            print(start_number, end=' ')
        start_number += 1
else:
    print("start number is greater than destination number")
    exit()

07. Taking start and end number input
two conditions (a) start = small, end = big (b) start = big, end = small
print odd or even number

start_number = int(input("Type a start number: "))
destination_number = int(input("Type a ending number: "))
if start_number < destination_number:
    while start_number <= destination_number:
        if start_number % 2 == 0:
            print(start_number, end=' ')
        start_number += 1
else:
    while start_number >= destination_number:
        if start_number % 2 == 1:
            print(start_number, end=' ')
        start_number -= 1



(b). while loops with break: example of while loops with break statement

(01). Taking start and end number input break number 
print start to end number and
after break the program will terminate
break out the while loop

start_number = int(input("Type a start number: "))
destination_number = int(input("Type a ending number: "))
break_number = int(input("Type a break number when the loop will terminate: "))
while start_number <= destination_number:
    print(start_number, end = ' ')
    if start_number == break_number:
        break
    start_number += 1

(02). addition of number (01) and just print even number
start_number = int(input("Type a start number: "))
destination_number = int(input("Type a ending number: "))
break_number = int(input("Type a break number when the loop will terminate: "))
while start_number <= destination_number:
    if start_number % 2 == 0:
        print(start_number, end = ' ')
    if start_number == break_number:
        break
    start_number += 1

(03). addition of number (01) and just print odd number
start_number = int(input("Type a start number: "))
destination_number = int(input("Type a ending number: "))
break_number = int(input("Type a break number when the loop will terminate: "))
while start_number <= destination_number:
    if start_number % 2 == 1:
        print(start_number, end = ' ')
    if start_number == break_number:
        break
    start_number += 1

(04). take input from the user you want to play games if yes
task needs to be completed you cant quit until questionneries will over
q1 to q3 the question and answer session will be recorded and answers shows
into the screen with question and answer

print("welcome to this world")
break_point = 1
user_input = input("you want to play the game ! type yes/no for the next steps: " ).lower()
answer_list = []
if user_input == "yes":
    print("you have made right decission")
    while break_point <= 3:
        print("Question ?")
        
        question_1 = input("Answers: ")
        answer_list.append(question_1)
        if break_point == 3:
            print(answer_list)
            break

        break_point += 1

(05). Take 3 questions
give 3 answers
and show recorded questions and answers
when questions asked finish
using break statement
terminate the loop

i = 0
question = ["What is your name ? ", "What is your profession ? ", "What is your monthly salary ? "]
answer = []
while i <= (len(question) -1):
    print(question[i])
    user_answers = input("Type your answer: ")
    answer.append(user_answers)

    if i == 2:
        print("your recorded questions and answers are")
        print(question[0], end= ' :')
        print(answer[0])
        print(question[1], end= ' :')
        print(answer[1])
        print(question[2], end= ' :')
        print(answer[2])
        break
    i += 1

(06). Quiz game: KBC

answers = []
i = 0
result = 0
print("welcome to the quiz game")
quetions = ["IAD stands for", "CPU stands for", "ROM stands for"]
answer_1 = ["a. internet addiction disorder", "b. internet alluminium detection"]
answer_2 = ["a. central pi united", "b. central processing unit"]
answer_3 = ["a. read only memory", "b. read optimization moment"]
while i <= (len(quetions) - 1):
    print(quetions[i])
    if i == 0:
        print(answer_1[0])
        print(answer_1[1])
    elif i == 1:
        print(answer_2[0])
        print(answer_2[1])
    elif i == 2:
        print(answer_3[0])
        print(answer_3[1])
    else:
        break
    user_answer = input("type A or B : ").lower()
    answers.append(user_answer)
    # print(answers)
    i += 1

j = 0
while j <= (len(answers) - 1):
    if j == 0 and answers[j] == "a":
        result += 1
    if j == 1 and answers[j] == "b":
        result += 1
    if j == 2 and answers[j] == "a":
        result += 1
    j += 1
print("your score: ", result)



(c). while loop with continue statement: example of while loop with continue statement

(01). take input start number
take input end number
take number while using continue statemt with while loop
print from start to end aftre using continue statement


starting_point = int(input("type a starting point number: "))
ending_point = int(input("type a ending point number: "))
continue_point = int(input("type a continue point number: "))

## different output
while starting_point <= ending_point:
    starting_point += 1
    if starting_point <= continue_point:
        continue
    print(starting_point, end= ' ')

## different output
while starting_point < ending_point:
    starting_point += 1
    if starting_point <= continue_point:
        continue
    print(starting_point, end= ' ')




## another example of continue
start_no = 1
end_no = 9
while start_no < end_no:
    start_no += 1
    if start_no < 5:
        continue

    if start_no % 2 == 0:
        print(start_no, end= ' ')



## another example of continue
start_no = 1
end_no = 9
while start_no < end_no:
    start_no += 1
    if start_no < 5:
        continue

    if start_no % 2 == 1:
        print(start_no, end= ' ')




(c). for loop: example of for loop

(01). example of for loop'

list = []
for alplabett in "Mehedi":
    list.append(alplabett)
    print(alplabett, end=' ')
    
print('\n', list)

(02). another example of loop

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in list:
    print(num, end= ' ')
    

print('\n', list[0])

"""

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for num in list:
#     print(num, end= ' ')












    



































    
    
