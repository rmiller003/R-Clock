# This an Alarm clock program written in Python 3.8

import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os, time, winsound

def createWidgets():

    label1 = Label(root, text="Enter the time in hh:mm - ")
    label1.grid(row=0, column=0, padx=5, pady=5)

    global entry1
    entry1 = Entry(root, width=15)
    entry1.grid(row=0, column=1)

    label2 = Label(root, text="Enter the alarm message: ")
    label2.grid(row=1, column=0, padx=5, pady=5)

    global entry2
    entry2 = Entry(root, width=15)
    entry2.grid(row=1, column=1)

root = tk.Tk()
root.title("R-Clock")
root.geometry("400x150")

createWidgets()


root.mainloop()


