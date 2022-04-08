def arithmetic_arranger(problems, result=False):
    arranged_problems = ''''''
    first_operands = ""
    operator_second = ""
    delimiter = ""
    risultato = ""
    if len(problems) > 5:
        return "Error: Too many problems."
    for problem in problems:
        a_problem = problem.split(' ')
        first = a_problem[0]
        second = a_problem[2]
        operator = a_problem[1]
        if not first.isdigit() or not second.isdigit():
            return "Error: Numbers must only contain digits."
        space_problems = 4 * ' '
        the_result = 0
        if operator == '+':
            the_result = int(first) + int(second)
        elif operator == '-':
            the_result = int(first) - int(second)
        else:
            return "Error: Operator must be '+' or '-'."
        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."
        maxlen = 0
        for element in a_problem:
            if len(element) > maxlen:
                maxlen = len(element)
        numdel = 0
        if maxlen < 4:
            delimiter += '-' * maxlen + '-' * 2 
            numdel += maxlen + 2
        else:
            delimiter += '-' * 6
            numdel += 6
        delimiter += space_problems
        first_operands += ' ' * (numdel - len(first)) + first + space_problems
        risultato += ' ' * (numdel - len(str(the_result))) + str(the_result) + space_problems
        operator_second += operator + ' ' * (numdel - len(second) - 1) + second + space_problems
    arranged_problems += first_operands + '\n' + operator_second + '\n' + delimiter + '\n'
    if result == True:
        arranged_problems += risultato
    return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
print(arithmetic_arranger(["78 + 9", "3 + 12", "57 - 13", "7 + 6", "123 - 34", "2 - 1"]))
print(arithmetic_arranger(["10 + 2", "10 * 2"], True))
print(arithmetic_arranger(["3 + 4", "27995 - 3450"]))
print(arithmetic_arranger(["3g + abab", "2 + 3"]))
