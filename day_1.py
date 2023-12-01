def find_numbers(calibrator_line):
    numbers = []
    for c in calibrator_line:
        if c.isdigit():
            numbers.append(c)

    return numbers[0], numbers[-1]


def part1():
    with open('day_1.txt', 'r') as file:
        sum = 0
        lines = file.readlines()

        for line in lines:
            first, last = find_numbers(line)
            sum += int(first + last)

        print(sum)


def part2():
    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    with open('day_1.txt', 'r') as file:
        sum = 0

        lines = file.readlines()
        for line in lines:
            numbers = []
            for i, c in enumerate(line):
                if c.isdigit():
                    numbers.append(c)
                    # print('Adding', c, 'as a number')
                else:
                    for digit in digits:
                        if line[i:i + len(digit)] == digit:
                            numbers.append(str(digits.index(digit) + 1))
                            # print('Adding', str(digits.index(digit) + 1), 'as a word')

            print(numbers)
            n = numbers[0] + numbers[-1]
            print(n)
            sum += int(n)

        print(sum)

part2()