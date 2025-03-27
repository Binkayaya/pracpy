balance = 1000
loop_1 = True
while loop_1 is True:
    try:
        operation = int(input('What would you like to do today? \n Enter 1 for Deposit \n Enter 2 for Withdrawal '
        '\n Enter 3 to Check your balance \n Enter 4 to Exit \n\n:'))
        
        if operation == 1:
            deposit_amount = int(input('How much would you like to deposit?'))
            balance = balance + deposit_amount
            print(f'Your new balance is {balance}')
            loop_2 = True
            while loop_2 is True:
                try:
                    choice = int(input('Would you like to do anything else? \n Enter 1 for Yes'
                    '\n Enter 2 for No \n\n:'))
                    if choice == 1:
                        loop_2 = False
                    elif choice == 2:
                        print('Thank you for banking with us!')
                        loop_1 = False
                    break
                except ValueError:
                    print("Invalid choice! Please choose either 1 or 2.")


        elif operation == 2:
            withdrawal_amount = int(input('How much would you like to withdraw?'))
            if withdrawal_amount > balance:
                print(f'Not enough balance. Current balance is {balance}. Try again!')
                continue
            else:
                balance = balance - withdrawal_amount
                print(f'Your new balance is {balance}')
                loop_2 = True
                while loop_2 is True:
                    try:
                        choice = int(input('Would you like to do anything else? \n Enter 1 for Yes'
                        '\n Enter 2 for No \n\n:'))
                        if choice == 1:
                            loop_2 = False
                        elif choice == 2:
                            print('Thank you for banking with us!')
                            loop_1 = False 
                        break
                    except ValueError:
                        print("Invalid choice! Please choose either 1 or 2.")
            
        elif operation == 3:
            print(f'Your current balance is {balance}')
            loop_2 = True
            while loop_2 is True:
                try:
                    choice = int(input('Would you like to do anything else? \n Enter 1 for Yes'
                    '\n Enter 2 for No \n\n:'))
                    if choice == 1:
                        loop_2 = False
                    elif choice == 2:
                        print('Thank you for banking with us!')
                        loop_1 = False
                    break 
                except ValueError:
                    print("Invalid choice! Please choose either 1 or 2.")
                    
        elif operation == 4:
            print('Thank you for banking with us!')
            break

    except ValueError:
        print("Invalid choice! Please choose among 1,2,3 and 4")
    