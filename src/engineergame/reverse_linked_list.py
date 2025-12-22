from typing import Optional, List


class ListNode:
    """Node in a singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverse a doubly linked list.

    Args:
        head: Head of the singly linked list.

    Returns:
        Head of the reversed singly linked list.
    """
    current = head
    new_head = None

    while current:
        next_node = current.next
        current.next = new_head
        new_head = current
        current = next_node
    return new_head

def create_linked_list(values: List[int]) -> Optional[ListNode]:
    """Helper: Create a linked list from a list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    """Helper: Convert linked list to Python list for easy comparison."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def reverseList_debug(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverse a singly linked list with detailed debug output.

    Args:
        head: Head of the singly linked list.

    Returns:
        Head of the reversed singly linked list.
    """
    current = head
    new_head = None
    iteration = 0

    print("  Initial state:")
    print(f"    current = {current.val if current else None}")
    print(f"    new_head = None")
    print()

    while current:
        iteration += 1
        print(f"  ╔═══ Iteration {iteration} ═══╗")
        print(f"  ║ BEFORE operations:")
        print(f"  ║   current.val = {current.val}")
        print(f"  ║   current.next = {current.next.val if current.next else None}")
        print(f"  ║   new_head = {new_head.val if new_head else None}")
        print(f"  ║")
        
        # Step 1: Save the next node
        next_node = current.next
        print(f"  ║ Step 1: Save next_node = {next_node.val if next_node else None}")
        
        # Step 2: Reverse the pointer
        current.next = new_head
        print(f"  ║ Step 2: Reverse pointer - current.next = {new_head.val if new_head else None}")
        
        # Step 3: Move new_head forward
        new_head = current
        print(f"  ║ Step 3: Move new_head = {new_head.val}")
        
        # Step 4: Move current forward
        current = next_node
        print(f"  ║ Step 4: Move current = {current.val if current else None}")
        print(f"  ╚═══════════════════╝")
        print()

    print(f"  ✓ Final new_head = {new_head.val if new_head else None}")
    print()
    return new_head


def print_list_structure(head: Optional[ListNode], label: str):
    """Helper: Print visual structure of linked list."""
    if not head:
        print(f"{label}: (empty)")
        return
    
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    
    print(f"{label}: {' → '.join(values)} → None")


def main():
    """Run test cases for reverseList function."""
    print("=" * 70)
    print("DETAILED ITERATION WALKTHROUGH: Reversing [1, 2, 3, 4]")
    print("=" * 70)
    print()
    
    debug_head = create_linked_list([1, 2, 3, 4])
    print_list_structure(debug_head, "Original")
    print()
    
    debug_result = reverseList_debug(debug_head)
    print_list_structure(debug_result, "Reversed")
    print()
    
    print("=" * 70)
    print("RUNNING STANDARD TEST CASES")
    print("=" * 70)
    print()
    
    test_cases = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], "Standard case"),
        ([], [], "Empty list"),
        ([1], [1], "Single element list"),
        ([1, 2], [2, 1], "Two element list"),
        ([1, 1, 1], [1, 1, 1], "All elements same"),
    ]
    
    for i, (input_list, expected_list, description) in enumerate(test_cases, 1):
        head = create_linked_list(input_list)
        reversed_head = reverseList(head)
        result = linked_list_to_list(reversed_head)
        status = "✓ PASS" if result == expected_list else f"✗ FAIL (expected {expected_list}, got {result})"
        print(f"Test {i}: {description}")
        print(f"  Input: {input_list}")
        print(f"  Result: {result} - {status}\n")

if __name__ == "__main__":
    main()