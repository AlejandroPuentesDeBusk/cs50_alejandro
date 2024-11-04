import emoji

def emo():

    i = input("Input: ")

    print("Output: ", emoji.emojize(i, language = "alias"))

emo()
