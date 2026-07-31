class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()

        for i in range((len(newStr))//2):
            if newStr[i] == newStr[len(newStr)-1-i]:
                continue
            else:
                return False
        return True