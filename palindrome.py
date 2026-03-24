def is_palindrome(s):
    s_clean = ''.join(ch.lower() for ch in s if ch.isalnum())
    return s_clean == s_clean[::-1]


# Passing a simple word
result1 = is_palindrome("Racecar")
print(f"Is 'Racecar' a palindrome? {result1}")

# Passing a full sentence with punctuation
phrase = "A man, a plan, a canal: Panama"
result2 = is_palindrome(phrase)
print(f"Is the Panama phrase a palindrome? {result2}")

# Passing something that isn't a palindrome
result3 = is_palindrome("Python")
print(f"Is 'Python' a palindrome? {result3}")
