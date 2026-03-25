
from passwordChecker import PasswordStrengthChecker
while True:    
    password = input("Enter a suitable password that must include:\n-An uppercase letter!\n-A number!\n-A lowercase letter!\n-A special character!\nEnter Here: ")
# Long line only includes all the conditions that need to be met    
    passwordChecker = PasswordStrengthChecker(password)
    
    if passwordChecker.is_strong():
        print("This password is incredibly strong, and is very unlikely to be broken!")
        print("------------------------------------------------------------------------")
        break
    else:
        print("This password is missing requirements! It must include:")

        if len(password) <12:
            print("- At least 12 Characters!!")
        if not passwordChecker.true_uppercase():
            print("- An uppercase letter!")
        if not passwordChecker.true_number():
            print("- A number!")
        if not passwordChecker.true_lowercase():
            print("- A lowercase letter!")
        if not passwordChecker.true_specialchar():
            print("- A special character!")
"""
While loop makes sure that the program doesnt completely stop once a password below the required 12 characters is inputted, will 
continue to ask for the password until this requirement is met. Made into a nice format that allows the user to see exactly what
the password needs to include
"""
