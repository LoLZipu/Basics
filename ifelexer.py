mode = input('Enter math operation(+,-,*,/) or f for Celsius to Fahrenheit conversion: ')
a = float(input('Enter first number: '))
if mode.lower() == 'f':
    print(f'{a} Celsius is equivalent to {(a*9/5)+32 } fahrenheit')
else:
    b = float(input('Enter second number: '))

    if mode == '+':
        print(f'Answer is: {a + b}')
    elif mode == '-':
        print(f'Answer is: {a - b}')
    elif mode == '*':
        print(f'Answer is: {a * b}')
    elif mode == '/':
        print(f'Answer is: {a / b}')
    else:
        print('Input error!')

