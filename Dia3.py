########################### DIA 3 #########################################

#Given an integer x, return true if x is a palindrome, and false otherwise.

def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if  x < 0:
            return False

        reverse = 0;
        num = x;

        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            x //= 10
        
        return reverse == num
        return reverse == num