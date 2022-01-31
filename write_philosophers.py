def main():
    outfile = open("philosophers.txt", "w")

    outfile.write("John Locke\nDavid Hume\nEdmund Burke\n")

    outfile.close()


def add_my_name():
    outfile = open("philosophers.txt", "a")

    outfile.write("Joshua Rollo")

    outfile.close()


main()
add_my_name()
