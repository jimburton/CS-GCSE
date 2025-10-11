from string import ascii_lowercase, ascii_uppercase

def enc_ceasar(key, text):
    enc = ""
    for c in text:
        enc += chr(ord(c)+key)
    return enc

def dec_ceasar(key, text):
    dec = ""
    for c in text:
        dec += chr(ord(c)-key)
    return dec

def rot13(text):
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
