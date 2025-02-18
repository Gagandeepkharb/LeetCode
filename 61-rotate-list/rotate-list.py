class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0:
            return head
        
        # Step 1: Find the length of the list and the last node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # Step 2: Normalize k
        k %= length
        if k == 0:
            return head
        
        # Step 3: Make the list circular
        tail.next = head
        
        # Step 4: Find the new tail (length - k % length - 1) and the new head
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head
