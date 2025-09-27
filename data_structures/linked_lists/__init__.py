"""
Linked List Data Structures

Implementation of various linked list types commonly used in interviews.
"""

from typing import Optional, Any


class ListNode:
    """Node for singly linked list."""
    
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next
    
    def __repr__(self) -> str:
        return f"ListNode({self.val})"


class SinglyLinkedList:
    """
    Singly Linked List implementation.
    
    Time Complexities:
    - Access: O(n)
    - Search: O(n)
    - Insertion: O(1) at head, O(n) at position
    - Deletion: O(1) at head, O(n) at position
    """
    
    def __init__(self):
        self.head: Optional[ListNode] = None
        self.size = 0
    
    def __len__(self) -> int:
        return self.size
    
    def append(self, val: int) -> None:
        """Add node at end of list. O(n)."""
        new_node = ListNode(val)
        
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
        self.size += 1
    
    def prepend(self, val: int) -> None:
        """Add node at beginning of list. O(1)."""
        new_node = ListNode(val, self.head)
        self.head = new_node
        self.size += 1
    
    def insert(self, index: int, val: int) -> None:
        """Insert node at specific index. O(n)."""
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        
        if index == 0:
            self.prepend(val)
            return
        
        current = self.head
        for _ in range(index - 1):
            current = current.next
        
        new_node = ListNode(val, current.next)
        current.next = new_node
        self.size += 1
    
    def delete(self, index: int) -> int:
        """Delete node at index and return its value. O(n)."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        
        if index == 0:
            val = self.head.val
            self.head = self.head.next
            self.size -= 1
            return val
        
        current = self.head
        for _ in range(index - 1):
            current = current.next
        
        val = current.next.val
        current.next = current.next.next
        self.size -= 1
        return val
    
    def find(self, val: int) -> int:
        """Find first occurrence of value. O(n)."""
        current = self.head
        index = 0
        
        while current:
            if current.val == val:
                return index
            current = current.next
            index += 1
        
        return -1
    
    def to_list(self) -> list:
        """Convert to Python list for easy visualization."""
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result


class DoublyListNode:
    """Node for doubly linked list."""
    
    def __init__(self, val: int = 0, 
                 prev: Optional['DoublyListNode'] = None,
                 next: Optional['DoublyListNode'] = None):
        self.val = val
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    """
    Doubly Linked List implementation.
    
    Time Complexities:
    - Access: O(n)
    - Search: O(n)
    - Insertion: O(1) at head/tail, O(n) at position
    - Deletion: O(1) at head/tail, O(n) at position
    """
    
    def __init__(self):
        self.head: Optional[DoublyListNode] = None
        self.tail: Optional[DoublyListNode] = None
        self.size = 0
    
    def append(self, val: int) -> None:
        """Add node at end. O(1)."""
        new_node = DoublyListNode(val)
        
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
    
    def prepend(self, val: int) -> None:
        """Add node at beginning. O(1)."""
        new_node = DoublyListNode(val)
        
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.size += 1
    
    def delete_node(self, node: DoublyListNode) -> None:
        """Delete specific node. O(1) if node reference is given."""
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        
        self.size -= 1


# Common Linked List Problems

def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse a singly linked list.
    
    Time: O(n), Space: O(1)
    """
    prev = None
    current = head
    
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    
    return prev


def find_middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Find middle node using slow/fast pointer technique.
    
    Time: O(n), Space: O(1)
    """
    if not head:
        return None
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow


def has_cycle(head: Optional[ListNode]) -> bool:
    """
    Detect if linked list has a cycle (Floyd's Cycle Detection).
    
    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return False
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False


def merge_two_sorted_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Merge two sorted linked lists.
    
    Time: O(m + n), Space: O(1)
    """
    dummy = ListNode(0)
    current = dummy
    
    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    # Attach remaining nodes
    current.next = l1 or l2
    
    return dummy.next