#!/usr/bin/python3
##
## EPITECH PROJECT, 2021
## worshop_cryptography_lois_bigot
## File description:
## exo1
##

import sys
import hashlib

def read_file():
    f = open("phpbb.txt", "r")
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
        if mdp[i] == "3ddcd95d2bff8e97d3ad817f718ae207b98c7f2c84c5519f89cd15d7f8ee1c3b":
            return i

def display(i, arr):
    print(arr[i])

def main():
    x = cmpstring(hashing(read_file()))
    y = read_file()
    display(x, y)

main()