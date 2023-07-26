from random import randint

again = "yes"

while again == "yes":
  number = randint(1, 100)
print("OK, Ive thought of a number between 1 and 100.\n")
prompt = "Make a guess: "
answer = -1
counter = 0

while answer != number:
    answer = int(input(prompt))
    counter = counter + 1
    if answer < number:
        print("thats too low.\n")
    elif answer > number:
        print("thats too high.\n")

print("that was my number. well done!")
print(f'\n you took {counter} guesses.')

again = input("would you like another game? ")

print("ok, bye!")