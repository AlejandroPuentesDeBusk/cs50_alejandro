import random


while True:

    try:
        value = int(input("Level: "))

        if value < 1:
            raise ValueError

        break

    except ValueError:

        print("That's not a level")


a = random.randint(1,value)


while True:

    try:
        ans = int(input("Guess: "))

        if ans < a:
            print("too small!")

        elif ans > a:
            print("Too large!")

        elif ans == a:
            print("Just right!")
            break

    except ValueError:

        print("Thats not a number")




