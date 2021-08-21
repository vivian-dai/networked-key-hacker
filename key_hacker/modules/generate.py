import random

"""
For generating things
"""

valid_chars = ["A", "B", "C", "D", "E", 
    "F", "G", "H", "I", "J", "K", "L", 
    "M", "N", "O", "P", "Q", "R", "S", 
    "T", "U", "V", "W", "X", "Y", "Z", 
    "a", "b", "c", "d", "e", "f", "g", 
    "h", "i", "j", "k", "l", "m", "n", 
    "o", "p", "q", "r", "s", "t", "u", 
    "v", "w", "x", "y", "z", "0", "1", 
    "2", "3", "4", "5", "6", "7", "8", "9"]

def generate_char():
    """
    Generates a random character

    Returns:
        character: A randomly generated character from the list of valid chars
    """
    return random.choice(valid_chars)

def generate_code(len):
    """
    Generates a code of length len

    Args:
        len (int): size in chars for the code to be

    Returns:
        string: a generated code
    """
    code = ""
    for i in range(len):
        code += generate_char
    return code
