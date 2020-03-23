# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 17:25:53 2020

@author: shirai
"""

import sys
import tkinter as tk
import tkinter.messagebox as tkm
import random


root = tk.Tk()

# ウインドウのタイトルを定義する
root.title(u'Buttonを使ってみる')

# ここでウインドウサイズを定義する
root.geometry('400x300')



#「描く」ボタンが押されたら
def draw(event):
    # 四角形で塗りつぶし
    canvas.create_rectangle(random.randint(0, 300), random.randint(0, 200), random.randint(0, 400), random.randint(0, 250), tag="rectangle", fill='green', outline='#00f')



#「消す」ボタンが押されたら
def erase(event):
    canvas.delete("rectangle")




#キャンバスエリア
canvas = tk.Canvas(root, width = 400, height = 250)
canvas.place(x=0, y=0)          # キャンバスエリアを(0,0)で指定



# 「描く」ボタン
button_draw = tk.Button(root, text=u'描く', width=15)
button_draw.bind("<Button-1>", draw)
button_draw.place(x=50, y=260)



# 「消す」ボタン
button_draw = tk.Button(root, text=u'消す', width=15)
button_draw.bind("<Button-1>", erase)
button_draw.place(x=200, y=260)


root.mainloop()