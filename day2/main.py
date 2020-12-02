from util.file import read
from operator import xor

def main():
    # part1
    lines = read('sample1.txt')
    valid_passwords1 = 0
    valid_passwords2 = 0
    for line in lines:
        # pre processing
        vals = line.split(': ')
        rule_vals = vals[0].split(' ')
        char = rule_vals[1]
        minimum = int(rule_vals[0].split('-')[0])
        maximum = int(rule_vals[0].split('-')[1])
        password = vals[1]
        count = password.count(char)

        if minimum <= count <= maximum:
            valid_passwords1 += 1

        # part2
        if xor(password[minimum - 1] == char, password[maximum - 1] == char):
            valid_passwords2 += 1

    print(valid_passwords1)
    print(valid_passwords2)


if __name__ == '__main__':
    main()
