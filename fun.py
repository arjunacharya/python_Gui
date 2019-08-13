'''
Created on 10-Aug-2019

@author: Arjun
'''
# Gui libaray tkinter 
import tkinter as tk
from tkinter import  Menu
from tkinter import  ttk
from Tools.demo.sortvisu import WIDTH
from _stat import filemode
from cProfile import label
from pip._vendor.webencodings import labels
from cgitb import text
from pip._vendor.pyparsing import col


# exit function name quit
def quit():
    win.quit()
    win.destroy()
    exit()

#instance
win=tk.Tk()

#title
win.title("GUI")


# menu bar
menuBar=Menu()
win.config(menu=menuBar)


#add menu item
fileMenu=Menu(menuBar,tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="exit",command=quit)
menuBar.add_cascade(label="file",menu=fileMenu)

#another menu item
helpmenu=Menu(menuBar,tearoff=0)
helpmenu.add_command(label="about")
menuBar.add_cascade(label="help",menu=helpmenu)


#tab control
tabcontrol=ttk.Notebook(win)
tab1=ttk.Frame(tabcontrol)
tabcontrol.add(tab1,text="Tab1")


tab2=ttk.Frame(tabcontrol)
tabcontrol.add(tab2,text="Tab2")

tabcontrol.pack(expand=1,fill="both")

#widegets frame
contain_frame=ttk.Labelframe(tab1,text="weather")
#using the grid layout
contain_frame.grid(column=0,row=0,padx=8,pady=4)



#adding label
ttk.Label(contain_frame,text="location:").grid(column=0,ro=0,sticky='w')



#starting GUI
win.minsize(width=300, height=1)
win.resizable(0, 0)
win.mainloop()
