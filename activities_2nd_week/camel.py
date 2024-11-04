word = input("Write it: ")

string="_"
new=""

for letter in word:
    if letter.isupper():
        new += string + letter.lower()

    else:
        new += letter



print(new)

