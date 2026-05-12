current_balance = 10000
print(f'Current Balance: {current_balance}')
try:
    amount_withdraw = int(input('Enter amount to withdraw: '))
    final_amount = current_balance - amount_withdraw
    print('Withdrawal successful!',
          f'\nRemaining Balance: {final_amount}')
except TypeError:
    print('Invalid input! Please enter numbers only.')

