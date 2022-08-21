f_n = input('Type in your first number: ')
s_n = input('Type in your second number: ')
math = input('What are we doing? ')

math_multiply = math_plus = math_minus = math_divide = False

if math == '*':
    math_multiply = True
if math == '+':
    math_plus = True
elif math == '-':
    math_minus = True
elif math == '/':
    math_divide = True

if math_multiply:
    print(f'Your answer is: {int(f_n) * int(s_n)}')
elif math_plus:
    print(f'Your answer is: {int(f_n) + int(s_n)}')
elif math_minus:
    print(f'Your answer is: {int(f_n) - int(s_n)}')
elif math_divide:
    print(f'Your answer is: {int(f_n) / int(s_n)}')
else:
    print("It's not an arithmetic operation")
