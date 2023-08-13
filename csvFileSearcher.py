#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 12:01:47 2023

@author: echo
"""

import csv
import re

for i in range(3):
    file = rf"{input('.csvFilePath >')}"
    try:
        with open(file,"r",encoding='utf-8') as r:
            data = csv.reader(r)
            data = list(data)
        break
    except:
        print("\aERROR")
else:
    print("\aLimit exceeded.")
            

def check_word_in_text(partial_word, text):
    pattern = re.compile(re.escape(partial_word), re.IGNORECASE)
    match = pattern.search(text)
    if match:
        return True
    else:
        return False

print("To exit, type 'exit'")

while True:
    inp = input("word >")
    if inp == "exit":
        break
    elif inp != "":
        for i in data:
            for i2 in i:
                if check_word_in_text(inp, i2):
                    print(i)