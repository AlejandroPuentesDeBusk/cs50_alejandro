import random


def main():

    level = get_level()

    list =generate_integer(level)

    i = 0
    error = 0
    correct = 0

    while True:

        print(f"{list[i]} + {list [i+1]} ", end="")
        ans = int(input("= "))

        res = list[i] + list[i+1]

        if ans != res:
            print("EEE")
            error += 1
        else:
            i+= 2
            error = 0
            correct += 1

        if error == 3:
            print("EEE")
            print(f"The correct andswer is {res}")
            i+= 2


        if i == 20:
            break

    print(f"Score: {correct}")




    ...


def get_level():



    while True:

        try:

            level = int(input("Level: "))

            match level:

                case 1 if level == 1:

                    return 1

                case 2 if level == 2:

                    return 2

                case 3 if level == 3:

                    return 3

        except ValueError:

            print("Just three levels aviable")

    return level


def generate_integer(level):

    list = []

    for i in range (10):


        if level == 1:

            x = random.randint(0,9)
            y = random.randint(0,9)


        elif level ==2:

            x = random.randint(10,99)
            y = random.randint(10,99)

        elif level == 3:

            x = random.randint(100,999)
            y = random.randint(100,999)

        else:
            raise ValueError

        list.append(x)
        list.append(y)

    print(list)

    return list




if __name__ == "__main__":
    main()



