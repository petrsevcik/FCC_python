# * Situations that will return an error:
#   * If there are **too many problems** supplied to the function. The limit is **five**, anything more will return:
#     `Error: Too many problems.`
#   * The appropriate operators the function will accept are **addition** and **subtraction**. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be:
#     `Error: Operator must be '+' or '-'.`
#   * Each number (operand) should only contain digits. Otherwise, the function will return:
#     `Error: Numbers must only contain digits.`
#   * Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be:
#     `Error: Numbers cannot be more than four digits.`

list_of_str = ["32 - 98888", "3801 - 2", "45 + 43", "123 + 49"]
def arithmetic_formatter(problems, boolean=False):
    #prerequisties
    valid_operators = ["+", "-"]
    first = []
    second = []
    line = "----"
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
        sec = "".join(y)
        first.append(x)
        second.append(sec)


    for number in first:
        final_string += f"{number:>7}"
    final_string += "\n"
    for number in second:
        final_string += f"{number:>7}"
    final_string += "\n"
    for i in range(len(problems)):
        final_string += f"{line:>7}"
    final_string += "\n"
    if boolean == True:
        results = [eval(example) for example in problems]
        for result in results:
            final_string += f"{result:>7}"
    return final_string

print(arithmetic_formatter(list_of_str))


