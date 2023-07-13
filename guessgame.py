from random import randint

number = randint(1, 100)
print("OK, Ive thought of a number between 1 and 100.\n")
prompt = "Make a guess: "
answer = -1
counter = 0

while answer is != number:
    answer = int(input(prompt))
    counter = counter + 1
    if answer < number:
        print("thats too low.\n")
    elif answer > number:
        print("thats too high.\n")

print("that was my number. well done!")
print(f'\n you took {counter} guesses.')