class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = ListNode()
        cur = head

        remind = 0
        while l1 or l2 or remind:
            if l1:
                remind += l1.val
                l1 = l1.next
            if l2:
                remind += l2.val
                l2 = l2.next

            cur.next = ListNode(remind % 10)
            remind //= 10
            cur = cur.next

        return head.next

