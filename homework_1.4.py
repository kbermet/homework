number = int(input('Enter any positive number: '))
i = 0
while number > 10:
    d = number % 10
    number //= 10
    if d > i:
        i = d
print(i)