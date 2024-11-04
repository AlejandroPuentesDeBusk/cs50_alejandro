import sys
from PIL import Image, ImageOps



def main():
    manage()
    im()


def manage():

    check = None

    try:

        original = str(sys.argv[1])
        new = str(sys.argv[2])

        if len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")

                # Verificar el primer argumento
        if not ("jpg" in sys.argv[1] or "png" in sys.argv[1]):
            sys.exit("Invalid Input")

        # Verificar el segundo argumento
        if not ("jpg" in sys.argv[2] or "png" in sys.argv[2]):
            sys.exit("Invalid Input")


        if "jpg" in sys.argv[1] and "jpg" in sys.argv[2]:
            check = True

        elif "png" in sys.argv[1] and "png" in sys.argv[2]:
            check = True

        if check != True:
            sys.exit("Input and Output have different extensions")

    except IndexError:
        sys.exit("Too few command-line arguments")




def im():

    inp = str(sys.argv[1])
    out = str(sys.argv[2])

    shirt = Image.open("shirt.png")
    original = Image.open(inp)
    size = shirt.size
    print(size)



    resized_original =ImageOps.fit(original,size, method = Image.Resampling.BICUBIC, bleed = 0.0,centering = (0.5, 0.5))
    resized_shirt = ImageOps.contain(shirt, size)
    resized_original.paste(resized_shirt,(0,0), resized_shirt)
    resized_original.save(out)






















if __name__ == "__main__":
    main()
