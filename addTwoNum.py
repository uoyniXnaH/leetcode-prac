# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    @classmethod
    def numberToArray(_cls, num):
        if num < 10:
            return [num]
        digits = []
        i = 10
        while num % i != num:
            digits.append((num % i) * 10 // i)
            i *= 10
        digits.append(10 * num // i)
        return digits
    
    @classmethod
    def arrayToNode(cls, arr, i):
        if i + 1 == len(arr):
            return ListNode(arr[i], None)
        else:
            return ListNode(arr[i], cls.arrayToNode(arr, i+1))
        
    @classmethod
    def nodeToNumber(cls, node):
        if node.next is None:
            return node.val
        else:
            return node.val + 10 * cls.nodeToNumber(node.next)

    def addTwoNumbers(self, l1, l2):
        n1 = Solution.nodeToNumber(l1)
        n2 = Solution.nodeToNumber(l2)
        return Solution.arrayToNode(Solution.numberToArray(n1 + n2), 0)