# -*- coding: utf-8 -*-

"""
Created on Tue Jul 16 12:48:08 2019

@author: William
"""

import itertools
import time

def encrypt_caesar(plaintext):
    # This part of the code implements the encrypt_caesar function
    ## plaintext is a string to encrypt
    
    # Your job is to shift each character in the plaintext by THREE spaces
    # If the character reaches the end, it loops back to the star (see example below)
    # Non-alphabetic characters should NOT be affected
    # ' ' doesn't change, '.' doesn't change, ',' doesn't change


    # 'Z' + 3 = 'C'
    # 'A' + 3 = 'D'
    # 'B' + 3 = 'E'
    # 'a' + 3 = 'd'
    # 'z' + 3 = 'c'
    
    # Encrypting 'PYTHON' returns 'SBWKRQ
    # 'P' + 3 = 'S'
    # 'Y' + 3 = 'B'
    
    
    
    
    # Have a look at ord() and chr()
    # https://docs.python.org/3/library/functions.html#ord
    # https://docs.python.org/3/library/functions.html#chr
    
    
    #########################################################
    #START CODE HERE
    
    
    
    
    
    
    #END CODE HERE
    #########################################################
    
    return ciphertext
    
def decrypt_caesar(ciphertext):
    # This part of the code implements the decrypt_caesar function
    ## ciphertext is a string to decrypt
    
    # Your job here is similar to the one in encrypt_caesar()
    # You shift characters backwards rather than forward
    # Keep in mind if any character is shifted past A or a, it loops back to Z
    
    # 'a' - 3 = 'x'
    # 'B' - 3 = 'Y'
    
    # Decrypting 'SBWKRQ' returns 'PYTHON'
    
    
    #########################################################
    #START CODE HERE





    
    #END CODE HERE
    #########################################################
    
    return plaintext
    

def encrypt_vignere(plaintext, key):
    # This part of the code implements the encrypt_vignere function
    ## plaintext is a string to be encrypted
    ## key is the key to encrypt the string with
    
    # Your job is to shift each character in the plaintext by a variable amount
    # The amount to shift any letter in the plaintext is determined by the key
    # Symbols should also NOT be shifted 
    #
    #
    # The letter 'A' shifts a character 0 spaces
    # The letter 'B' shifts a character 1 space
    #
    # Encrypting 'ATTACKATDAWN' with key 'LEMON' gives 'LXFOPVEFRNHR'
    # 'A' + key 'L' = 'L'
    # 'a' + key 'L' = 'l'
    # 'T' + key 'E' = 'X'
    
    # The key is repeated to produce a key of: 'LEMONLEMONLE'
    # If the key is shorter than the plaintext, the key is repeated 
    
    

    # Have a look at "itertools documentation"
    # https://docs.python.org/2/library/itertools.html
    # Might be useful for this assignment
    
    
    #########################################################
    #START CODE HERE





    
    #END CODE HERE
    #########################################################
    
    
    return ciphertext

    
def decrypt_vignere(ciphertext, key):
    #This part of the code implements the decrypt_vignere function
    ##ciphertext is a string to be decrypted
    ##key is the key to decrypt the string with
    
    # Similar to the encrypt vignere, your job is to reverse the encryption
    # Shifting backwards, following similar rules to the encrypt_vignere()


    #########################################################
    #START CODE HERE





    
    #END CODE HERE
    #########################################################
    
    
    return plaintext
    
    
def main():
    #DO NOT EDIT THIS
    #################################
    #CAESAR ENCRYPT AND DECRYPT
    
    print('You are now encrypting the phrase: "I Love Python" using caesar cipher')
    ciphertext = encrypt_caesar("I Love Python")
    print('The ciphertext produced is:', ciphertext)
    print('It should be: L Oryh Sbwkrq')
    if ciphertext == 'L Oryh Sbwkrq':
        print('(1)You are correct, congratulations~')
    else: 
        print('(1)You are incorrect, please go back and repair your code')
    time.sleep(4)
    
    
    
    print('\nYou are now decrypting the ciphertext: "L Oryh Sbwkrq" using caesar cipher')
    plaintext = decrypt_caesar(ciphertext)
    print('The decrypted text is:', plaintext)
    print('It should be: I Love Python')
    if ciphertext == 'I Love Python':
        print('(2)You are correct, congratulations~')
    else: 
        print('(2)You are incorrect, please go back and repair your code')
    time.sleep(4)
    
    
    
    
    #VIGNERE ENCRYPT AND DECRYPT
    print('\nYou are now encrypting the phrase: "ATTACKATDAWN" using vignere cipher\nkey: LEMON')
    ciphertext = encrypt_vignere("ATTACKATDAWN", "LEMON")
    print('The ciphertext produced is:', ciphertext)    
    print('It should be: LXFOPVEFRNHR')
    if ciphertext == 'LXFOPVEFRNHR':
        print('(3)You are correct, congratulations~')
    else: 
        print('(3)You are incorrect, please go back and repair your code')
    time.sleep(4)
    
    print('\nYou are now decrypting the ciphertext: "LXFOPVEFRNHR" using vignere cipher\nkey: LEMON')
    plaintext = decrypt_vignere(ciphertext, "LEMON")
    print('The decrypted text is:', plaintext)
    print('It should be: ATTACKATDAWN')
    if ciphertext == 'ATTACKATDAWN':
        print('(4)You are correct, congratulations~')
    else: 
        print('(4)You are incorrect, please go back and repair your code')
     


if __name__ == '__main__':
    main()





    
