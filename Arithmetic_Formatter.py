def arithmetic_arranger(problems, show_answers = False):
    arr_prob = ""
    space = ' ' * 4
    if len(problems) > 5:
        return "Error: Too many problems."
    
    operations = list(map(lambda x: x.split()[1], problems)) #split operations form numbers
    for op in operations:
        if op not in ['+','-']:
            return "Error: Operator must be '+' or '-'."

    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""
    num_1 = list(map(lambda x:x.split()[0], problems))
    num_2 = list(map(lambda x:x.split()[2], problems))
    value = []

    for i in num_1 + num_2:
        if not i.isdigit():
            return 'Error: Numbers must only contain digits.'
        elif len(i) > 4:
            return 'Error: Numbers cannot be more than four digits.'

    for i in range(0,len(operations)):
        if operations[i] == '+':
            value.append(str(int(num_1[i]) + int(num_2[i])))
        elif operations[i] == '-':
            value.append(str(int(num_1[i]) - int(num_2[i])))
    
    max_length = []
    for i in range(0,len(num_1)):
        max_length.append(max(len(num_1[i]),len(num_2[i])))

    for i in range(0,len(value)):
        first_line += '  ' + (' ' * (int(max_length[i]) - len(num_1[i]))) + str(num_1[i]) + space
        second_line += str(operations[i]) + ' ' + (' ' * (int(max_length[i]) - len(num_2[i]))) + str(num_2[i]) + space
        third_line += '--' + '-' * int(max_length[i]) + space
        if int(value[i]) > 0:
            fourth_line += ' ' + (' ' * (int(max_length[i]) - len(value[i]) + 1)) + str(value[i]) + space
        else:
            fourth_line += ' ' + (' ' * (int(max_length[i]) - len(value[i]) + 1)) + str(value[i]) + space

    if show_answers: #combine every line to arr_prob
        arr_prob = first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + third_line.rstrip() + "\n" + fourth_line.rstrip()
    else:
        arr_prob = first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + third_line.rstrip()
    return arr_prob

print(f'{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')