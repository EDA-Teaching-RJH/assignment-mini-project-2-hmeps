import re
from passwordChecker import PasswordStrengthChecker
password = input("Enter a suitable password: ")

passwordChecker = PasswordStrengthChecker(password)
print(passwordChecker.check_length())