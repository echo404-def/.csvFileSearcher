#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 19:34:46 2023

@author: echo
"""

import requests
from bs4 import BeautifulSoup
from time import sleep
import csv
import re
import tkinter as tk
import os


class File:
    def get_savefile_path(self):
        desktop = os.path.join(os.path.join(os.path.expanduser('~'), 'Desktop'))
        file = os.path.join(desktop, "JANcode_res.csv")
        return(file)

class GUI:
    def make_display(self):
        self.root = tk.Tk()
        self.root.title("JANコード検索")
        self.root.geometry("300x360")
        self.text = tk.Text(self.root)
        self.text.pack()
        self.btn = tk.Button(self.root,text="実行",command=self.pressed)
        self.btn.pack()
        self.root.mainloop()
        
    def pressed(self):
        self.data = self.text.get("1.0", "end-1c")
        if not self.data == "":
            self.btn.destroy()
            self.text.destroy()
            self.root.geometry("400x90")
            self.confirmation()
            
    def confirmation(self):
        self.label = tk.Label(self.root,text="このファイルに保存します")
        self.label.pack()
        self.entry = tk.Entry(self.root,width=400)
        self.entry.pack()
        self.entry.insert(0,self.file)
        self.btn = tk.Button(self.root,text="決定",command=self.admit)
        self.btn.pack()
        
    def admit(self):
        self.file = self.entry.get()
        self.label.destroy()
        self.btn.destroy()
        self.entry.destroy()
        label = tk.Label(self.root,text=f"{self.file}に保存しました。\nウィンドウを閉じてください。")
        label.pack()
        self.label2 = tk.Label(self.root,fg="red")
        self.label2.pack()
        self.processer(self.data)

class Main(File,GUI):
    def __init__(self):
        self.file = self.get_savefile_path()
        self.make_display()
    
    def processer(self,data):
        ls = data.split("\n")
        ls = list(set(ls))

        res = ""

        for i in ls:
            sleep(0.3)
            jancode = i
            url = f"https://www.jancode.xyz/code/?q={jancode}"
            html = requests.get(url).text
            soup = BeautifulSoup(html, 'html.parser')
            
            
            # pタグ内のテキストを取得
            n = 0
            try:
                p_text = soup.find('p', class_='description').get_text(strip=True)
                print(p_text)
                res += p_text + "\n"
            except:
                n += 1
                print("\aERROR")
        print("end")
        if n != 0:
            self.label2["text"] = f"{n}件のJANコードの情報が発見できませんでした\nコマンドラインから詳細を確認してください"
        
        res = re.sub(r'\n+$', '', res)

        data = res.split("\n")
        res = []

        for i in data:
            i = i.split("/")
            i3 = []
            for i2 in i:
                i2 = re.sub(r'\s+$', '', i2, flags=re.MULTILINE)
                i3.append(i2)
            res.append(i3)
            
        with open(self.file,"w") as w:
            writer = csv.writer(w)
            writer.writerows(res)
            
if __name__ == "__main__":
    Main()
