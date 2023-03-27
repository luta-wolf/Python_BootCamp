template = [
    '*   *',
    '** **',
    '* * *'
]


def check_line(line: str) -> None:
    if len(line) != 5:
        print('Error')
        quit()


def check_template(lines: list) -> bool:
    global template
    for i in range(len(template)):
        for j in range(len(template[i])):
            if template[i][j] == '*' and lines[i][j] != '*' or template[i][j] != '*' and lines[i][j] == '^':
                return False
    return True


def main():
    lines = []
    for i in range(3):
        line: str = input()
        check_line(line)
        lines.append(line)
    print(check_template(lines))


if __name__ == "__main__":
    main()

# cat m.txt | python3 mfinder.py
