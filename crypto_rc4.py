# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 22:01:40 2019

@author: sandverm

Cryptography  RC4 algo v0.1
"""
import sys

program_name = sys.argv[0]
args = sys.argv[1:]
countArg = len(args)

consoleMode = False
if countArg != 3:
    print("Usage:")
    print("app <passphrase> <in file> <out file>")
    print("No argument given, encrypt text on console", end = "\n\n")
    consoleMode = True

#user input
if consoleMode:
    key = input("key:")
    data = input("data:")
else:
    key = args[0]
    fileIn = open(args[1], "r")
    data = fileIn.read()


key = [ord(key[i]) for i in range(len(key))]

BIT_LEN = 256

S = [s for s in range(BIT_LEN)]

T = [key[i%len(key)] for i in range(BIT_LEN)]

def swap(L, i, j):
    temp = L[i]
    L[i] = L[j]
    L[j] = temp

# Scrambling the value of T by permutation 
j = 0
for i in range(BIT_LEN):
    j = (j + S[i] + T[i]) % BIT_LEN
    swap(S, i, j)

def get_byte_stream():
    i = 0
    j = 0
    while True:
        i = (i + 1) % BIT_LEN
        j = (j + S[i]) % BIT_LEN
        swap(S, i, j)
        t = (S[i] + S[j]) % BIT_LEN
        k = S[t]
        yield k



def encrypt(data, stream):
    """
    returns cypher when data is passed.
    returns data when cypher is passed.
    """
    cypher = []
    cypher = [chr((ord(d) ^ next(stream))) for d in data]
    return cypher


res = encrypt(data, get_byte_stream())

if consoleMode:
    for i in res:
        print(i, end='')
    print("")
else:
    fileOut = open(args[2], "w")
    for i in res:
        fileOut.write(i)
    fileOut.close()
