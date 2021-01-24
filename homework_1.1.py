# Calculator

first_num = float(input('Enter first number:'))
second_num = float(input('Enter second number:'))

print('Addition', first_num + second_num)
print('Substraction', first_num - second_num)
print('Multiplication', first_num * second_num)
if second_num == 0:
    print('Choose another number')
else:
    print('Division', first_num / second_num)

# Anniversary

name = input('Please enter your name: ')
age = int(input('Enter your age: '))
retire_age = 70
if age >= 70:
    print('You are already retired')
elif age%5 == 0:
    print('Congrats, its your anniversary year')
    print('You will get retired in', retire_age - age, 'years')