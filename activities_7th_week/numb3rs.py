import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    matches = re.search(r"^(0-9{1,3}.){3}(0-9{1,3}$", ip)

    if matches:
        print("succes")

    else:
        print("Not right")




if __name__ == "__main__":
    main()
