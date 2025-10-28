askingUserName = input('Enter your username: ')

# Check if username contains only letters
if not askingUserName.isalpha():
    print('Please enter only alphabets for username')
else:
    askingPassword = input('Enter your password: ')
    
    # Check if password contains only numbers
    if not askingPassword.isdigit():
        print('Please enter only numbers for password')
    else:
        # Only save if both are valid
        with open("password.txt", "a") as file:
            file.write(askingUserName + ' : ' + askingPassword + '\n')
        print('Username and password saved successfully!')