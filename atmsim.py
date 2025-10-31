correct_username = "vishwak"
correct_password = "1234"

asking_username = input("Please enter the user name: ")



if asking_username == correct_username:
    asking_password = input("Enter your password: ")
    
    if asking_password == correct_password:
        

        print("\nYou have entered the SBI bank online ATM machine.")
        print('PLEASE CHOOSE THE ACTION YOU WOULD LIKE TO PERFORM:')
        print('1. widhrew')
        print('2. donate')
        
        asking = input("Enter the option you would like to perform (widraw/donate): ").lower()
        

        if asking == 'donate':
            donation_amount = input("How much would you like to donate? ")

            print(f"Thank you for your donation of {donation_amount}!")
            
        elif asking == 'widraw':
            withdrawal_amount = input('How much would you like to widraw? ')

            print(f"Please take your cash of {withdrawal_amount}.")
        else:
  
            print('You have entered the wrong option. Please restart the process.')
    else:

        print('Incorrect password. Please restart the process.')
else:

    print('Incorrect username. Please restart the process.')