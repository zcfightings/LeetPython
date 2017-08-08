class Solution(object):
    def myAtoi(self, str):
        if not str or  len(str) == 0:
            return 0
        str = str.strip().split(' ')[0]
        if str[0] =='+' :
            return self.myAtoi2(str[1:],False)
        if str[0] == '-':
            return self.myAtoi2(str[1:],True)
        if str[0] == '0':
            return self.myAtoi2(str[1:],False)
        return self.myAtoi2(str,False)

    def myAtoi2(self,str,flag):
        result = 0
        start = ord('0')
        for c in str:
            if c==' ':
                continue
            if (c < '0' or c > '9') :
                break;
            result = result * 10 + (ord(c) - start)
        if flag:
            result *= -1
        if result > 2147483647:
            result = 2147483647
        if result < -2147483648:
            result = -2147483648
        return result

so = Solution()
print(so.myAtoi("-2147483648"))
