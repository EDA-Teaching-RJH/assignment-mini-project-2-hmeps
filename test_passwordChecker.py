import unittest # for testing the code
from passwordChecker import PasswordStrengthChecker #import the original class

class testPasswordChecker(unittest.TestCase):
    def test_password_strength(self):
        # for all the weak passwords
        weak = PasswordStrengthChecker("12345")
        weak.calculate_strength()
        self.assertEqual(weak.find_strength(), "Weak!")
        # for all the medium passwords
        medium = PasswordStrengthChecker("UniOfKent10")
        medium.calculate_strength()
        self.assertEqual(medium.find_strength(), "Medium!")
        # for all the strong passwords
        strong = PasswordStrengthChecker("StudentAtKentUNI1?")
        strong.calculate_strength()
        self.assertEqual(strong.find_strength(), "Strong!")

if __name__ == "__main__":
    unittest.main()