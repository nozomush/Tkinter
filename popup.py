# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:24:08 2020

@author: shirai
"""

import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog as sim

document = ''
file_path = ''
log_path = 'text/edit_log.txt'
log_path_alert_file = 'text/要注意ファイル.txt'

def main(file, all_text, doc):
    #メインウィンドウ生成
    root = tk.Tk()
    root.title('タイトル')
    root.geometry("+110+100")
    root.focus_set()
    
    global document
    document = doc
    
    global file_path
    file_path = file
    
    #ラベル
    Static1 = tk.Label(text=all_text, justify='left')
    Static1.pack(expand = True, fill = 'x')
    
    #サブウィンドウを開くボタンの配置（メインウィンドウ上に）
    button1 = tk.Button(root, text = "ボタン1", command = subwindow_open)
    button1.pack(side='left')
            
    button2 = tk.Button(root, text = "ボタン2")
    button2.pack(side='left')

    # Show the next file with pressing Enter Key
    def close_window(event):
        root.destroy()
        
    root.bind('<Return>', close_window)
   
    root.mainloop()
    
#サブウィンドウを開く関数の定義
def subwindow_open() :
    subwindow = tk.Toplevel()
    subwindow.title('文章の置換')
    subwindow.geometry("500x200+150+300")
    sub_label = tk.Label(subwindow, text='')
    sub_label.pack()
    
    line_index = sim.askstring("simpledialog", "行番号の入力", initialvalue="")
    target_para = document.paragraphs[int(line_index)].text

    print('-------------')
    print('変更箇所　　:', target_para)
    print('-------------')
    
    # テキストボックス
    txt = tk.Entry(subwindow,width=40)
    txt.pack()
    if target_para[0].isdecimal() or target_para[0] in '１２３４５６７８９':
        txt.insert(tk.END, target_para[1:])    
    else:
        txt.insert(tk.END, '1' + target_para)    
        
    def replace_text(event):
        print('置換された文:', txt.get())
        print('-------------')
        if len(txt.get()) > 0:
            subwindow.withdraw()
            
    insert_button = tk.Button(subwindow, text='挿入ボタン', width=16, command = replace_text)
    insert_button.pack(side = 'top')   

    txt.focus_set()
    # バインディング
    txt.bind('<Return>', replace_text)

    #メッセージボックスを開く関数の定義
    def msgbox_display():
        response = messagebox.askyesno("タイトル", "他の行があれば行番号を指定してください。他の行はありますか？")
        if response:
            print("はい")
        else:
            print("いいえ")

    #メッセージボックスを表示させるボタンの配置（サブウィンドウ上に）
    messagebox_button = tk.Button(subwindow, text = "挿入ボタン押したら押してください", command = msgbox_display)
    messagebox_button.pack(side = 'bottom')

    subwindow.mainloop()

if __name__ == '__main__':
    main('1 aiueo', 'LABEL', 'ABCDEFG')