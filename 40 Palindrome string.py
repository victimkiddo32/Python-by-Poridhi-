def isPalindrome(s: str, left: int, right: int):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return isPalindrome(s, left + 1, right - 1)

def checkPalindrome(s: str):
    is_pal = isPalindrome(s, 0, len(s) - 1)
    print(f"{s} is palindrome : {is_pal}")

# Example usage
checkPalindrome("madam")
checkPalindrome("hello")