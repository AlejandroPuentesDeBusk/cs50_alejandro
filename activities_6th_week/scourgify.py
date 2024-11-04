import csv
import sys


def main():

    write(r_file())


def r_file():

    students= []

    try:
        file_name = sys.argv[1]
        afther= sys.argv[2]

        if len(sys.argv) >3:
            sys.exit("Too many comand-line arguments")


    except IndexError:
        sys.exit("To few command-line arguments")

    with open(file_name) as file:

        reader = csv.DictReader(file)

        for dic in reader:

            last, first = dic["name"].split(",")
            first = first.strip()
            last = last.strip()

            students.append({"first":first,"last":last, "house":dic["house"]})

        return students


def write(students):



    after = sys.argv[2]

    with open (after, "w") as file:

        writer = csv.DictWriter(file, fieldnames = ["first","last","house"])
        writer.writeheader()


        for student in students:
            writer.writerow({"first":student["first"],"last":student["last"], "house": student["house"]})




if __name__ == "__main__":
    main()
