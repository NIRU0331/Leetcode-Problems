class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        prev = slow.next = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev, curr = curr, tmp
        
        left, right = head, prev
        while right:
            tmp1 = left.next
            tmp2 = right.next
            left.next = right
            right.next = tmp1

            left, right = tmp1, tmp2