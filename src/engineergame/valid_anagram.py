def isAnagram(s: str, t: str) -> bool:
    """Check if two strings are anagrams of each other. 
        An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
        Args:
            s: First string
            t: Second string
        Returns:
        True if s and t are anagrams, False otherwise
    """
    if len(s) != len(t):
        return False
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1
    return True

def main():
    """Run test cases for isAnagram function."""
    test_cases = [
        ("listen", "silent", True),
        ("triangle", "integral", True),
        ("apple", "pale", False),
        ("rat", "car", False),
        ("aabbcc", "abcabc", True),
        ("abcd", "dcba", True),
        ("hello", "billion", False),
        ("anagram", "nagaram", True),
        ("", "", True),
        ("a", "a", True),
        ("a", "b", False),
    ]
    
    print("Running isAnagram test cases:\n")
    
    for i, (s, t, expected) in enumerate(test_cases, 1):
        result = isAnagram(s, t)
        status = "✓ PASS" if result == expected else f"✗ FAIL (expected {expected}, got {result})"
        print(f"Test {i}: s='{s}', t='{t}'")
        print(f"  Result: {result} - {status}\n")

if __name__ == "__main__":
    main()




