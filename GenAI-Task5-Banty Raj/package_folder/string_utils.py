# string_utils.py

def capitalize_words(text):
    """Returns text with each word capitalized."""
   
    return text.title()

def reverse_string(text):
    """Returns the reversed string."""
    
    return text[::-1]

def word_count(text):
    """Returns the number of words in the text."""
   
    return len(text.split())