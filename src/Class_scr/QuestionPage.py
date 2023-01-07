from tkinter import *
from tkinter import messagebox
import webbrowser

from Utils import *

class QuestionPage:
    def __init__(self, window, img_q_path, img_o1_path, img_o2_path, o1_pos, o2_pos, o1_value, o2_value):
        self.name = img_o1_path
        self.img_q = PhotoImage(file=img_q_path)
        self.img_o1 = PhotoImage(file=img_o1_path)
        self.img_o1 = self.img_o1.subsample(1)
        self.img_o2 = PhotoImage(file=img_o2_path)
        self.img_o2 = self.img_o2.subsample(1)
        
        self.frame = Frame(window)
        self.frame.place(x=0, y=0)
        
        self.canvas = Canvas(self.frame, height=710, width=503, bg='white')
        self.canvas.pack()
        self.canvas.create_image(250, 335, image=self.img_q)
        
        self.q_var = IntVar()
        self.radio1 = Radiobutton(self.frame, image=self.img_o1, variable=self.q_var,
                            overrelief='solid',selectcolor='red',
                            value=o1_value, indicatoron=False)
        self.radio1.place(x=40, y=o1_pos)
        self.radio2 = Radiobutton(self.frame, image=self.img_o2, variable=self.q_var,
                            overrelief='solid',selectcolor='red', 
                            value=o2_value, indicatoron=False)
        self.radio2.place(x=40, y=o2_pos)
        
    def add_next(self, img, pos, command):        
        self.btn_next = Button(self.frame, image=img, 
                                borderwidth=1,overrelief='solid'
                                ,command=command)
        self.btn_next.place(x=pos[0], y=pos[1])
    
    def add_before(self, img, pos, command):
        self.btn_before = Button(self.frame, image=img, 
                                borderwidth=1, overrelief='solid'
                                ,command=command)
        self.btn_before.place(x=pos[0], y=pos[1])
