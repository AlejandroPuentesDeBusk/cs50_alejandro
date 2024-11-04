
Amount_Due = 50


while True:

    money = int(input("Insert Coin:"))
    if money == 5 or money == 10 or money == 25:
            Amount_Due = Amount_Due - money

    if Amount_Due <=0:
            break

    else:
            print("Amount Due:", Amount_Due)

Change_Owed = Amount_Due * -1
print("Change Owed:", Change_Owed)
















