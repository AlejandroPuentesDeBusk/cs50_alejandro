months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}


def date():

    while True:

        try:

            date = input("Date: ")

            if "/" in date:

                date = date.split("/")

                day = int(date[1])
                if day > 30:
                    raise ValueError
                month = int(date[0])
                if month > 12:
                    raise ValueError
                year = int(date[2])

                print(f"{year}-{month:02}-{day:02}")

                break

            elif "," in date:

                date = date.replace(",", "").split(" ")

                day = int(date[1])
                if day > 30:
                    raise ValueError
                month = months[date[0]]
                year = int(date[2])

                print(f"{year}-{month:02}-{day:02}")

                break

        except ValueError:
            print("WOOPS")


date()
