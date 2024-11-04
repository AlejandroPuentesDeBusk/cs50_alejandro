import requests
import sys


def main():

    multy = exit()
    data = server(multy)
    print(f"${data:,.4f}")



def server(multy):

    url = "https://api.coindesk.com/v1/bpi/currentprice.json"

    try:

        response = requests.get(url)

    except requests.RequestException:

        print("Errror")


    datos = response.json()
    rate = datos['bpi']['USD']['rate']
    rate = rate.replace(",", "")

    bitcoin = float(rate)

    price = bitcoin * multy

    return price

def exit():

     try:

         a = (sys.argv[1])


     except IndexError:

         sys.exit("Missing command-line argument")

     try:

         multy = float(sys.argv[1])


     except ValueError:

         sys.exit("Command-line argument is not a number")

     return multy






if __name__ == "__main__":
    main()
