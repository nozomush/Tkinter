# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 16:29:36 2020

@author: shirai
"""
import tkinter as tk

root = tk.Tk()


list = root.Treeview()
list.pack( fill = tk.BOTH, expand = 1 )
items = [ list.insert( '', 'end', text = str( i ) ) for i in range( 10 ) ]
list.selection_set( items[ 0 ] )
list.focus_set() # This is not working - list has no focus :(
tk.mainloop()
