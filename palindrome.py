class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Step1: Clean the string of any non-alnum characters and convert it to lower case
        s_cleaned=''.join(c.lower() for c in s if c.isalnum())
        s_reverse=s_cleaned[::-1]
        if s_cleaned == s_reverse:
            return True
        else:
            return False