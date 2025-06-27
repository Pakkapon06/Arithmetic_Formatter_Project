def arithmetic_arranger(problems, show_ans = False):
    arr_prob = ""
    space = ' ' * 4
    if len(problems) > 5: #limit amount of problems
        return "Error: Too many problems."
    
    operations = list(map(lambda x: x.split()[1], problems)) #split operations form numbers
    for op in operations:
        if op not in ['+','-']:
            return "Error: Operator must be '+' or '-'."

    first_line = "" #1st num
    second_line = "" #2nd num
    third_line = "" #-----
    fourth_line = "" #result
    num_1 = list(map(lambda x:x.split()[0], problems)) #split first numbers form problems
    num_2 = list(map(lambda x:x.split()[2], problems)) #split second numbers form problems
    value = []

    for i in range(0,len(operations)): #add result to list of value
        if operations[i] == '+':
            value.append(str(int(num_1[i]) + int(num_2[i])))
        elif operations[i] == '-':
            value.append(str(int(num_1[i]) - int(num_2[i])))

    for i in value: #add string of result to fourth_line
        if int(i) > 0:
            fourth_line += (' '*2 + i + space)
        else:
            fourth_line += (' ' + i + space)

    if show_ans: #combine every line to arr_prob
        arr_prob = first_line + "\n" + second_line + "\n" + third_line + "\n" + fourth_line
    else:
        arr_prob = first_line + "\n" + second_line + "\n" + third_line
    return arr_prob

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 20000", "45 + 43", "123 + 49"],True)}')