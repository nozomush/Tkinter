# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:56:08 2020

@author: shirai
"""

import tkinter as tk
import tkinter.messagebox as tkm

target = 'ok'
index = -1
the_line = ''

with open('test.txt','r') as f:
    lines = f.readlines()

root = tk.Tk()

# Settings
root.title('REPLACE')
root.geometry('600x400+400+500')

# Label
label_0 = tk.Label(text = 'TARGET')
label_0.pack()

# Input field
entry_0 = tk.Entry(width = 50) # 50%
entry_0.insert(tk.END, target)
entry_0.pack()

# Label
label = tk.Label(text = '全文表示')
label.pack()

list_box = tk.Listbox()

for i,line in enumerate(lines):
    list_box.insert(i,f'{i} {line}')
    if target in line:
        index = i
        the_line = line
        
#list_box.pack()
list_box.pack(expand = True, fill = 'x', padx = 20)

# Input field
entry_1 = tk.Entry(width = 50) # 50%
entry_1.insert(tk.END, f'{index} {the_line}')
entry_1.pack()

# Input field
entry_2 = tk.Entry(width = 50) # 50%
entry_2.insert(tk.END, '')
entry_2.pack()
#entry_2.pack(padx=200,pady=30)

# Replace line
def replace_text(event):
    text_1 = entry_1.get()
    text_2 = entry_2.get()
    print(text_1)
    print(text_2)
    
    # Replace line
    if index >= 0:
        lines[index] = text_2 + '\n'
        with open('test.txt','w') as f:
            f.writelines(lines)


    else:
        tkm.showerror('エラー', '対象のテキストは存在しません') 
# Button
button = tk.Button(text = 'BUTTON', width = 20)
button.bind('<Button-1>', replace_text)
button.pack(expand = True, fill = 'y', pady = 20)

# Focus
entry_2.focus_force()

root.mainloop()