def check_line(line: str):
    if len(line) != 5:
        print('Error')
        quit()


def main():
    count: int = 0
    for i in range(3):
        line: str = input()
        check_line(line)
        if i == 0 and line[0] == line[4] == '*' and line[1] != '*' and line[2] != '*' and line[3] != '*':
            count += 1
        elif i == 1 and line[0] == line[1] == line[3] == line[4] == '*' and line[2] != '*':
            count += 1
        elif i == 2 and line[0] == line[2] == line[4] == '*' and line[1] != '*' and line[3] != '*':
            count += 1
    if count == 3:
        print(True)
    else:
        print(False)


if __name__ == "__main__":
    main()

# cat m.txt | python3 mfinder.py
