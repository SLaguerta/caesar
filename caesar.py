# from sys import argv, exit

from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    newText = ""
    for eachChar in text:
        newChars = rotate_character(eachChar, rot)
        newText = newText + newChars
    return newText

# def user_input_is_valid(argv):
#     if len(argv) == 1:
#         # print("usage: python3 caesar.py n")
#         # exit()
#     elif argv[1].isdigit() == False:
#         # print("usage: python3 caesar.py n")
#         # exit()
#     else:
#         #return int(argv[1])
#
# rot = user_input_is_valid(argv)
# text = input("Type a mesage:")
# print(encrypt(text, rot))
