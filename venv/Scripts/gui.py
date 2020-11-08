# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.3 (default, Mar 27 2019, 17:13:21) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: C:\Users\diana_aimbetova\PycharmProjects\tagcounter\venv\Scripts\gui.py
# Compiled at: 2020-11-08 18:47:41
# Size of source mod 2**32: 791 bytes
import tkinter as tk

class Gui(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.master.title('HTML Parser')
        self.master.geometry('200x200')
        site = tk.StringVar()
        site_entry = tk.Entry(textvariable=site)
        site_entry.place(relx=0.5, rely=0.1, anchor='c')
        get_button = tk.Button(text='Get', command=(self.get))
        get_button.place(relx=0.3, rely=0.3, anchor='c')
        view_button = tk.Button(text='View', command=(self.view))
        view_button.place(relx=0.6, rely=0.3, anchor='c')

    def get(self):
        print('get')

    def view(self):
        print('view')