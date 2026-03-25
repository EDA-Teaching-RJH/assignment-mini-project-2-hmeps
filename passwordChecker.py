class PasswordStrengthChecker:
    def __init__(self, password):
        self.password = password
    def check_length(self):
        if len(self.password) >= 12:
            return "Perfect Length!"
        else:
            return "Too Short, likely to be compromised!"
    
"""
Set multiple lengths of self.password so that it provides feeback even if it is theoretically long enough to be a good password
you should still try and get a better length password
"""