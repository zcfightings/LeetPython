class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self.kth(nums1,nums2,l // 2)
        else:
            return (self.kth(nums1,nums2,l // 2) + self.kth(nums1,nums2,l//2 - 1)) / 2

    def kth(self,a,b,k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        la, lb = len(a)//2 ,len(b)//2
        va,vb = a[la],b[lb]

        if la+lb < k:
            if va > vb:
                return self.kth(a,b[lb+1:],k-lb-1)
            else:
                return self.kth(a[la+1:],b,k-la-1)
        else:
            if va > vb:
                return self.kth(a[:la],b,k)
            else:
                return self.kth(a,b[:lb],k)

so = Solution()
A=[1,2]
B = [3,4]
l=len(A)+len(B)
print((so.kth(A,B,l // 2) + so.kth(A,B,l//2 - 1)) / 2)








