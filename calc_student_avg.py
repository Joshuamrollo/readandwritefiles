import csv


def main():
    student_file = open("Student_Scores.csv", mode="r")
    avg_file = open("Student_avg.csv", mode="w")
    csvreader = csv.reader(student_file, delimiter=",")

    for row in csvreader:
        avg = str(round(int(row[1]) + int(row[2]) + int(row[3]) / 3, 2))

        avg_file.write(row[0] + "," + avg + "\n")

    student_file.close()
    avg_file.close()


main()
