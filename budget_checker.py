budget = 500
print(f'Budget: {budget}')
expenses = [100, 200, 300]
print(f'Expenses: {expenses}')
total = sum(expenses)
print(f'Total:{total}')
if total != budget:
    print('Over Budget')
else:
    print('Exact Budget')
