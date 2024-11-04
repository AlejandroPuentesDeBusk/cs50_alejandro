import sys

def main():

    out()
    lines = read()
    logic(lines)
    contar()



def out():
    try:

        a = sys.argv[1]
        a.split(".")

        if "py" in a:
            None
        else:
            sys.exit("Not a python file")

        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")


    except IndexError:

        sys.exit("Too few arguments")


def read():


    try:

        name = str(sys.argv[1])

        with open (name) as file:

            lines = file.readlines()

            lineas_filtradas = [line for line in lines if line.strip() and not line.strip().startswith('#')]

            return lineas_filtradas


    except FileNotFoundError:

        sys.exit("FIle does not exist")


def logic(lineas_filtradas):

    name = str(sys.argv[1])

    with open(name, "w") as file:

        file.writelines(lineas_filtradas)

def contar():

    contador = 0

    name = str(sys.argv[1])

    with open(name) as file:

        lines = file.readlines()

        for line in lines:

            contador += 1

        print(contador)




if __name__ == "__main__":
    main()
