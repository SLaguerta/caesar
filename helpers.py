def alphabet_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter in alphabet:
        position = alphabet.index(letter)
        return position
    elif letter in alphabet2:
        position = alphabet2.index(letter)
        return position
    else:
        return letter

def rotate_character(char, rot):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    charPosition = alphabet_position(char)
    if char in alphabet:
        charPosition = charPosition + rot
        return alphabet[charPosition%26]
    elif char in alphabet2:
        charPosition = charPosition + rot
        return alphabet2[charPosition%26]
    else:
        return char
