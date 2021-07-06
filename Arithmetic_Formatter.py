
list_of_str = ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]
def arithmetic_formatter(problems, boolean=False):
    #prerequisties
    valid_operators = ["+", "-"]
    first = []
    operator = []
    second = []
    length = []
    line = "-"
    final_string = ""

    #conditions & sorting
    if len(problems) > 5:
        return "Error: Too many problems."
    for example in problems:
        x,*y = example.split()
        if y[0] not in valid_operators:
            return "Error: Operator must be '+' or '-'."
        if not (x.isdigit() and y[1].isdigit()):
            return "Error: Numbers must only contain digits."
        if not (len(x) < 5 and len(y[1]) < 5):
            return "Error: Numbers cannot be more than four digits."
        length.append(int((len(x)+2)))if len(x) > len(y[1]) else length.append(int(len(y[1])+2))

        first.append(x)
        operator.append(y[0])
        second.append(y[1])

    length_second = [n-1 for n in length]

    first_line = ""
    second_line = ""
    line_line = ""
    result_line = ""

    #first row
    for i, number in enumerate(first):
        first_line += f"{number:>{length[i]}}    "

    #second row
    for i, number in enumerate(second):
        second_line += f"{operator[i]}{number:>{length_second[i]}}    "

    #line
    for i, dot_line in enumerate(length):
        line_line += f"{int(dot_line)*line:>{length[i]}}    "
    final_string += "\n"

    first_line.rstrip()
    second_line.rstrip()
    line_line.rstrip()

    # result
    if boolean == True:
        results = [eval(example) for example in problems]
        for i, result in enumerate(results):
            result_line += f"{result:>{length[i]}}    "
        result_line.rstrip()
        final_string = first_line + "\n" + second_line +"\n" + line_line +"\n" + result_line
    else:
        final_string = first_line + "\n" + second_line + "\n" + line_line
    return final_string

print(arithmetic_formatter(list_of_str))

