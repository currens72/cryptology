from pickletools import string1
import string
from typing import Counter
from collections import Counter
import tkinter as tk

#100 most common words according to wikipedia.org
#REMOVED ALL 2 LETTER WORDS
commonWord = ["THE", "AND", "THAT", "HAVE", "FOR", "NOT", "WITH", "YOU", "THIS", "BUT", "HIS", "FROM", "THEY", "SAY", "HER", "SHE", "WILL", "ONE", "ALL", "WOULD", "THERE", "THEIR", "WHAT", "OUT", "ABOUT", "WHO", "GET", "WHICH", "WHEN", "MAKE", "CAN", "LIKE", "TIME", "JUST", "HIM", "KNOW", "TAKE", "PEOPLE", "INTO", "YEAR", "YOUR", "GOOD", "SOME", "COULD", "THEM", "THEM", "SEE", "OTHER", "THAN", "THEN", "NOW", "LOOK", "ONLY", "COME", "ITS", "OVER", "THINK", "ALSO", "BACK", "AFTER", "USE", "TWO", "HOW", "OUR", "WORK", "FIRST", "WELL", "WAY", "EVEN", "NEW", "WANT", "BECAUSE", "ANY", "THESE", "GIVE", "DAY", "MOST"]

#function to check if 100 most common words are contained in decryption
def contains(string):
    if any(ele in string for ele in commonWord):
        return True
    else:
        return False

#function to count how many of 100 most common words appear
def countWords(string):
    total = sum(string.count(i) for i in commonWord)
    return total

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
decryptedCount = int(1)
decryptedList = []
#function for shift cipher button
def shiftCipherButton():
    #function to automatically decrypt cipher text
    def autoDecrypt():
        decryptedList.clear()
        encryptedText = cipherText.get(1.0, "end-1c")
        encryptedText = encryptedText.replace(" ", "")
        encryptedText = encryptedText.upper()
        for i in range(1, 26):
            shifted = alphabet[i:] + alphabet[:i]
            translation = str.maketrans(shifted, alphabet)
            checkText = encryptedText.translate(translation)
            if contains(checkText):
                if countWords(checkText) > 1:
                    decryptedList.append(checkText)
        plainText.insert("1.0", decryptedList[0])
        nextLabel["text"] = str(len(decryptedList) - 1) + " remaining encryptions"
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
        global decryptedCount
        global automatic
        decryptedCount = int(1)
        plainText.delete("1.0", "end")
        if automatic == 1:
            autoDecrypt()
        else:
            manualDecrypt()
    #function to switch cipher
    def nextDecrypion():
        plainText.delete("1.0", "end")
        global decryptedCount
        numberLeft = str(len(decryptedList) - decryptedCount - 1)
        if decryptedCount < len(decryptedList):
            nextLabel["text"] = numberLeft + " remaining encryptions"
            plainText.insert("1.0", decryptedList[decryptedCount])
            decryptedCount = decryptedCount + 1
        else:
            nextLabel["text"] = "0 remaining encryptions"
            plainText.insert("1.0", "Out of auto-detected decryptions. Click run to reset the list.")
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
    nextButton = tk.Button(
        shiftWindow,
        text="Click for next\nencryption.",
        width=15,
        height=3,
        bg="white",
        fg="black",
        command=nextDecrypion
    )
    nextLabel = tk.Label(
        shiftWindow,
        text="0 remaining encryptions"
    )
    runButton.grid(row=0, column=0)
    autoLabel.grid(row=1, column=0)
    autoButton.grid(row=2, column=0)
    cipherText.grid(row=0, column=3)
    plainText.grid(row=2, column=3)
    shiftAmount.grid(row=1, column=3)
    inputLabel.grid(row=0, column=2)
    shiftLabel.grid(row=1, column=2)
    nextButton.grid(row=2, column=2)
    nextLabel.place(x=200, y=160)

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