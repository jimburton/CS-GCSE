"""Some simple ciphers."""
from string import ascii_lowercase, ascii_uppercase

def enc_caesar(key: int, text: str) -> str:
    """Encode/Decode text with a Caesar cipher with a given offset.
    
    To decode a message, supply a key which is the negation of the
    key that was used to encode it.
    
    A Caesar cipher is one of the simplest and most widely 
    known encryption techniques. It is a type of substitution 
    cipher in which each letter in the plaintext is replaced by 
    a letter some fixed number of positions down the alphabet. 
    For example, with a left shift of 3, D would be replaced by A, 
    E would become B, and so on. The method is named after Julius 
    Caesar, who used it in his private correspondence.
    
    Args:
        key (int): The cipher.
        text (str): The message to be encoded.

    Returns:
        str: The encoded message.
    """
    pass

def rot13(text: str) -> str:
    """Rot13 is a Caesar cipher with key=13. This means that calling Rot13
    twice recovers the original text. The encoding transforms the message to
    lower case then transforms alphabetic ASCII characters to their Rot13 
    counterpart. Non alphabetic characters are not changed.
    
    Args:
    text (str): The message to be encoded.

    Returns:
    str: The encoded message.
    """
    enc = ""
    for c in text:
        c_rot = c
        if c in ascii_lowercase:
            c_rot = ascii_lowercase[(ascii_lowercase.index(c) + 13) % len(ascii_lowercase)]
        elif c in ascii_uppercase:
            c_rot = ascii_uppercase[(ascii_uppercase.index(c) + 13) % len(ascii_uppercase)]
        enc += c_rot
    return enc

def vigenere(key: str, text: str, encode: bool=True) -> str:
    """The Vigenère cipher is a method of encrypting alphabetic text 
    where each letter of the plaintext is encoded with a different Caesar 
    cipher, whose increment is determined by the corresponding letter of 
    another text, the key.

    For example, if the plaintext is 'attacking tonight' and the key is 
    'oculorhinolaryngology', then

    the first letter of the plaintext, a, is shifted by 14 positions in the 
    alphabet (because the first letter of the key, o, is the 14th letter of 
    the alphabet, counting from zero), yielding o;
    the second letter, t, is shifted by 2 (because the second letter of the 
    key, c, is the 2nd letter of the alphabet, counting from zero) yielding v;
    the third letter, t, is shifted by 20 (u), yielding n, with wrap-around;
    and so on.

    Args:
        key (str): A string representing the key for the cipher.
        text (str): The message to be encoded or decoded.
        encode (bool): True (the default) means encode, False means decode.

    Returns:
        str: The encoded/decoded message.
    """
    enc = ""
    if encode:
        for i,c in enumerate(text):
            cipher = ord(key[i % len(key)])
            enc += chr(ord(c) + cipher % len(key))
        return enc
    else:
        for i,c in enumerate(text):
            cipher = ord(key[i % len(key)])
            enc += chr(ord(c) - cipher % len(key))
        return enc

def test_caesar():
    """ Test the enc_caesar function. """
    secret = 'We attack tonight at midnight. Bring sandwiches!'
    enc = enc_caesar(7, secret)
    assert(secret == enc_caesar(-7, enc))
    
def test_rot13():
    """ Test the rot13 function. """
    secret = """Oh, I do like to be beside the seaside, oh I do
    like to be beside the sea;
    Oh I do like to stroll along the prom, prom, prom, Where the brass bands 
    play, tiddly-om-pom-pom."""
    assert(secret == rot13(rot13(secret)))
    
def test_vigenere():
    """ Test the vigenere function. """
    key = 'lklkldv'
    secret = """Hey! That's no way to say goodbye."""
    enc = vigenere(key, secret, encode=True)
    assert(secret == vigenere(key, enc, encode=False))