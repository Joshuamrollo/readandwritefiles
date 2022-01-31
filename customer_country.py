import csv


def main():
    file = open("customer_country.csv", "w")
    csvfile = open("customers.csv")
    csvreader = csv.reader(csvfile, delimiter=",")
    count = 0
    for row in csvreader:
        file.write(row[1] + " " + row[2] + "," + row[4] + "\n")
        count += 1

    file.write(str(count) + " customers")

    file.close()
    csvfile.close()


main()
