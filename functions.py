
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
#6
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        current = dummy
     
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
      
        if list1:
            current.next = list1
        if list2:
            current.next = list2
            
        return dummy.next

#7
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = []
        for num in nums:
            if num not in l: 
                l.append(num)        
        for i in range(len(l)):
            nums[i] = l[i]
        
        return len(l) 
#dictioneries
grades = {
    'ali': 93,
    'reza': 44,
    'nika': 77,
    'jamshid': 34,
    'taraneh': 96,
    'parham': 50
}

def tops(grades):
    names = []
    for key, value in grades.items(): 
        if value >= 80:
            names.append(key)
    return names  

    
#8
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        n, m = len(haystack), len(needle)
        if m > n:
            return -1
        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i
        return -1
#9
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return i
        return len(nums)

#10
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        s = s[::-1]
        counter = 0
        for ch in s:
            if ch == ' ':
                return counter
            counter += 1
        return counter

#11
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(map(str, digits)))
        num += 1
        return list(map(int, str(num)))
#12
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        r = x
        while r * r > x:
            r = (r + x // r) // 2
        return r
#13 i used dynamic programming to solve this problem
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        
        memo = [0] * (n + 1)
        memo[0] = 1 
        memo[1] = 1 
        
        for i in range(2, n + 1):
            memo[i] = memo[i-1] + memo[i-2]
        
        return memo[n]
#14
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        tmp = head
        while tmp and tmp.next:  
            if tmp.val == tmp.next.val:  
                tmp.next = tmp.next.next  
            else:
                tmp = tmp.next  
        return head
