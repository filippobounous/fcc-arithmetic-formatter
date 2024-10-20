from re import split


def arithmetic_arranger(problems, solution=False):

  operators = ['+', '-']
  first_line = ''
  second_line = ''
  third_line = ''
  solution_line = ''

  if len(problems) > 5:
    return 'Error: Too many problems.'

  for i, prob in enumerate(problems):
    to_solve = split(' ', prob)

    if to_solve[1] not in operators:
      return "Error: Operator must be '+' or '-'."

    if len(to_solve[0]) > 4 or len(to_solve[2]) > 4:
      return 'Error: Numbers cannot be more than four digits.'

    try:
      int(to_solve[0])
      int(to_solve[2])
    except ValueError:
      return 'Error: Numbers must only contain digits.'

    if to_solve[1] == operators[0]:
      result = int(to_solve[0]) + int(to_solve[2])
    else:
      result = int(to_solve[0]) - int(to_solve[2])

    if i != 0:
      first_line += ' ' * 4
      second_line += ' ' * 4
      third_line += ' ' * 4
      solution_line += ' ' * 4

    first_line += '  ' + ' ' * max(len(to_solve[2]) - len(to_solve[0]),
                                   0) + to_solve[0]
    second_line += to_solve[1] + ' ' + (
        ' ' * max(len(to_solve[0]) - len(to_solve[2]), 0) + to_solve[2])
    third_line += (2 + max(len(to_solve[0]), len(to_solve[2]))) * '-'

    solution_line += ' ' * max(
        max(len(to_solve[0]), len(to_solve[2])) + 2 - len(str(result)),
        0) + str(result)

  if solution is False:
    return first_line + '\n' + second_line + '\n' + third_line
  else:
    return first_line + '\n' + second_line + '\n' + third_line + '\n' + solution_line
