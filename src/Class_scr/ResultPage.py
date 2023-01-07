from tkinter import *
from tkinter import messagebox
import webbrowser

from Utils import *

# # 최종 결과화면 : frame29
# # fram29 생성 및 위치 지정 및 캔버스 생성

# # 다시하기 버튼
# btn_restart= Button(frame29, image=img_restart,borderwidth=1,command=lambda:[OpenFrame(frame1)])
# btn_restart.place(x=100,y=530)

# # 종료하기 버튼
# btn_end = Button(frame29, image=img_end,borderwidth=1,command= close)
# btn_end.place(x=320,y=532)

# # 링크 연결 버튼 및 종료
# btn_web = Button(frame29,image=img_web,borderwidth=1,\
#     command= lambda:[web('https://www.16personalities.com/ko/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95-isfp'),close()])
# btn_web.place(x=242,y=363)

class ResultPage:
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
    
    def add_end(self, img, pos, command):
        self.btn_end = Button(self.frame, image=img, 
                                borderwidth=1,overrelief='solid'
                                ,command=command)
        self.btn_end.place(x=pos[0], y=pos[1])
        
    def add_link(self, img, pos, command):
        self.btn_link = Button(self.frame, image=img, 
                                borderwidth=1,overrelief='solid'
                                ,command=command)
        self.btn_link.place(x=pos[0], y=pos[1])
