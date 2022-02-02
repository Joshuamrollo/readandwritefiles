import csv


def main():
    csvfile = open("EmployeePay.csv")
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        print(("Fname: " + row[1]).rstrip("\n"))
        print(("Lname: " + row[2]).rstrip("\n"))
        print(("Salary: $" + "{:,}".format(int(row[3]))).rstrip("\n"))
        print(("Bonus: " + row[4] + "%").rstrip("\n"))
        print(
            (
                "Total pay: $"
                + "{:,}".format(float(row[3]) + (float(row[3]) * float(row[4])))
            ).rstrip("\n")
        )
        a = input()

    csvfile.close()


main()
