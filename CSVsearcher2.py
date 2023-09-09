#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 11:28:02 2023

@author: ahitochigaidesu.
"""

import tkinter as tk
import re
import pandas as pd
import sys


class Commands:
    commands_array = {}
    
    def command_checker(self,command):
        if command in self.commands_array.keys():
            return(True)
        else:
            return(False)
        
    def command_handler(self,command):
        func = self.commands_array[command]
        func()


class File:
    def get_filepath(self):
        for i in range(3):
            file = input("ファイルパスを指定してください >>")
            file = file.replace('"',"")
            file = rf"{file}"
            try:
                self.df = pd.read_csv(file)
                break
            except:
                print("\aファイルを開くことに失敗しました")
        else:
            sys.exit()


class Searcher:
    def searcher(self,word):
        res = []
        for i in self.df.itertuples():
            for i2 in i[1:]:
                i2 = str(i2)
                if i2 != "nan":
                    if self.check_word_in_text(word, i2):
                        res.append(i[1:])
                        break
        return(res)
                    
    
    def check_word_in_text(self,partial_word, text):
        pattern = re.compile(re.escape(partial_word), re.IGNORECASE)
        match = pattern.search(text)
        if match:
            return True
        else:
            return False
        
    def starts_with_slash_with_space(self,s):
        pattern = r'^\s*/'
        match = re.search(pattern, s)
        return bool(match)
    
    def NDC_searcher(self,ndc:str):
        res = []
        for index, i in enumerate(self.df["NDC"]):
            i = str(i)
            if i != "nan":
                for i2, inp in zip(list(i),ndc):
                    if inp == "x":
                        pass
                    elif i2 != inp:
                        break
                else:
                    res.append(self.df.iloc[index])
        return(res)

    
    
    

class Main(Searcher,File,Commands):
    def __init__(self):
        self.get_filepath()
        self.root = tk.Tk()
        self.root.title("蔵書検索")
        self.root.geometry("500x300")
        self.frame_1 = tk.Frame(self.root)
        self.frame_1.pack()
        self.label_1 = tk.Label(self.frame_1,text="ver 2.0")
        self.label_1.grid(column=0,row=0)
        self.entry = tk.Entry(self.frame_1)
        self.entry.grid(column=1,row=0)
        self.btn_1 = tk.Button(self.frame_1,text="検索",command=self.pressed)
        self.btn_1.grid(column=2,row=0)
        self.textbox = tk.Text(self.root)
        self.textbox.pack()
        
        self.entry.bind("<Return>",self.binded)
        
        self.root.mainloop()
        
    def output(self,data:list):
        self.textbox.delete("1.0", tk.END)
        text = ""
        for i in data:
            i3 = ""
            for i2 in i:
                if str(i2) != "nan":
                    i3 += f"{i2} / "
            else:
                text += f"{i3}\n\n"
        self.textbox.insert(tk.END, text)
        self.label_1["text"] = f"{len(data)}件ヒット"
        
    def binded(self,event):
        self.pressed()
        
    def pressed(self):
        data = re.sub('^\s*','',self.entry.get())
        if not self.starts_with_slash_with_space(data):
            res = self.searcher(data)
            self.output(res)
        else:
            data = re.sub("^/\s*","",data)
            if self.command_checker(data):
                self.command_handler(data)
            else:
                res = self.NDC_searcher(data)
                self.output(res)

if __name__ == "__main__":
    Main()
