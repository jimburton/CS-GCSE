"""Some simplpe ciphers."""
from string import ascii_lowercase, ascii_uppercase

def enc_ceasar(key, text):
    """Encode text with a Caser cipher with a given offset.
    The encoding may include non alpha-numeric ASCII characters."""
    enc = ""
    for c in text:
        enc += chr(ord(c)+key)
    return enc

def dec_ceasar(key, text):
    """Decode a Caesar cipher with a given offset."""
    dec = ""
    for c in text:
        dec += chr(ord(c)-key)
    return dec

def rot13(text):
    """Rot13 is a Caesar cipher with key=13. This means that callibg Rot13
    twice recovers the original text. The encoding transforms lower case
    alphabetic characters to their Rot13 lowercase counterpart, and
    similarly for upper case input. Non alphabetic characters are not
    changed.
    """
    enc = ""
    for c in text:
        c_rot = ''
        if c in ascii_lowercase:
            c_rot = ascii_lowercase[(ascii_lowercase.index(c) + 13) % 26]
        elif c in ascii_uppercase:
            c_rot = ascii_uppercase[(ascii_uppercase.index(c) + 13) % 26]
        else:
            c_rot = c
        enc += c_rot
    return enc
