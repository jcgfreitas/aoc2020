from util.file import read


def main():
    # part1
    lines = read('sample1.txt')
    values = {}
    numbers = []
    for line in lines:
        values[int(line)] = True
        numbers.append(int(line))
    for val in values:
        dif = 2020 - val
        if dif in values:
            res = val * dif
            print(f'pair found: {val}, {dif}')
            print(f'answer: {res}')
            break
    # part2
    for val1 in numbers:
        dif = 2020 - val1
        numbers2 = list(filter(lambda x: x <= dif, numbers))
        for val2 in numbers2:
            dif2 = 2020 - val1 - val2
            if dif2 in values:
                res = val1 * val2 * dif2
                print(f'result found: {val1}, {val2}, {dif2}')
                print(f'answer: {res}')
                return


if __name__ == '__main__':
    main()