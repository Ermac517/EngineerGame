def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            if stack and stack[-1] == mapping[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return not stack

def main():
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("((()))", True),
        ("((())", False),
        (")(", False),
    ]

    print("Running isValid test cases:\n")

    for i, (s, expected) in enumerate(test_cases, 1):
        result = isValid(s)
        status = "✓ PASS" if result == expected else f"✗ FAIL (expected {expected}, got {result})"
        print(f"Test {i}: s='{s}'")
        print(f"  Result: {result} - {status}\n")

if __name__ == "__main__":
    main()