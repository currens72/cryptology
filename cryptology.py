from pickletools import string1
import string
from typing import Counter
from collections import Counter
import tkinter as tk

#100 most common words according to wikipedia.org
commonWord = ["THE", "BE", "TO", "OF", "AND", "IN", "THAT", "HAVE", "IT", "FOR", "NOT", "ON", "WITH", "HE", "AS", "YOU", "DO", "AT", "THIS", "BUT", "HIS", "BY", "FROM", "THEY", "WE", "SAY", "HER", "SHE", "OR", "AN", "WILL", "MY", "ONE", "ALL", "WOULD", "THERE", "THEIR", "WHAT", "SO", "UP", "OUT", "IF", "ABOUT", "WHO", "GET", "WHICH", "GO", "ME", "WHEN", "MAKE", "CAN", "LIKE", "TIME", "NO", "JUST", "HIM", "KNOW", "TAKE", "PEOPLE", "INTO", "YEAR", "YOUR", "GOOD", "SOME", "COULD", "THEM", "THEM", "SEE", "OTHER", "THAN", "THEN", "NOW", "LOOK", "ONLY", "COME", "ITS", "OVER", "THINK", "ALSO", "BACK", "AFTER", "USE", "TWO", "HOW", "OUR", "WORK", "FIRST", "WELL", "WAY", "EVEN", "NEW", "WANT", "BECAUSE", "ANY", "THESE", "GIVE", "DAY", "MOST", "US"]

#function to check if 100 most common words are contained in decryption
def contains(string):
    total = sum(string.count(i) for i in commonWord)
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

############################################################################################
############################################################################################
###############  Window Below Here  ########################################################
############################################################################################
############################################################################################

automatic = int(1)
#function for shift cipher button
def shiftCipherButton():
    #function to automatically decrypt cipher text
    def autoDecrypt():
        encryptedText = cipherText.get(1.0, "end-1c")
        encryptedText = encryptedText.replace(" ", "")
        encryptedText = encryptedText.upper()
        for i in range(1, 26):
            shifted = alphabet[i:] + alphabet[:i]
            translation = str.maketrans(shifted, alphabet)
            checkText = encryptedText.translate(translation)
            if contains(checkText):
                print("True")
            else:
                print("False")
    #function to mannualy decrypt cipher text
    def manualDecrypt():
        shiftBy = shiftAmount.get(1.0, "end-1c")
        shiftBy = int(shiftBy)
        encryptedText = cipherText.get(1.0, "end-1c")
        encryptedText = encryptedText.replace(" ", "")
        encryptedText = encryptedText.upper()
        shifted = alphabet[shiftBy:] + alphabet[:shiftBy]
        #combines regular and shifted alphabet into table for translation
        translation = str.maketrans(shifted, alphabet)
        plainText.insert("1.0", encryptedText.translate(translation))
        #function to shift between automatic or manual
    def autoManual():
        global automatic
        if automatic == 1:
            automatic = automatic - 1
            autoButton["text"] = "Manual"
        else:
            automatic = automatic + 1
            autoButton["text"] = "Automatic"
    #function to run decryption
    def runDecryption():
        global automatic
        plainText.delete("1.0", "end")
        if automatic == 1:
            autoDecrypt()
        else:
            manualDecrypt()
    ##############################################
    ##############################################
    ##############################################
    shiftWindow = tk.Toplevel()
    shiftWindow.resizable(width=False, height=False)
    shiftWindow.geometry('555x250')
    autoLabel = tk.Label(
        shiftWindow,
        text="\nShift between automatic and\nmanual by pressing the\nbutton below.\n"
    )
    autoButton = tk.Button(
        shiftWindow,
        text="Automatic",
        width=25,
        height=5,
        bg="white",
        fg="black",
        command=autoManual
    )
    runButton = tk.Button(
        shiftWindow,
        text="Run",
        width=25,
        height=5,
        bg="white",
        fg="black",
        command=runDecryption
    )
    cipherText = tk.Text(
        shiftWindow,
        height=5,
        width=25
    )
    plainText = tk.Text(
        shiftWindow,
        height=5,
        width=25
    )
    shiftAmount = tk.Text(
        shiftWindow,
        height=1,
        width=3
    )
    inputLabel = tk.Label(
        shiftWindow,
        text="\n\nEnter encrypted text to the left\n\n"
    )
    shiftLabel = tk.Label(
        shiftWindow,
        text="\n\nEnter shift amount here -->\n\n"
    )
    runButton.grid(row=0, column=0)
    autoLabel.grid(row=1, column=0)
    autoButton.grid(row=2, column=0)
    cipherText.grid(row=0, column=3)
    plainText.grid(row=2, column=3)
    shiftAmount.grid(row=1, column=3)
    inputLabel.grid(row=0, column=2)
    shiftLabel.grid(row=1, column=2)

######################################################
######################################################
######################################################
######################################################
######################################################

#setting up the window
window = tk.Tk()
window.title('Basic Cryptology')
window.resizable(width=False, height=False)

shiftButton = tk.Button(
    window,
    text="Shift-By Cipher",
    width=25,
    height=5,
    bg="white",
    fg="black",
    command=shiftCipherButton
)
shiftButton.grid(row=0, column=0)

permutateButton = tk.Button(
    window,
    text="Custom Permutated Alphabet",
    width=25,
    height=5,
    bg="white",
    fg="black"
)
permutateButton.grid(row=0, column=1)

alphabet = string.ascii_uppercase

window.mainloop()