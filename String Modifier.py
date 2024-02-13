def replace_chars(string):
  """Replaces all "a"s with "*" and all "z"s with "x" in a string.

  Args:
    string: The string to be modified.

  Returns:
    The modified string with "a"s replaced by "*" and "z"s replaced by "x".
  """

  new_string = ""
  for char in string:
    if char == "a":
      new_string += "*"
    elif char == "z":
      new_string += "x"
    else:
      new_string += char
  return new_string

# Example usage
string = "This is a test string with some a's and z's."
modified_string = replace_chars(string)
print(modified_string)
