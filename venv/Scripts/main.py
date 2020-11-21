from cmd import run
from gui import Gui
import tkinter as tk
import logging
from datetime import datetime

logging.basicConfig(filename='myapp.log', level=logging.INFO)
logging.info(str(datetime.now())+' Started')
print("please enter command: ")
command = input()
if '--get' in command or '--view' in command:
    logging.info(str(datetime.now()) + ' Console mode running...')
    run(command)
else:
    logging.info(str(datetime.now()) + ' GUI mode running...')
    root = tk.Tk()
    app = Gui(master=root)
    app.mainloop()
logging.info(str(datetime.now())+' Finished')