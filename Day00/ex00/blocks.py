import sys


def check():
	if len(sys.argv) == 2 and sys.argv[1].isdigit():
		return 1
	else:
		print('Error: wrong number of argument or last argument not digital.')


def main():
	if check():
		string = int(sys.argv[1])
		if string >= 10:
			string = 10
		for _ in range(string):
			line = input()
			if len(line) == 32 and line.startswith('00000') and line[5] != '0':
				print(line)


if __name__ == "__main__":
	main()

# cat data_hashes.txt| python3 blocks.py 10