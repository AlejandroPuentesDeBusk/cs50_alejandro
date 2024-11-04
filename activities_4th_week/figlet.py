import sys
from pyfiglet import Figlet

figlet = Figlet()

#figlet.getFonts()

try:

    x = sys.argv[1]

    match x:

        case x if sys.argv[1] == "-f":

            text = input("Input: ")

            figlet.setFont(font = sys.argv[2])

            print(figlet.renderText(text))

        case _:

            sys.exit("Incorrect argument")

except IndexError:

            text = input("Input: ")

            figlet.setFont(font = "roman")

            print(figlet.renderText(text))


