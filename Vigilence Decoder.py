from collections import Counter

def count_letter_frequencies(text):
  """
  Counts the occurrences of each letter in a text.
  """
  letters = [char.lower() for char in text if char.isalpha()]
  return Counter(letters)

def compare_frequencies(cipher_counts, english_counts):
  """
  Compares letter frequency distributions.
  """
  total_diff = 0
  for letter, count in cipher_counts.items():
    expected_count = english_counts[letter]
    total_diff += abs(count - expected_count)
  return total_diff

def guess_keyword_length(text):
  """
  Guesses the keyword length based on frequency analysis.
  """
  cipher_counts = count_letter_frequencies(text)

  # Compare frequencies with expected English distribution
  english_counts = Counter('etaoinshrdlcumfwgypbvkjxqz')
  min_diff = float('inf')
  key_length = 0
  for i in range(1, len(text)//2):
    shifted_counts = cipher_counts.copy()
    for j in range(i):
      shifted_counts[chr((ord(x) - j - 97) % 26 + 97)] += cipher_counts[chr((ord(x) + j - 97) % 26 + 97)]
    diff = compare_frequencies(shifted_counts, english_counts)
    if diff < min_diff:
      min_diff = diff
      key_length = i

  return key_length

# Example usage: assuming you have the ciphertext and known English letter frequencies
ciphertext = "..."
key_length = guess_keyword_length(ciphertext)

# This is just a starting point, further analysis and potentially other approaches
# are needed for full decryption. Remember to use it ethically and responsibly.
