# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        sizeA = self.__get_size__(headA)
        sizeB = self.__get_size__(headB)

        if(sizeA > sizeB):
            while(sizeA > sizeB):
                if headA is None:
                    return None
                headA = headA.next
                sizeA -= 1
        else:
            while(sizeB > sizeA):
                if headB is None:
                    return None
                headB = headB.next
                sizeB -= 1
        
        while(headA != headB):
            if headA is None or headB is None:
                return None
            headA = headA.next
            headB = headB.next
    

        return headA


    def __get_size__(self, head):
        
        if head is None:
            return 0

        size = 1

        while(head.next is not None):
            head = head.next
            size += 1

        return size
