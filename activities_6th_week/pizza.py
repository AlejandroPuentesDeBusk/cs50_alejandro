from tabulate import tabulate
import sys
import csv


def main():

    sicilian()

    None

def sicilian():


    menu = []


    try:

        name = str(sys.argv[1])

        test= name.split(".")

        if "csv" not in test:
            sys,exit("Not a csv file")


    except IndexError:
        sys.exit("Too few comand line arguments")

    try:


        with open(name) as file:

            reader = csv.reader(file)

            for row in reader:
                menu.append(row)

        headers = menu[0]
        menu = menu[1:]


        print(tabulate(menu,headers, tablefmt = "grid"))

    except FileNotFoundError:
        sys.exit("File do not exist")



if __name__ == "__main__":
    main()



