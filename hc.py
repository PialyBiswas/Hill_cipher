# -*- coding: utf-8 -*-
"""
Created on Thu May 17 18:47:25 2018

@author: pialy biswas 
to encrypt 3 letter using 3x3 key matrix 
"""

import numpy as np
from numpy.linalg import inv
originalMessage = []
encryptKey = []
def get_user_input(value, msg):
	text=input(msg).lower()
	for character in text:
		number=ord(character)-97
		value.append(number)

get_user_input(originalMessage, 'Enter Message to Encrypt')
get_user_input(encryptKey, 'Enter decryption Key')
inputLen= len(originalMessage)
rows, cols=np.int(inputLen), np.int(inputLen) 
def build_matrix(matrix):
	value = np.zeros((rows, 1),dtype=int)
	for i in range(0, len(matrix)):
		r=int(i/cols)
		c=int(i%cols)
		value[c,r]=matrix[i]
	return value
originalMessage = build_matrix(originalMessage)
print(originalMessage)
def build_Keymatrix(matrix):
	value = np.zeros((rows, cols),dtype=int)
	for i in range(0, len(matrix)):
		r=int(i/cols)
		c=int(i%cols)
		value[r,c]=matrix[i]
	return value
encryptKey = build_Keymatrix(encryptKey)
print(encryptKey)
encryptedMessage = (np.dot(encryptKey,originalMessage))%26
print(encryptedMessage)
decryptionKey = inv(np.matrix(encryptKey))
decryptionKey = (decryptionKey*(np.linalg.det(np.matrix(encryptKey))))%26
decryptedMessage1 = (np.dot(decryptionKey,encryptedMessage))%26
b=np.matrix([26, 26,26]).T
decryptedMessage1=np.rint(b-decryptedMessage1)
print(decryptedMessage1)
