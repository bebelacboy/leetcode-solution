from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
  def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
      return None
    start_dummy = ListNode(None, head)
    prev = start_dummy
    current = prev.next
    while current.next:
      next_node = current.next
      current.next = next_node.next
      next_node.next = current
      prev.next = next_node
      prev = current
      if prev.next:
        current = current.next
      if current.next:
        next_node = current.next
      
    return start_dummy.next