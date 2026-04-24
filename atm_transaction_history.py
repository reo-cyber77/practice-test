transactions = (('Deposit', 5000),
                ('Withdraw', 1200),
                ('Deposit', 3000))
total_deposit = 0
total_withdrawals = 0

print('Transaction History: ')
for t in transactions:
    trans_type = t[0]
    amount = t[1]

    print(f'{trans_type}: {amount}')

    if trans_type == 'Deposit':
        total_deposit += amount
    elif trans_type == 'Withdraw':
        total_withdrawals += amount


final_balance = total_deposit - total_withdrawals
print(f'\nTotal Deposits: {total_deposit}')
print(f'Total Withdrawls: {total_withdrawals}')
print(f'Final Balance: {final_balance}')
