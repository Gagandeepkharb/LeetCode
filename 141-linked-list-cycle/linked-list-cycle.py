class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next           # Move slow pointer by one step
            fast = fast.next.next      # Move fast pointer by two steps
            
            if slow == fast:           # If they meet, there's a cycle
                return True
        
        return False                    # If fast pointer reaches None, no cycle
