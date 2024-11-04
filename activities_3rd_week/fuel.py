def main():

    while True:
        try:

            fraction = input("state: ")
            state = convert(fraction)

            break

        except ValueError:
            print("It is not a fraction ")

        except ZeroDivisionError:
            print("It can´t be zero")


    res=gauge(state)

    print(res)




def convert(fuel):

    try:
        a, b = fuel.split("/")
        a = int(a)
        b = int(b)
    except ValueError:
        raise ValueError("Both a and b must be integers")

    if b == 0:
        raise ZeroDivisionError


    if a > b:
        raise ValueError("a can't be greater than b")



    frac = a/b

    per = 100*frac
    per = round(per)


    return per


def gauge(per):


    if per <= 1:
         return "E"
    elif per >= 99:
         return "F"
    else:
         return f"{per}%"



if __name__ == "__main__":
    main()








