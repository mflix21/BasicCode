bangla = int(input("Enter Your Bangla Exam score :"))
english = int(input("Enter Your English exam's score: "))
math=int(input(" Enter your Math exam's score:"))

average=(bangla + english + math)/3
print("Avearge is: ", average)

if (average <=100) and (average >=80):
    print("You got A+")
elif (average <=79) and (average >=59):
    print("You got B")
else:
    print("You failed! lol")
