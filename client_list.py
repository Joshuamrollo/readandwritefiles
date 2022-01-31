def main():
    with open("clients.txt", "r") as in_file:
        for idx, line in enumerate(in_file):
            print((str(idx + 1) + ". " + line).rstrip("\n"))


main()
