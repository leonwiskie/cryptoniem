#!/usr/bin/env python3
import random
word_file = 'words'
WORDS = open(word_file).read().splitlines()

print("[*] Generate NSA like cryptonyms")
for n in range(2):
    cryptonym = ''.join([WORDS[random.randint(0,len(WORDS))] for i in range(2)]).upper()

print(cryptonym)
