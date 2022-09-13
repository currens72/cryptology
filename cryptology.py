from pickletools import string1
import string
from typing import Counter
from collections import Counter

#function to manually shift by to decrypt text
def decrypt():
    text = input("Enter shift-by text here: ")
    shift_amount = input("Enter shift amount here: ")
    shift_value = int(shift_amount)
    #creates shifted alphabet
    shifted = alphabet[shift_value:] + alphabet[:shift_value]
    #combines regular and shifted alphabet into table for translation
    translation = str.maketrans(shifted, alphabet)
    print(text.translate(translation))

#function to manually shift by to encrypt text
def encrypt():
    text = input("Enter shift-by text here: ")
    shift_amount = input("Enter shift amount here: ")
    shift_value = int(shift_amount)
    #creates shifted alphabet
    shifted = alphabet[shift_value:] + alphabet[:shift_value]
    #combines regular and shifted alphabet into table for translation
    translation = str.maketrans(alphabet, shifted)
    print(text.translate(translation))

#function used to count letter frequency
def frequency():
    ciphertext = input("Enter cipher text here: ")
    freq = Counter(ciphertext)
    print(freq)

#function used to create new permutated alphabet
def permutate():
    text = input("Enter cipher text here: ")
    newAlphabet = input("Enter new alphabet here (ALL CAPS): ")
    #loop to re-enter the alphabet if it is the incorrect size
    while len(newAlphabet) != 26:
        print("Alphabet contains the wrong amount of characters.")
        newAlphabet = input("Enter new alphabet here (ALL CAPS): ")
    translation = str.maketrans(newAlphabet, alphabet)
    print(text.translate(translation))

#function for counting bigrams
def bigram():
    ciphertext = input("Enter cipher text here: ")
    bigramCount = Counter(map(''.join, zip(ciphertext, ciphertext[1:])))
    print(bigramCount)

#function for counting trigrams
def trigram():
    ciphertext = input("Enter cipher text here: ")
    trigramCount = Counter(map(''.join, zip(ciphertext, ciphertext[1:], ciphertext[2:])))
    print(trigramCount)

alphabet = string.ascii_uppercase