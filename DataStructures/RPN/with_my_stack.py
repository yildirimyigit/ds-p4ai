"""
  @author: yigit.yildirim@boun.edu.tr
"""

from my_stack import MyStack


# ornek expression: "15 5 + 3 *"
def rpn(expression):
    # operand: sayi
    # operation: islem
    operations = ['+', '*', '-', '/']
    elements = expression.split()
    stack = MyStack()

    for e in elements:
        if e in operations:
            num2 = stack.pop()
            num1 = stack.pop()

            if e == '+':
                result = num1 + num2
            elif e == '*':
                result = num1 * num2
            elif e == '-':
                result = num1 - num2
            else:
                result = num1 / num2

            stack.push(result)
        else:
            num = int(e)
            stack.push(num)

    print(stack.pop())


rpn("15 5 3 + *")
