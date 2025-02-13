def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    top_row = []
    bottom_row = []
    dashes_row = []
    results_row = []

    for problem in problems:
        operand1, operator, operand2 = problem.split()

        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

        if not (operand1.isdigit() and operand2.isdigit()):
            return 'Error: Numbers must only contain digits.'

        if len(operand1) > 4 or len(operand2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # +2 accounts for the operator and space
        width = max(len(operand1), len(operand2)) + 2

        top = operand1.rjust(width)
        bottom = operator + ' ' + operand2.rjust(width - 2)
        dashes = '-' * width

        if show_answers:
            result = str(eval(operand1 + operator + operand2)).rjust(width)

        top_row.append(top)
        bottom_row.append(bottom)
        dashes_row.append(dashes)

        if show_answers:
            results_row.append(result)

    if show_answers:
        return '\n'.join(['    '.join(top_row), '    '.join(bottom_row), '    '.join(dashes_row), '    '.join(results_row)])
    else:
        return '\n'.join(['    '.join(top_row), '    '.join(bottom_row), '    '.join(dashes_row)])


print(
    f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}'
)

# Expected output:
