# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

class Solution:
    def reorderList(self, head: ListNode):
        if not head or not head.next:
            return head

        # Step 1: Find the middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half
        prev, curr = None, slow.next
        slow.next = None   # cut the list into two halves
        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode

        # Step 3: Merge two halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

#main code
arr = list(map(int, input().split()))
head = ListNode(arr[0])
tail = head
for i in range(1, len(arr)):
    temp = ListNode(arr[i])
    tail.next = temp
    tail = temp

sol = Solution()
sol.reorderList(head)

def printlist(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

printlist(head)
