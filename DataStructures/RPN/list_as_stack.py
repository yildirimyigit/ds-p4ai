"""
  @author: yigit.yildirim@boun.edu.tr
"""


# ornek expression: "15 5 + 3 *"
def rpn(expression):
    # operand: sayi
    # operation: islem
    operations = ['+', '*', '-', '/']
    elements = expression.split()
    stack = []

    for elem in elements:
        # if int --> push to stack
        # otherwise, apply operation
        if elem in operations:
            num2 = stack.pop()
            num1 = stack.pop()

            if elem == '+':
                result = num1 + num2
            elif elem == '*':
                result = num1 * num2
            elif elem == '-':
                result = num1 - num2
            else:
                result = num1 / num2

            stack.append(result)

        else:
            operand = int(elem)
            stack.append(operand)

    print(stack.pop())


rpn("15 7 1 1 + - / 3 * 2 1 1 + + -")
