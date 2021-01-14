#!/usr/bin/python3
##
## EPITECH PROJECT, 2021
## worshop_cryptography_lois_bigot
## File description:
## exo2
##

import sys
import hashlib

salt = "5UA@/Mw^%He]SBaU"

def read_file():
    f = open("info.txt", "r")
    arr = f.read().split('\n')
    return arr

def hashing(arr):
    i = 0
    mdp = []
    for i in arr:
        h = hashlib.sha256(i.encode('utf-8')).hexdigest()
        mdp.append(h)
    return mdp

def cmpstring(mdp):
    i = 0
    for i in range(len(mdp)):
        if mdp[i] == "fc2298f491eac4cff95e7568806e088a901c904cda7dd3221f551e5b89b3c3aa":
            return i

def display(i, arr):
    print(arr[i])

def main():
    x = cmpstring(hashing(read_file()))
    y = read_file()
    display(x, y)

main()