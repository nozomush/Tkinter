# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 16:25:58 2020

@author: shirai
"""

#-*- coding: utf8 -*-

import tkinter as tk
import tkinter.messagebox as tkm


root = tk.Tk()

# ウインドウのタイトルを定義する
root.title(u'Buttonを使ってみる')

# ここでウインドウサイズを定義する
root.geometry('400x300')


# ボタンが押されたら呼び出される関数
def showMessage(text):
    tkm.showinfo('ダイアログのタイトル', text)


# ラベルを使って文字を画面上に出す
Static1 = tk.Label(text=u'▼　Entryだぞ！　▼')
Static1.pack()


# Entryを出現させる
Entry1 = tk.Entry(width=50)                   # widthプロパティで大きさを変える
Entry1.insert(tk.END, u'挿入する文字列')        # 最初から文字を入れておく
Entry1.pack()


# Buttonを設置してみる
Button1 = tk.Button(text=u'テキストを取得するボタン', width=50, command=lambda: showMessage(Entry1.get()))        # 関数に引数を渡す場合は、commandオプションとlambda式を使う
Button1.pack()


# 普通のダイアログ
tkm.showinfo('ダイアログのタイトル', '普通のダイアログ')

# ワーニングなダイアログ
tkm.showwarning('ダイアログのタイトル', 'ワーニングなダイアログ')

# エラーな感じのダイアログ
tkm.showerror('ダイアログのタイトル', 'エラーな感じのダイアログ')


# YES/NOなダイアログ（YESがクリックされたら戻り値がtrue、NOならfalse）
tkm.askyesno('ダイアログのタイトル', 'YES/NOなダイアログ')


# リトライキャンセルダイアログ（リトライがクリックされたら戻り値がtrue、キャンセルならfalse）
tkm.askretrycancel('ダイアログのタイトル', 'リトライキャンセルダイアログ')


# OK/NOダイアログ（リトライがクリックされたら戻り値が'yes'、キャンセルなら'no'）
tkm.askquestion('ダイアログのタイトル', 'OK/NOダイアログ')


# OK/CANCELダイアログ（OKがクリックされたら戻り値がtrue、キャンセルならfalse
tkm.askokcancel('ダイアログのタイトル', 'OK/CANCELダイアログ')



root.mainloop()