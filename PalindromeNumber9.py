class Solution(object):
    def isPalindrome(self, x):
        if x < 0:return False
        if x ==0: return True
        num = []
        while x > 0:
            num.append(x % 10)
            x //= 10
        length = len(num)
        for i in range((length+2) // 2):
            if num[i] != num[length-i-1]:
                return False
        return True

so = Solution()
print(so.isPalindrome(0))