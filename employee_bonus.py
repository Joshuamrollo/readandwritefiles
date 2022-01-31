import csv


def main():
    csvfile = open("EmployeePay.csv")
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        print(
            (
                row[1]
                + " "
                + row[2]
                + " total pay: "
                + str(float(row[3]) + (float(row[3]) * float(row[4])))
            ).rstrip("\n")
        )

    csvfile.close()


main()
