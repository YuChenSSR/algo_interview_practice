"""
Easy Level Interview Problems

Collection of fundamental interview problems that test basic understanding
of data structures and algorithms.
"""

from typing import List, Optional


def valid_parentheses(s: str) -> bool:
    """
    Problem: Valid Parentheses
    
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.
    
    Example:
    - "()" -> True
    - "()[]{}" -> True
    - "(]" -> False
    - "([)]" -> False
    
    Time: O(n), Space: O(n)
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    
    return not stack


def reverse_integer(x: int) -> int:
    """
    Problem: Reverse Integer
    
    Given a signed 32-bit integer x, return x with its digits reversed.
    If reversing x causes the value to go outside [-2^31, 2^31-1], return 0.
    
    Example:
    - 123 -> 321
    - -123 -> -321
    - 120 -> 21
    
    Time: O(log x), Space: O(1)
    """
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    
    result = 0
    sign = -1 if x < 0 else 1
    x = abs(x)
    
    while x:
        digit = x % 10
        x //= 10
        
        # Check for overflow before updating result
        if result > (INT_MAX - digit) // 10:
            return 0
        
        result = result * 10 + digit
    
    result *= sign
    return result if INT_MIN <= result <= INT_MAX else 0


def palindrome_number(x: int) -> bool:
    """
    Problem: Palindrome Number
    
    Given an integer x, return true if x is palindrome integer.
    
    Example:
    - 121 -> True
    - -121 -> False
    - 10 -> False
    
    Time: O(log x), Space: O(1)
    """
    if x < 0:
        return False
    
    original = x
    reversed_num = 0
    
    while x > 0:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10
    
    return original == reversed_num


def remove_duplicates_sorted_array(nums: List[int]) -> int:
    """
    Problem: Remove Duplicates from Sorted Array
    
    Given an integer array nums sorted in non-decreasing order,
    remove duplicates in-place such that each unique element appears only once.
    
    Example:
    - [1,1,2] -> 2, nums = [1,2,_]
    - [0,0,1,1,1,2,2,3,3,4] -> 5, nums = [0,1,2,3,4,_,_,_,_,_]
    
    Time: O(n), Space: O(1)
    """
    if not nums:
        return 0
    
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    
    return slow + 1


def merge_two_sorted_lists_problem(list1: Optional['ListNode'], list2: Optional['ListNode']) -> Optional['ListNode']:
    """
    Problem: Merge Two Sorted Lists
    
    You are given the heads of two sorted linked lists list1 and list2.
    Merge the two lists in a one sorted list.
    
    Time: O(n + m), Space: O(1)
    """
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
    
    current.next = list1 or list2
    return dummy.next


def maximum_depth_binary_tree(root: Optional['TreeNode']) -> int:
    """
    Problem: Maximum Depth of Binary Tree
    
    Given the root of a binary tree, return its maximum depth.
    
    Time: O(n), Space: O(h) where h is height of tree
    """
    if not root:
        return 0
    
    return 1 + max(maximum_depth_binary_tree(root.left), 
                   maximum_depth_binary_tree(root.right))


def best_time_to_buy_and_sell_stock(prices: List[int]) -> int:
    """
    Problem: Best Time to Buy and Sell Stock
    
    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock 
    and choosing a different day in the future to sell that stock.
    
    Return the maximum profit you can achieve from this transaction.
    
    Example:
    - [7,1,5,3,6,4] -> 5 (buy at 1, sell at 6)
    - [7,6,4,3,1] -> 0 (no profit possible)
    
    Time: O(n), Space: O(1)
    """
    if not prices:
        return 0
    
    min_price = prices[0]
    max_profit = 0
    
    for price in prices[1:]:
        # Update minimum price seen so far
        min_price = min(min_price, price)
        # Update maximum profit
        max_profit = max(max_profit, price - min_price)
    
    return max_profit


def contains_duplicate(nums: List[int]) -> bool:
    """
    Problem: Contains Duplicate
    
    Given an integer array nums, return true if any value appears 
    at least twice in the array.
    
    Example:
    - [1,2,3,1] -> True
    - [1,2,3,4] -> False
    
    Time: O(n), Space: O(n)
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


def valid_anagram(s: str, t: str) -> bool:
    """
    Problem: Valid Anagram
    
    Given two strings s and t, return true if t is an anagram of s.
    
    Example:
    - "anagram", "nagaram" -> True
    - "rat", "car" -> False
    
    Time: O(n), Space: O(1) assuming only lowercase letters
    """
    if len(s) != len(t):
        return False
    
    char_count = {}
    
    # Count characters in first string
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Decrement count for characters in second string
    for char in t:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] == 0:
            del char_count[char]
    
    return len(char_count) == 0


# Helper classes for linked list and tree problems
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right