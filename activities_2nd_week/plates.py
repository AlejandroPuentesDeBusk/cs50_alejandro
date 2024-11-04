def main():

    word = str(input("NUMBER: "))

    is_valid(word)


def is_valid(plate):

    if valid(plate) and letters(plate) and special(plate) and zero(plate) and mid(plate):
        print ("Valid")
        return True

    else:
        print ("Invalid")
        return False

#lenght from 2 to 6
def valid(s):

    if len(s) > 1 and len(s) < 7:
        return True

#The first digits must be letters
def letters(s):

    if s[0:2].isalpha():
        return True
    elif s[0:1].isalpha():
        return True
    elif s[0].isalpha():
        return True
    else:
        return False


#It only includes numbers and letters
def special(s):

    if s.isalnum():
        return True
    else: return False

#If the fisrt digit is 0 retuns false
def zero(s):

    lenght = len(s)
    middle = int(lenght/2)
    part_2 = s[middle:lenght]

    if part_2[0] == "0":
        return False
    else:
        return True

#If we have numbers in the middle and at the end a letter retuns false
def mid(s):


    lenght = len(s)
    middle = int(lenght/2)
    part_2 = s[middle:lenght]
    last = len(part_2)-1

    if part_2[0].isdigit() or part_2[1].isdigit():
        if part_2[last].isalpha():
            return False
        else:
            return True
    else:
        return True

if __name__ == "__main__":
    main()
