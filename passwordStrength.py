import json

from passwordChecker import PasswordStrengthChecker
from passwordChecker import generate_strong_passwords
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Hello and welcome to this Password Generator/Creater, make sure you follow the instructions to create the best and safest password for YOU!")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

while True:
    user_choice = str(input("Would you like an automatically generated password? (yes/no): ")).lower().strip()
    if user_choice == "yes":
        password = generate_strong_passwords()
        print(f"Generated Password: {password}")
        passwordChecker = PasswordStrengthChecker(password)
        passwordChecker.calculate_strength()
# all the same code as used below to add the computer generated password to the json data file
        print("Score:", passwordChecker.score)
        print("Strength:", passwordChecker.find_strength())
# add the same json code as earlier written down below, simple copy over but changed it so the data is just within the json implementation
        with open("data/results.json", "a") as f:
            json.dump({
                "Password": password,
                "Score": passwordChecker.score,
                "Strength": passwordChecker.find_strength(),
            }, f)
            f.write("\n")
# now the computer generated password should be in the json data file with all the other passwords generated with their score
# and strength levels alike        
        user_question = str(input("Would you like to also enter your own password? (yes/no): ")).lower().strip()
# to see if user wants to proceed after the computer generated password
        if user_question == "yes":
            pass
        else:
            print("==========================================================")
            print("Thank you for using this program, Program had now Ended!")
            break
    elif user_choice == "no":
        pass
    else:
        print("Please enter a 'yes' OR 'no': ")
        continue
    """
The computer password generator should now flow seamlessly into the manual password entering stage of the program if the user wishes
    """    
    while True:
        print("=======================================================================")
        password = input("Enter a suitable password that must include:\n-At least 10 characters!\n-An uppercase letter!\n-A number!\n-A lowercase letter!\n-A special character!\n||Enter Here: ")
        print("=======================================================================")
# Long line only includes all the conditions that need to be met    
        passwordChecker = PasswordStrengthChecker(password)
    
        if passwordChecker.is_strong():
# Use is_strong as all the conditions are under that function so I only have to call a single function instead of countless different ones!
            print("This password is incredibly strong, and is very unlikely to be broken!")
            print("=======================================================================")
            break
        else:
            print("This password is missing requirements! It must include:")
#Provides a list of all the conditions and the response if they are not met
            if len(password) <10:
                print("- At least 10 Characters!!")
            if not passwordChecker.true_uppercase():
                print("- An uppercase letter!")
            if not passwordChecker.true_number():
                print("- A number!")
            if not passwordChecker.true_lowercase():
                print("- A lowercase letter!")
            if not passwordChecker.true_specialchar():
                print("- A special character!")
            if all:
                print("=======================================================================")
                print("\nFeedback:")
                for f in passwordChecker.obtain_feedback(): # called back into passwordChecker for the obtain.feedback() function
                    print("-", f)
        """
While loop makes sure that the program doesnt completely stop once a password below the required 10 characters is inputted, will 
continue to ask for the password until this requirement is met. Made into a nice format that allows the user to see exactly what
the password needs to include.
        """

    passwordChecker.calculate_strength()
    print("Your Password Score is:", passwordChecker.score)
    print("The strength level of this Password is:", passwordChecker.find_strength())
    print("=======================================================================")
# This prints out the score in a neat and well presented way, that can be easily followed and interacted with


    data = {
        "Password": password,
        "Score": passwordChecker.score,
        "Strength": passwordChecker.find_strength()
        }
# created a dcitionary so that extra information that may need to be collected like username can be stored with the password, score
# and strength if a username input was added.
    with open("data/results.json", "a") as f:
        json.dump(data, f)
        f.write("\n")
    
    """
Using json to open other files to convert python script to json so it can be outputted in a file that stores all inputted passwords
keeping track of their score and how good of a password it is
    """
    break
print("=============================================================")
print("Thank you for saving your Passwords with this program today!")
print("=============================================================")