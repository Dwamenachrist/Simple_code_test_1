def concatenate_strings(a: str, b: str) -> str:
    """
    Concatenates two strings.
    Does not explicitly handle non-string inputs.
    """
    return a + b

def get_string_length(s: str) -> int:
    """
    Returns the length of a string.
    Does not explicitly handle non-string inputs.
    """
    return len(s)

def split_string(s: str, delimiter: str) -> list:
    """
    Splits a string by a delimiter.
    Does not explicitly handle non-string inputs or invalid delimiters.
    """
    return s.split(delimiter)
