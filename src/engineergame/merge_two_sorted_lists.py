from typing import Optional, List


class ListNode:
    """Node in a singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """Merge two sorted linked lists into one sorted list.
    
    Args:
        list1: Head of first sorted linked list
        list2: Head of second sorted linked list
    
    Returns:
        Head of merged sorted linked list
    """
    if not list1:
        return list2
    if not list2:
        return list1

    if list1.val < list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2


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


def main():
    """Run test cases for mergeTwoLists function."""
    test_cases = [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4], "Merge two sorted lists"),
        ([], [], [], "Both lists empty"),
        ([], [0], [0], "First list empty"),
        ([1, 2, 3], [], [1, 2, 3], "Second list empty"),
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6], "Interleaved values"),
        ([5], [1, 2, 4], [1, 2, 4, 5], "First list single element"),
        ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6], "No overlap, first < second"),
        ([4, 5, 6], [1, 2, 3], [1, 2, 3, 4, 5, 6], "No overlap, second < first"),
    ]
    
    print("Running mergeTwoLists test cases:\n")
    
    for i, (list1_vals, list2_vals, expected, description) in enumerate(test_cases, 1):
        list1 = create_linked_list(list1_vals)
        list2 = create_linked_list(list2_vals)
        
        merged = mergeTwoLists(list1, list2)
        result = linked_list_to_list(merged)
        
        status = "✓ PASS" if result == expected else f"✗ FAIL (expected {expected}, got {result})"
        print(f"Test {i}: {description}")
        print(f"  List1: {list1_vals}")
        print(f"  List2: {list2_vals}")
        print(f"  Result: {result} - {status}\n")


if __name__ == "__main__":
    main()