# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res=ListNode()
        pointres=res
        point=head
        total=0
        while point.next != None:
            if point.val!=0:
                total+=point.val
            else:
                pointres.val=total
                pointres.next=ListNode()
                pointres=pointres.next
                total=0
            point=point.next
        pointres.val=total
        return res.next