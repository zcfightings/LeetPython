class ListNode(object):
     def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        head = pre = ListNode(0)
        while l1  or l2  or carry:
            vl2 = vl1 = 0
            if l1:
                vl1 = l1.val
                l1 = l1.next
            if l2:
                vl2 = l2.val
                l2 = l2.next
            carry,vl3 = divmod(vl1 + vl2 + carry , 10)
            cur = ListNode(vl3)
            pre.next = cur
            pre = cur
        return head.next

so = Solution()
l1 = ListNode(5)
l2 = ListNode(5)
l = so.addTwoNumbers(l1,l2)
while(l):
    print(l.val)
    l=l.next






