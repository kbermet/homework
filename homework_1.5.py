sales = int(input('Enter your company total turnover: '))
staff= int(input('Number of employees: '))
cost = int(input('Enter costs: '))
if sales >= cost:
    result = (f'Your profitability is:', format(sales/cost))
    print('Your firm is doing fine')
if sales <= cost:
    print('You need to decrease costs')
profit = (sales-cost)-sales
turn_per_staff = profit/staff
print('Your profit per employee is', turn_per_staff)