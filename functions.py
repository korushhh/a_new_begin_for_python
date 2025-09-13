
def odd_or_even(list):
    res = ['even' if n%2==0 else 'odd' for n in list]
    return res
print(odd_or_even([1,2,3,4,5,6,7,9,11,22,44]))

def files_merge(names,l_names,ages):
    for person in zip(names,l_names,ages):
        print(person)
names = ['reza','majid','babak']
l_names = ['golzar','salehi','rahnama']
ages = [48,53,41]

files_merge(names,l_names,ages)
# leet code problems
#1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return res
#2    
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum1 = 0
        place = 1
        p = l1
        while p is not None:
            sum1 += p.val * place
            place *= 10
            p = p.next

        sum2 = 0
        place = 1
        q = l2
        while q is not None:
            sum2 += q.val * place
            place *= 10
            q = q.next

        total = sum1 + sum2
        if total == 0:
            return ListNode(0)

        dummy = ListNode(0)
        cur = dummy
        while total > 0:
            digit = total % 10
            total //= 10
            cur.next = ListNode(digit)
            cur = cur.next

        return dummy.next
    
#3
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        sum = 0
        tmp = x
        while(tmp != 0):
            sum = sum * 10 + (tmp % 10)
            tmp = int(tmp/10)
        return sum == x

#4
class Solution:
    def romanToInt(self, s: str) -> int:
        vals = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        result = 0
        n = len(s)
        for i in range(n):
            if i + 1 < n and vals[s[i]] < vals[s[i + 1]]:
                result -= vals[s[i]]
            else:
                result += vals[s[i]]

        return result

#5
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in pairs.values():
                stack.append(ch)
            elif ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                return False

        return not stack

