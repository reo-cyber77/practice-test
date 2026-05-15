import datetime
now = datetime.datetime.now()
def login(attempts, username, password):
    with open('accounts.txt','r') as file:
        for acc in file:
            with open ('security_logs.txt','a') as security_logs:
                if username and password in acc:
                    print('Access Granted!',
                      '\nLogin attempt recorded successfully.')
                    security_logs.write(f'\n{now.strftime('%Y-%m-%d %I:%M:%S')}|{username}|SUCCESSFUL LOGIN')
                else:
                    print('Access Denied!',
                        '\nLogin attempt recorded successfully.')
                    security_logs.write(f'\n{now.strftime('%Y-%m-%d %I:%M:%S')}|{username}|FAILED')
                    attempts_tuple = (username, password)
                    attempts.append(attempts_tuple)
                    if len(attempts) > 3:
                        print('You have used all the attempts')
                        break

                    
                   
def view_logs():
    with open('security_logs.txt', 'r') as file:
        content = file.read()
        print(content)


def count_failed_attempts(attempts):
    print(f'Attempts: {len(attempts)}')

                
            
                












print('====================================',
      '\n\nCYBERSECURITY LOGIN AUDIT TRACKER',
      '\n\n====================================',
      '\n\n1 - Login',
      '\n2 - View Logs',
      '\n3 - Count Failed Attempts',
      '\n4 - Exit')
attempts_login = []
while True:
    choice = input('Choose: ')
    if choice == '1':
        emp_username = input('Username: ')
        emp_password = input('Password: ')
        login(attempts_login, emp_username, emp_password)
    elif choice == '2':
        view_logs()
    elif choice == '3':
        count_failed_attempts(attempts_login)
    elif choice == '4':
        break
    else:
        print('Invalid Choice!')