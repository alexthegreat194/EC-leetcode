from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list_len = 0
        start = head
        while start is not None:
            start = start.next
            list_len += 1
            
        current = head
        for i in range(int(list_len/2)):
            current = current.next
        
        return current