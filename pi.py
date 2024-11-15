#! /home/ajw/Documents/csc24_notes/.venv/bin/python

"""
Challenge: Decode a hidden message encrypted within the digits of Pi.

Description:
The digits of Pi contain an infinite sequence of numbers. The flag for this
challenge has been cleverly encrypted and hidden in the decimal expansion
of Pi. The task is to decode the flag from its numerical disguise.

Ciphertext: 
[95, 568, 6, 38, 69, 10, 86, 170, 29, 95, 86, 170, 65, 604, 29,
 17, 138, 47, 29, 83, 56, 29, 138, 56, 604, 604, 47, 65, 29, 95,
 568, 171, 38, 23, 1]

Flag Format: FLAG(decrypted_message)
"""

from mpmath import mp

# Set the precision for Pi to 1000 decimal places
mp.dps = 1000
pi = str(mp.pi)  # Get Pi as a string

# Ciphertext to be decrypted
ciphertext = [95, 568, 6, 38, 69, 10, 86, 170, 29, 95, 86, 170, 65, 604, 29,
              17, 138, 47, 29, 83, 56, 29, 138, 56, 604, 604, 47, 65, 29, 95,
              568, 171, 38, 23, 1]

# Decrypt the ciphertext using the digits of Pi
def decrypt_message(ciphertext, pi_digits):
    """
    Decrypts the ciphertext by extracting specific segments of Pi's digits.
    
    Args:
        ciphertext (list): A list of numerical indices pointing to Pi's digits.
        pi_digits (str): The decimal expansion of Pi as a string.

    Returns:
        str: The decrypted message.
    """
    decrypted_chars = []
    for cipher in ciphertext:
        # Extract two digits starting at the (cipher + 2)-th position of Pi
        extracted_digits = pi_digits[cipher + 2:cipher + 4]
        # Convert the extracted digits to a character
        decrypted_chars.append(chr(int(extracted_digits)))
    return ''.join(decrypted_chars)

# Decrypt the ciphertext
decrypted_message = decrypt_message(ciphertext, pi)

# Print the decrypted message in the specified format
print(decrypted_message)
