
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) <= 0:
            return 0
        last_start = 0
        visit = {s[0]: 0}
        carlen = 1
        max_len = 1
        for i in range(1, len(s)):
            if s[i] not in visit.keys():
                carlen += 1
                visit[s[i]] = i
            else:
                if last_start <= visit[s[i]]:
                    carlen = i - visit[s[i]]
                    last_start = visit[s[i]] + 1
                    visit[s[i]] = i
                else:
                    carlen += 1
                    visit[s[i]] = i
            max_len = carlen if (carlen > max_len) else max_len
        return max_len


so = Solution()
len = so.lengthOfLongestSubstring("qwnfenpglqdq")
print(len)
