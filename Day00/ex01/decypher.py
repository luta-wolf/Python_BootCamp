import sys


def main():
    line: str = sys.argv[1]
    line: list = line.split()
    for i in line:
        print(i[0], end="")
    print()


if __name__ == "__main__":
    main()

# python3 decypher.py "Have you delivered eggplant pizza at restored keep?"
