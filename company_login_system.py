stored_user = 'admin'
stored_pass = 'python123'
attempts = 3

while attempts > 0:
    print(f'\nRemaining attempts: {attempts}')
    user_input = input('Username: ')
    pass_input = input('Password: ')

    # Manual check for empty fields
    if user_input == "" or pass_input == "":
        print('Fields cannot be empty!')
        continue 

    # Checking if credentials match
    if user_input == stored_user and pass_input == stored_pass:
        print('Login Successful')
        
        # Menu appears only after a successful login
        while True:
            print('\n1 - View Employee Records', '\n2 - Logout')
            choice = input('Enter choice: ')
            if choice == '1':
                print("Viewing records...")
            elif choice == '2':
                print("Logging out...")
                break # Exits the menu loop
            else:
                print('Invalid choice. Please try again!')
        break # Exits the login loop entirely
    else:
        attempts -= 1
        print('Incorrect Credentials')

if attempts == 0:
    print('Account Locked')
