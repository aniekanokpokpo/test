from typing import List, Tuple

# operatorInput = input("Enter operator, (*, +, - or /) \n")
# firstParamInput = int(input("Enter first numeric parameter  \n"))
# secondParamInput = int(input("Enter second numeric parameter  \n"))


def calculate(op, first, second):
    result = str(first) + ' ' + op + ' ' + str(second) + ' = '
    if op == '+':
        result += str(first + second)
    elif op == 'x':
        result += str(first * second)
    elif op == '-':
        result += str(first - second)
    elif op == '/':
        result += str(first / second)
    else:
        result = 'invalid operator. expected x, + or / but received ' + op

    print(result)


def read_file_to_list() -> List[Tuple[str, str, str]]:
    result: List[Tuple[str, str, str]] = []
    with open("one_calc_fle.txt", 'r') as input_file:
        all_lines = input_file.read()
    line_array = all_lines.split("\n")
    for line in line_array:
        row = line.split(' ')
        entry = row[1], row[2], row[3]
        result.append(entry)
    print(result)
    return result


def calculate_from_file():
    all_inputs = read_file_to_list()
    for in_tuple in all_inputs:
        calculate(in_tuple[0], int(in_tuple[1]), int(in_tuple[2]))

# calculate(operatorInput, firstParamInput, secondParamInput)


calculate_from_file()
