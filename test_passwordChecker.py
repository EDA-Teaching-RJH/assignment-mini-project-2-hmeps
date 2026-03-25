import unittest # for testing the code
from passwordChecker import PasswordStrengthChecker #import the original class

class testPasswordChecker(unittest.TestCase):
    def test_password_strength(self):
        # for all the weak passwords
        weak = PasswordStrengthChecker("12345") #example of weak and common password
        weak.calculate_strength()
        self.assertEqual(weak.find_strength(), "Weak!")
        # for all the medium passwords
        medium = PasswordStrengthChecker("UniOfKent10") #example of medium password
        medium.calculate_strength()
        self.assertEqual(medium.find_strength(), "Medium!")
        # for all the strong passwords
        strong = PasswordStrengthChecker("StudentAtKentUNI1?") #example of strong password
        strong.calculate_strength()
        self.assertEqual(strong.find_strength(), "Strong!")
"""
assertEqual checks whether the two values are equal, e.g weak and Weak, and then based off its findings in the passwordChecker.py file
it returns the test with a True or False so is Boolean logic, so you can easily find out where the issue is and whether the code all lines up
Can catch the assertion error if using a try: and except: logic but there is no need here as the code lined up perfectly fine
"""
if __name__ == "__main__":
    unittest.main()

"""
Calls back to the main fucntion using unittest and returns 'OK' at the end
"""