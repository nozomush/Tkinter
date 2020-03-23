# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:56:08 2020

@author: shirai
"""

import tkinter as tk

with open('test.txt','r') as f:
    s = f.read()


root = tk.Tk()

# Settings
root.title('タイトル')
root.geometry('600x200+400+500')

# Label
label = tk.Label(text = 'Label')
#label.pack()

# Input field
entry_1 = tk.Entry(width = 20) # 50%
entry_1.insert(tk.END, 'Input something here')
#entry_1.pack(side = 'left')

# Input field
entry_2 = tk.Entry(width = 20) # 50%)
entry_2.insert(tk.END, s)
#entry_2.pack(side = 'right')
entry_2.grid(padx=20,pady=30)
# Get text
def get_text(event):
    text = entry_1.get()
    print(text)


# Button
button = tk.Button(text = 'BUTTON', width = 20)
button.bind('<Button-1>', get_text)
#button.pack()

# Focus
entry_1.focus_set()

root.mainloop()