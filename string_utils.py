'''A simple string utility module.'''

def reverse_string(s):
  """Reverses a string."""
  return s[::-1]

def is_palindrome(s):
  """Checks if a string is a palindrome."""
  return s == s[::-1]
