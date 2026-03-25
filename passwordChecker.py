import re
class PasswordStrengthChecker:
    def __init__(self, password):
        self.password = password
        self.score = 0
#Adding a scoring method to make the password strength into a game
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
            len(self.password) >=10 and
            self.true_uppercase() and
            self.true_number() and
            self.true_lowercase() and
            self.true_specialchar() and
            not self.weak_patterns_true()
        )
    """
Created a strong password checker that uses all conditions that a regular password checker would use
like uppercase, special characters and numbers using the very useful regex library
    """
    def calculate_strength(self):
        if len(self.password) >=10:
            self.score +=1
        if len(self.password) >=12:
            self.score += 2
        if len(self.password) >=15:
            self.score += 3
        if self.true_uppercase():
            self.score += 2
        if self.true_number():
            self.score += 1
        if self.true_lowercase():
            self.score +=1
        if self.true_specialchar():
            self.score += 3
        if self.weak_patterns_true():
            self.score -=2
        if self.common_patterns_true():
            self.score -=4
        return self.score
    """
The score checker adds a game sense to the regular password checker so that it encourages the user to create stronger and hence safer passwords
to protect their devices and accounts from potential hacks or data leaks.
    """
    def find_strength(self):
        if self.score <=4:
            return "Really Weak!"
        elif self.score <= 6:
            return "Medium Level Strength!"
        elif self.score <=8:
            return "Quite Strong!"
        else:
            return "Incredibly Strong!"
    """
This provides extra information on what score the user shoud be aiming for and provides feedback so that they know what characters make
a password really strong and difficult to be leaked or broken!
    """
    def weak_patterns_true(self):
        checks = [
            re.search(r"\s", self.password), # no whitespace
            re.search(r"(.)\1{2,}", self.password), # no single character patterns
            re.search(r"(..)\1", self.password), # no alternating patterns
            re.search(r"\d{10,}", self.password), # longer than 10 characters
        ]
        return any(checks)
# Using regex to stop any common passwords or repetitions in passwords to make them stronger
    def common_patterns_true(self):
        patterns = [
            "12345",
            "abcde",
            "ABCDE",
            "password",
            "Password"
        ]
        for i in patterns:
            if i in self.password.lower():
                return True
        return False
    """
Trying to catch any possile really common and easy passwords that may slip under the code and are able to be used
so that the password that is allowed is truly the strongest it could be.
    """
    def obtain_feedback(self):
        feedback = []

        if len(self.password) <10:
            feedback.append("Password chosen is too Short!")
        if not self.true_uppercase():
            feedback.append("Add uppercase letters!")
        if not self.true_number():
            feedback.append("Add numbers!")
        if not self.true_lowercase():
            feedback.append("Add lowercase letters!")
        if not self.true_specialchar():
            feedback.append("Add special characters!")
        if self.weak_patterns_true():
            feedback.append("Avoid adding weak patterns into your chosen Password!")
        if self.common_patterns_true():
            feedback.append("Avoid Common Patterns, e.g'Password'!")

        return feedback
    """
Creating a feedback list so that the issues with the code can be added to the list and outputted to the user with clear instructions
and so that the code remembers what previous issues with the password were so the warnings arent repeated
    """