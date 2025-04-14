# first create functions for all the operations



def invalid_error():
    print("Invalid amount entered. Try again.")

def deposit(balance):
    while True:
        try:
            amount = int(input("Enter deposit amount: "))
            if amount > 0:
                balance += amount
                print(f'Deposit successful! Your current balance is {balance}')
                return balance
            else:
                invalid_error()
                continue
        except ValueError:
            invalid_error()
    


def withdraw(balance):
    while True:
        try:
            amount = int(input("Enter withdrawal amount: "))
            if amount < 0:
                invalid_error()
                continue
            elif amount > balance:
                print(f'Insufficient funds. Your balace is {balance}. Try again!')
                continue
            else:
                balance = balance - amount
                print(f'Withdrawal successful! Your current balance is {balance}')
                return balance
        except ValueError:
            invalid_error()
    


def check_balance(balance):
    print(f'Your current balance is {balance}')
    return balance


def choice_func():
    while True:
        choice = str(input('Would you like to do anything else? '
        '(y/n) ')).strip().lower()
        
        if choice == 'y':
            return True
        elif choice == 'n':
            print('Thank you for banking with us!')
            return False
        else:
            print('Invalid choice. Try again.')
            


def error_msg_yn():
    print('Invalid selection. Select y or n')

def main():
    balance = 1000
    while True:
        try:
            operation = int(input('What would you like to do today? \n' 
            'Enter 1 for Deposit \n' 
            'Enter 2 for Withdrawal \n' 
            'Enter 3 to Check your balance \n' 
            'Enter 4 to Exit \n\n:'))
        except ValueError:
            print('Enter a valid number between 1 and 4.')
            continue

        if operation == 1:
            balance = deposit(balance)
        elif operation == 2:
            balance = withdraw(balance)
        elif operation == 3:
            balance = check_balance(balance)
        elif operation == 4:
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid option. Please choose 1–4.")
            continue            
        
        if not choice_func():
            break

main()
