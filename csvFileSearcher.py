#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 12:01:47 2023

@author: echo
"""

import csv
import re
import sys

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
    sys.exit()
            


def check_word_in_text(partial_word, text):
    pattern = re.compile(re.escape(partial_word), re.IGNORECASE)
    match = pattern.search(text)
    if match:
        return True
    else:
        return False

def search(word):
    res = []
    if word != "":
        for i in data:
            for i2 in i:
                if check_word_in_text(word, i2):
                    res.append(i)
        return(res)
    

def pressed(event=None):
    word = entry_1.get()
    ls = search(word)
    res = ""
    n = len(ls)
    for i in ls:
        for i2 in i:
            res += i2 + " / "
        res += "\n"*2
    textbox.delete("1.0",tk.END)
    textbox.insert(tk.END,res)
    label_1["text"] = f"{n}件ヒット"


try:
    import tkinter as tk
    root = tk.Tk()
    root.title("蔵書検索")
    frame_1 = tk.Frame(root)
    frame_1.pack()
    label_1 = tk.Label(frame_1,text="")
    label_1.grid(column=0,row=0)
    entry_1 = tk.Entry(frame_1)
    entry_1.grid(column=1,row=0)
    btn_1 = tk.Button(frame_1,text="検索",command=pressed)
    btn_1.grid(column=2,row=0)
    textbox = tk.Text(root)
    textbox.pack()
    
    entry_1.bind("<Return>",pressed)
    
    root.mainloop()
    
except:
    print("To exit, type 'exit'")
    
    while True:
        inp = input("word >")
        if inp == "exit":
            break
        else:
            print(search(inp))
