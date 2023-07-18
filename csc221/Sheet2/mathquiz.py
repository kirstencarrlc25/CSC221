from random import randint
score = 0
for x in range (3): 
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    question = "What is " + str(num1) + " times " + str(num2) + "? "

    answer = int(input(question))
    if answer == num1 * num2:
        print("You're right")
        score = score + 1
    if answer != num1 * num2:
        print('Try again')

print("You got " + str(score) + " questions right.")