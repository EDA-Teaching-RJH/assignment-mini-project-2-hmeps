import re
class PasswordStrengthChecker:
    def __init__(self, password):
        self.password = password
# Set the class that will be used to check the password for all possible corrections that could be needed
    def true_uppercase(self):
        return bool(re.search(r"[A-Z]", self.password))
    def true_number(self):
        return bool(re.search(r"[0-9]", self.password))
    def true_lowercase(self):
        return bool(re.search(r"[a-z]", self.password))
    def true_specialchar(self):
        return bool(re.search(r"[!£$%^&*?<>@#|_]", self.password))
    
    def is_strong(self):
        return (
            len(self.password) >=12 and
            self.true_uppercase() and
            self.true_number() and
            self.true_lowercase() and
            self.true_specialchar()
        )
"""
Created a strong password checker that uses all conditions that a regular password checker would use
like uppercase, special characters and numbers using the very useful regex library
"""