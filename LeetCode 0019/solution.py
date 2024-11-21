# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        new_head_node = ListNode()
        new_head_node.next = head 
        behind_node = new_head_node
 
        nth_node = head

        i = 1
        while head:
            if i > n:
                behind_node = nth_node
                nth_node = nth_node.next

            head = head.next
            i += 1

        behind_node.next = nth_node.next
        
        return new_head_node.next