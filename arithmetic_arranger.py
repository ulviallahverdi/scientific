def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = []
    for problem in problems:
        operands = problem.split()
        operand1 = operands[0]
        operator = operands[1]
        operand2 = operands[2]

        if operator != "+" and operator != "-":
            return "Error: Operator must be '+' or '-'."

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        if operator == "+":
            result = int(operand1) + int(operand2)
        else:
            result = int(operand1) - int(operand2)

        max_length = max(len(operand1), len(operand2)) + 2
        arranged_problems.append(f"{operand1.rjust(max_length)}\n{operator} {operand2.rjust(max_length - 2)}\n{'-' * max_length}")

        if show_answers:
            arranged_problems[-1] += f"\n{str(result).rjust(max_length)}"

    arranged_problems = "    ".join(arranged_problems)
    return arranged_problems
