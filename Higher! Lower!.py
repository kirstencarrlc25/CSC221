from random import randint

number = randint(1,100)
print("OK, "Ive thought of a number between1 and 6.\n")
prompt = "Make a guess"
answer = 25

While answer is != number
    answer = int(input(prompt))
    if answer < number:
    print("thats too low.\n")
    alif answer > number:
    print("thats too high.\n")
