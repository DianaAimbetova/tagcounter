import tkinter as tk
import db_worker
import html_tag_counter
import site_util
import logging
from datetime import datetime

class Gui(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.master.title('HTML Parser')
        self.master.geometry('1300x500')
        site = tk.StringVar()
        site_entry = tk.Entry(textvariable=site)
        site_entry.place(relx=0.5, rely=0.1, anchor='c')
        lbl = tk.Label(self.master, text="Results")
        lbl.place(relx=0.0, rely=0.5, anchor='sw')
        get_button = tk.Button(text='Get', command=(lambda: self.get(site.get(), lbl)))
        get_button.place(relx=0.4, rely=0.15, anchor='c')
        view_button = tk.Button(text='View', command=(lambda: self.view(site.get(), lbl)))
        view_button.place(relx=0.6, rely=0.15, anchor='c')

    def get(self,site,lbl):
        site = site_util.define_site_name(site)
        parser = html_tag_counter.MyHTMLParser()
        url = site_util.build_url(site)
        parser.feed(site_util.get_site_content(url))
        tags = html_tag_counter.get_tags()
        logging.info(str(datetime.now()) + ' Getting tags: ' + str(tags))
        code = db_worker.insert_tags(site, url, tags)
        if code == 200:
            lbl.configure(text=str('Data inserted succesfully'))
        else:
            lbl.configure(text=str('Error! For more information please check myapp.log file'))

    def view(self, site, lbl):
        site = site_util.define_site_name(site)
        url = site_util.build_url(site)
        result = db_worker.select_tags(url)
        logging.info(str(datetime.now()) + ' Getting tags: ' + str(result))
        lbl.configure(text=str(result))
