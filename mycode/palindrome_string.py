def is_palindrome_string(text):
    reverse = ""

    for char in text:
        reverse = char + reverse

    if text == reverse:
        return True
    else:
        return False