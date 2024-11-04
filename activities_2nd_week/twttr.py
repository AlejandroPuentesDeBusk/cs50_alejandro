def main():

    word = input("Word: ")

    shorten(word)



def shorten(string):

    new=""

    for letter in string:

        new += letter.lstrip("aeiouAEIOU")

    return new


if __name__ == "__main__":
    main()
