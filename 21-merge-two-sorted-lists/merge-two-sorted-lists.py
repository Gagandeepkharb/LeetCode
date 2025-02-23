class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()  # Dummy node
        current = dummy  # Pointer to track merged list

        while list1 and list2:  # Loop while both lists have nodes
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next  # Move pointer forward

        current.next = list1 if list1 else list2  # Attach remaining nodes

        return dummy.next  # Return head of merged list
