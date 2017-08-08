import sys
class Solution(object):
    def reverse(self, x):
        flag = 1
        if x < 0:
            x *= -1
            flag = -1
        result = 0
        while x != 0:
            tail = x % 10
            result = result * 10 + tail
            if result * flag < -2147483648  or result *flag > 1534236469:
                return 0
            x //= 10
        if flag == -1:
            result *= -1
        return result

so = Solution()
print(so.reverse(1463847412))



