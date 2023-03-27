import sys


def main():
    line = sys.argv[1]
    line = line.split()
    for i in line:
        print(i[0], end="")
    print()


if __name__ == "__main__":
    main()
