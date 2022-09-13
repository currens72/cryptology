from pickletools import string1
import string
from typing import Counter
from collections import Counter

#100 most common words according to wikipedia.org
commonWord = ["THE", "BE", "TO", "OF", "AND", "IN", "THAT", "HAVE", "IT", "FOR", "NOT", "ON", "WITH", "HE", "AS", "YOU", "DO", "AT", "THIS", "BUT", "HIS", "BY", "FROM", "THEY", "WE", "SAY", "HER", "SHE", "OR", "AN", "WILL", "MY", "ONE", "ALL", "WOULD", "THERE", "THEIR", "WHAT", "SO", "UP", "OUT", "IF", "ABOUT", "WHO", "GET", "WHICH", "GO", "ME", "WHEN", "MAKE", "CAN", "LIKE", "TIME", "NO", "JUST", "HIM", "KNOW", "TAKE", "PEOPLE", "INTO", "YEAR", "YOUR", "GOOD", "SOME", "COULD", "THEM", "THEM", "SEE", "OTHER", "THAN", "THEN", "NOW", "LOOK", "ONLY", "COME", "ITS", "OVER", "THINK", "ALSO", "BACK", "AFTER", "USE", "TWO", "HOW", "OUR", "WORK", "FIRST", "WELL", "WAY", "EVEN", "NEW", "WANT", "BECAUSE", "ANY", "THESE", "GIVE", "DAY", "MOST", "US"]

#function to check if 100 most common words are contained in decryption
def contains(string):
    if any(ele in string for ele in commonWord):
        return True
    else:
        return False

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

testing = input("Enter text here: ")
print(contains(testing))