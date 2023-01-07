from tkinter import *
from tkinter import messagebox
import webbrowser

from Utils import *

class StartPage:
    def __init__(self, window, img_background_path):
        self.img = PhotoImage(file=img_background_path)
        
        self.frame = Frame(window)
        self.frame.place(x=0, y=0)
        
        self.canvas = Canvas(self.frame, height=710, width=503, bg='white')
        self.canvas.pack()
        self.canvas.create_image(250, 335, image=self.img)
        
    def add_next(self, img, pos, command):
        self.btn_next = Button(self.frame, image=img, 
                                borderwidth=1,overrelief='solid'
                                ,command=command)
        self.btn_next.place(x=pos[0], y=pos[1])
    