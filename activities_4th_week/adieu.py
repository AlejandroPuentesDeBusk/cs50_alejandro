import inflect

p = inflect.engine()


names = []


while True:

    try:

        name = input()

        names.append(name)

    except EOFError:

        new_names = p.join(names)

        print(f"Adieu, adieu, to {new_names}")
        break








