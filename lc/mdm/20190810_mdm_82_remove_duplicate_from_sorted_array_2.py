#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode("dummy")
        dummy.next = head
        curr = head
        prev = dummy
        prepre = None
        while curr:
            if curr.val == prev.val:
                # skip til to new value
                temp = curr
                curr = curr.next
                while curr:
                    if curr.val != temp.val:
                        break
                    curr = curr.next
                prev = prepre
                prepre.next = curr

            else:
                prepre = prev
                prev = curr
                curr = curr.next
        return dummy.next

def nodeToString(node: ListNode):
    stack = []
    while node:
        stack.append(node.val)
        node = node.next
    return "->".join([str(x) for x in stack])

root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(3)
root.next.next.next.next = ListNode(4)
root.next.next.next.next.next = ListNode(4)
root.next.next.next.next.next.next = ListNode(5)


print(nodeToString(root))
ans = Solution().deleteDuplicates(root)
print(nodeToString(ans))


root = ListNode(1)
root.next = ListNode(1)
root.next.next = ListNode(1)
root.next.next.next = ListNode(2)
root.next.next.next.next = ListNode(3)

print(nodeToString(root))
ans = Solution().deleteDuplicates(root)
print(nodeToString(ans))