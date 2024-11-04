ex = input("Expresion: ")


x, y, z = ex.split(" ")

x = float(x)
z = float(z)

match y:
    case "+":
        print(x + z)
    case "-":
        print(x - z)
    case "*":
        print(x * z)
    case "/":
        print(x /z)










