from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
  def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    i = 0
    start_dummy = ListNode(None, head)
    left_limit = start_dummy
    if not head.next:
      return head
    while i < left - 1:
      left_limit = left_limit.next
      i += 1
    start_node = left_limit.next
    while i < right - 1:
      next_node = start_node.next
      start_node.next = next_node.next
      next_node.next = left_limit.next
      left_limit.next = next_node
      i += 1
    return start_dummy.next
      

param = [1,2,3,4,5]
node_before = None
for i in range(len(param) - 1, -1, -1):
  if i == len(param) -1:
    node_before = ListNode(param[i], None)
  node_before = ListNode(param[i], node_before)

the_head = Solution().reverseBetween(node_before, 2, 4)
