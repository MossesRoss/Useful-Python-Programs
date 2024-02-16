def caesar_cipher(text, shift):
  """
  Encrypts or decrypts a message using the Caesar Cipher.

  Args:
    text: The message to encrypt or decrypt.
    shift: The number of positions to shift letters (positive for encrypt, negative for decrypt).

  Returns:
    The encrypted or decrypted message.
  """

  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  shifted_alphabet = alphabet[shift:] + alphabet[:shift]
  new_text = ''

  for char in text:
    if char.isalpha():
      index = alphabet.find(char.lower())
      new_letter = shifted_alphabet[index]
      new_text += new_letter.upper() if char.isupper() else new_letter.lower()
    else:
      new_text += char

  return new_text

# Encrypt the message with a shift of 6
encrypted_text = caesar_cipher("SECRET MEETING AT THE PALACE", 6)
print("Encrypted message:", encrypted_text)  # Output: YKIXKZ SKKZOTM GZ ZNK VGRGIK

# Decrypt the encrypted text with a shift of -6
decrypted_text = caesar_cipher(encrypted_text, -6)
print("Decrypted message:", decrypted_text)  # Output: SECRET MEETING AT THE PALACE
