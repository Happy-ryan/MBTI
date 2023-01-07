from tkinter import *
from tkinter import messagebox
import webbrowser
############################################################
def OpenFrame(frame): # 넘어가기, 다음문항 - 화면 전환 이벤트
    frame.tkraise()

def NoBeforeBtn(): # 이전문항 - frame3에서 이전 문항 없을 때 발생하는 이벤트
        messagebox.askokcancel('알림','이전문항이 존재하지 않습니다.')

def NextBtn(q,frame): # 다음문항 - 다음문항 버튼 클릭할 때 발생하는 이벤트
    if q.get() == 0: # 응답하지 않았을 때 알림창
        messagebox.askokcancel('알림','응답하지 않은 항목이 있습니다.')
    else: # 다음 문항으로 넘어가도록 만들기
        OpenFrame(frame)

def SubmmitBtn(q,frame): # 제출하기버튼의 이벤트-q1~q12.get()값을 리스트에 넣고 mbti 결과 내는 함수
        global mbti_list
        global result_list
        global result
        if q.get() == 0:
            messagebox.askokcancel('알림','마지막 문항에 응답하지 않았습니다.')
        else:
            for q in q_list:
                mbti_list[q.get()] += 1
            result_list = [i for i, x in enumerate(mbti_list) if x >= 2]
            result = sum([x * 10**(3-i) for i, x in enumerate(result_list)])
            OpenFrame(frame)
            print(mbti_list) # 각 성향 선택 횟수 파악 리스트
            print(result_list) # 3문제 중 2문제 이상 선택된 성향의 인덱스 출력
            print(result) # result_list 네자리수로 만든, mbti 결과가 global result로 ResultBtn()에서 비교

def ResultBtn():
    global result
    if result == 1457: #INTJ-전략가/frame16
        print('INTJ-전략가')
        OpenFrame(frame16)
    elif result ==1458: #INTP-논리술사/frame17
        print('INTP-논리술사')
        OpenFrame(frame17)
    elif result ==2457: #ENTJ-통솔자/fram18
        print('ENTJ-통솔자')
        OpenFrame(frame18)
    elif result ==2458: #ENTP-변론가/frame19
        print('ENTP-변론가')
        OpenFrame(frame19)
    elif result ==1467: #INFJ-옹호자/frame20
        print('INFJ-옹호자')
        OpenFrame(frame20)
    elif result ==1468: #INFP-중재자/frame21
        print('INFP-중재자')
        OpenFrame(frame21)
    elif result ==2467: #ENFJ-선도자/frame22
        print('ENFJ-선도자')
        OpenFrame(frame22)
    elif result ==2468: #ENFP-활동가/frame23
        print('ENFP-활동가')
        OpenFrame(frame23)
    elif result ==1357: #ISTJ-현실주의자/frame24
        print('ISTJ-현실주의자')
        OpenFrame(frame24)
    elif result ==1367: #ISFJ-수호자/frame25
        print('ISFJ-수호자')
        OpenFrame(frame25)
    elif result ==2357: #ESTJ-경영자/frame26
        print('ESTJ-경영자')
        OpenFrame(frame26)
    elif result ==2367: #ESFJ-집정관/frame27
        print('ESFJ-집정관')
        OpenFrame(frame27)
    elif result ==1358: #ISTP-장인/frame28
        print('ISTP-장인')
        OpenFrame(frame28)
    elif result ==1368: #ISFP-모험가/frame29
        print('ISFP-모험가')
        OpenFrame(frame29)
    elif result ==2358: #ESTP-사업가/frame30
        print('ESTP-사업가')
        OpenFrame(frame30)
    elif result ==2368: #ESFP-연예인/frame31
        print('ESFP-연예인')
        OpenFrame(frame31)
# 종료하기
def close():
    window.destroy()
# 외부 링크 열기
def web(web):
    webbrowser.open(web)
############################################################
window = Tk()
window.title('H는 묵음이야 ~ M Bㅏ프 T I')
window.geometry('503x710')
window.resizable(False,False)
############################################################
img_click = PhotoImage(file='image/click.PNG') # frame1의 클릭하기버튼
img_pass = PhotoImage(file='image/btn_pass.PNG') # frame2의 넘어가기버튼
img_next = PhotoImage(file='image/btn_next.PNG') # 다음문항버튼
img_next = img_next.subsample(2)
img_before = PhotoImage(file='image/btn_before.PNG') # 이전문항버튼
img_before = img_before.subsample(2)
img_submmit = PhotoImage(file='image/btn_submmit.PNG') # 제출하기버튼
img_submmit = img_submmit.subsample(3)
img_result = PhotoImage(file='image/btn_result.PNG') # 결과보기버튼
img_restart = PhotoImage(file='image/btn_restart.PNG') # 다시하기 버튼
img_restart = img_restart.subsample(2)
img_end = PhotoImage(file='image/btn_end.PNG') # 종료하기 버튼
img_end = img_end.subsample(2)
img_web = PhotoImage(file='image/web.png') # 링크연결 버튼
img_web = img_web.subsample(1)
###########################################################종료화면 이미지
img_f16 = PhotoImage(file='image/f16.PNG')
img_f17 = PhotoImage(file='image/f17.PNG')
img_f18 = PhotoImage(file='image/f18.PNG')
img_f19 = PhotoImage(file='image/f19.PNG')
img_f20 = PhotoImage(file='image/f20.PNG')
img_f21 = PhotoImage(file='image/f21.PNG')
img_f22 = PhotoImage(file='image/f22.PNG')
img_f23 = PhotoImage(file='image/f23.PNG')
img_f24 = PhotoImage(file='image/f24.PNG')
img_f25 = PhotoImage(file='image/f25.PNG')
img_f26 = PhotoImage(file='image/f26.PNG')
img_f27 = PhotoImage(file='image/f27.PNG')
img_f28 = PhotoImage(file='image/f28.PNG')
img_f29 = PhotoImage(file='image/f29.PNG')
img_f30 = PhotoImage(file='image/f30.PNG')
img_f31 = PhotoImage(file='image/f31.PNG')
############################################################
# 시작화면: frame1

# frame1 사진 호출
img_startpage = PhotoImage(file='image/startpage.PNG')
# fram1 생성 및 위치 지정 및 캔버스 생성
frame1 = Frame(window)
frame1.place(x=0,y=0) # 프레임 위치 (x=0,y=0) 통일

canvas1 = Canvas(frame1,height=710,width=503,bg='white')
canvas1.pack()
canvas1.create_image(250,335,image=img_startpage)

# 시작하기 버튼
btn_start = Button(frame1, image=img_click,borderwidth=1,overrelief='solid',command= lambda: [OpenFrame(frame2)])
btn_start.place(x=120,y=480)
############################################################
# 설명화면 : frame2

# frame2 사진 호출
img_explainpage = PhotoImage(file='image/explainpage.PNG')

# fram2 생성 및 위치 지정 및 캔버스 생성
frame2 = Frame(window)
frame2.place(x=0,y=0) # 프레임 위치 (x=0,y=0) 통일

canvas2 = Canvas(frame2,height=710,width=503,bg='white')
canvas2.pack()
canvas2.create_image(250,335,image=img_explainpage)

# 넘아가기 버튼
btn_pass = Button(frame2, image=img_pass,borderwidth=1,overrelief='solid',command= lambda: [OpenFrame(frame3)])
btn_pass.place(x=135,y=480)
############################################################문항1
# 문제화면1 : frame3 - q1 (이전문항 - 메세지창 : 이전 문항이 없습니다.)
# frame3 사진 호출
img_q1 = PhotoImage(file='image/q1.PNG') # 배경 - canvas
img_q1_1 = PhotoImage(file='image/q1_1.PNG')
img_q1_1 = img_q1_1.subsample(1)
img_q1_2 = PhotoImage(file='image/q1_2.PNG')
img_q1_2 = img_q1_2.subsample(1)

# fram3 생성 및 위치 지정
frame3 = Frame(window)
frame3.place(x=0,y=0) # 프레임 위치 (x=0,y=0) 통일

canvas3 = Canvas(frame3,height=710,width=503,bg='white')
canvas3.pack()
canvas3.create_image(250,335,image=img_q1)

# 문항1-체크하는 라디오 버튼 생성
q1 = IntVar()
rd1 = Radiobutton(frame3,image=img_q1_1,variable=q1,value=2,indicatoron=False,overrelief='solid',selectcolor='red') # E성향 - value : 2
rd1.place(x=46,y=300)
rd2 = Radiobutton(frame3,image=img_q1_2,variable=q1,value=1,indicatoron=False,overrelief='solid',selectcolor='red') # I성향 - value : 1
rd2.place(x=46,y=400)

# 다음문항 버튼
btn_next = Button(frame3, image=img_next,borderwidth=1,overrelief='solid',command= lambda: [NextBtn(q1,frame4)])
btn_next.place(x=270,y=530)

# 이전문항 버튼
btn_before = Button(frame3, image=img_before,borderwidth=1,overrelief='solid',command= NoBeforeBtn)
btn_before.place(x=100,y=530)
############################################################문항2
# 문제화면2 : frame4 - q2 
# frame4 사진 호출
img_q2 = PhotoImage(file='image/q2.PNG') # 배경 - canvas
img_q2_1 = PhotoImage(file='image/q2_1.PNG')
img_q2_1 = img_q2_1.subsample(1)
img_q2_2 = PhotoImage(file='image/q2_2.PNG')
img_q2_2 = img_q2_2.subsample(1)

# fram4 생성 및 위치 지정
frame4 = Frame(window)
frame4.place(x=0,y=0) # 프레임 위치 (x=0,y=0) 통일

canvas4 = Canvas(frame4,height=710,width=503,bg='white')
canvas4.pack()
canvas4.create_image(250,335,image=img_q2)

# 문항2-체크하는 라디오 버튼 생성
q2 = IntVar()
rd3 = Radiobutton(frame4,image=img_q2_1,variable=q2,value=7,indicatoron=False,overrelief='solid',selectcolor='red') # J성향 - value : 7
rd3.place(x=46,y=300)
rd4 = Radiobutton(frame4,image=img_q2_2,variable=q2,value=8,indicatoron=False,overrelief='solid',selectcolor='red') # P성향 - value : 8
rd4.place(x=46,y=400)

# 다음문항 버튼
btn_next = Button(frame4, image=img_next,borderwidth=1,overrelief='solid',command= lambda: [NextBtn(q2,frame5)])
btn_next.place(x=270,y=530)

# 이전문항 버튼
btn_before = Button(frame4, image=img_before,borderwidth=1,overrelief='solid',command= lambda:[OpenFrame(frame3)])
btn_before.place(x=100,y=530)
############################################################문항3
# 문제화면3 : frame5 - q3
# frame5 사진 호출
img_q3 = PhotoImage(file='image/q3.PNG') # 배경 - canvas
img_q3_1 = PhotoImage(file='image/q3_1.PNG')
img_q3_1 = img_q3_1.subsample(1)
img_q3_2 = PhotoImage(file='image/q3_2.PNG')
img_q3_2 = img_q3_2.subsample(1)

# fram5 생성 및 위치 지정
frame5 = Frame(window)
frame5.place(x=0,y=0) # 프레임 위치 (x=0,y=0) 통일

canvas5 = Canvas(frame5,height=710,width=503,bg='white')
canvas5.pack()
canvas5.create_image(250,335,image=img_q3)

# 문항3-체크하는 라디오 버튼 생성
q3 = IntVar()
rd5 = Radiobutton(frame5,image=img_q3_1,variable=q3,value=5,indicatoron=False,overrelief='solid',selectcolor='red') # T성향 - value : 5
rd5.place(x=46,y=300)
rd6 = Radiobutton(frame5,image=img_q3_2,variable=q3,value=6,indicatoron=False,overrelief='solid',selectcolor='red') # F성향 - value : 6
rd6.place(x=46,y=400)

# 다음문항 버튼
btn_next = Button(frame5, image=img_next,borderwidth=1,overrelief='solid',command= lambda: [NextBtn(q3,frame6)])
btn_next.place(x=270,y=530)

# 이전문항 버튼
btn_before = Button(frame5, image=img_before,borderwidth=1,overrelief='solid',command= lambda:[OpenFrame(frame4)])
btn_before.place(x=100,y=530)
############################################################문항4
# 문제화면4 : frame6 - q4
# frame6 사진 호출
img_q4 = PhotoImage(file='image/q4.PNG') # 배경 - canvas
img_q4_1 = PhotoImage(file='image/q4_1.PNG')
img_q4_1 = img_q4_1.subsample(1)
img_q4_2 = PhotoImage(file='image/q4_2.PNG')
img_q4_2 = img_q4_2.subsample(1)

# fram6 생성 및 위치 지정
frame6 = Frame(window)
frame6.place(x=0,y=0) # 프레임 위치 (x=0,y=0) 통일

canvas6 = Canvas(frame6,height=710,width=503,bg='white')
canvas6.pack()
canvas6.create_image(250,335,image=img_q4)

# 문항4-체크하는 라디오 버튼 생성
q4 = IntVar()
rd7 = Radiobutton(frame6,image=img_q4_1,variable=q4,value=4,indicatoron=False,overrelief='solid',selectcolor='red') # N성향 - value : 4
rd7.place(x=46,y=300)
rd8 = Radiobutton(frame6,image=img_q4_2,variable=q4,value=3,indicatoron=False,overrelief='solid',selectcolor='red') # S성향 - value : 3
rd8.place(x=46,y=400)

# 다음문항 버튼
btn_next = Button(frame6, image=img_next,borderwidth=1,overrelief='solid',command= lambda: [NextBtn(q4,frame7)])
btn_next.place(x=270,y=530)

# 이전문항 버튼
btn_before = Button(frame6, image=img_before,borderwidth=1,overrelief='solid',command= lambda:[OpenFrame(frame5)])
btn_before.place(x=100,y=530)
############################################################문항5
# 문제화면5 : frame7 - q5
# frame7 사진 호출
img_q5 = PhotoImage(file='image/q5.PNG') # 배경 - canvas
img_q5_1 = PhotoImage(file='image/q5_1.PNG')
img_q5_1 = img_q5_1.subsample(1)
img_q5_2 = PhotoImage(file='image/q5_2.PNG')
img_q5_2 = img_q5_2.subsample(1)

# fram6 생성 및 위치 지정
frame7 = Frame(window)
frame7.place(x=0,y=0) # 프레임 위치 (x=0,y=0) 통일

canvas7 = Canvas(frame7,height=710,width=503,bg='white')
canvas7.pack()
canvas7.create_image(250,335,image=img_q5)

# 문항5-체크하는 라디오 버튼 생성
q5 = IntVar()
rd9 = Radiobutton(frame7,image=img_q5_1,variable=q5,value=8,indicatoron=False,overrelief='solid',selectcolor='red') # P성향 - value : 8
rd9.place(x=46,y=300)
rd10 = Radiobutton(frame7,image=img_q5_2,variable=q5,value=7,indicatoron=False,overrelief='solid',selectcolor='red') # J성향 - value : 7
rd10.place(x=46,y=400)

# 다음문항 버튼
btn_next = Button(frame7, image=img_next,borderwidth=1,overrelief='solid',command= lambda: [NextBtn(q5,frame8)])
btn_next.place(x=270,y=530)

# 이전문항 버튼
btn_before = Button(frame7, image=img_before,borderwidth=1,overrelief='solid',command= lambda:[OpenFrame(frame6)])
btn_before.place(x=100,y=530)
############################################################문항6
# 문제화면6 : frame8 - q6
# frame8 사진 호출
img_q6 = PhotoImage(file='image/q6.PNG') # 배경 - canvas
img_q6_1 = PhotoImage(file='image/q6_1.PNG')
img_q6_1 = img_q6_1.subsample(1)
img_q6_2 = PhotoImage(file='image/q6_2.PNG')
img_q6_2 = img_q6_2.subsample(1)

# fram6 생성 및 위치 지정
frame8 = Frame(window)
frame8.place(x=0,y=0) # 프레임 위치 (x=0,y=0) 통일

canvas8 = Canvas(frame8,height=710,width=503,bg='white')
canvas8.pack()
canvas8.create_image(250,335,image=img_q6)

# 문항6-체크하는 라디오 버튼 생성
q6 = IntVar()
rd11 = Radiobutton(frame8,image=img_q6_1,variable=q6,value=1,indicatoron=False,overrelief='solid',selectcolor='red') # I성향 - value : 1
rd11.place(x=46,y=300)
rd12 = Radiobutton(frame8,image=img_q6_2,variable=q6,value=2,indicatoron=False,overrelief='solid',selectcolor='red') # E성향 - value : 2
rd12.place(x=46,y=400)

# 다음문항 버튼
btn_next = Button(frame8, image=img_next,borderwidth=1,overrelief='solid',command= lambda: [NextBtn(q6,frame9)])
btn_next.place(x=270,y=530)

# 이전문항 버튼
btn_before = Button(frame8, image=img_before,borderwidth=1,overrelief='solid',command= lambda:[OpenFrame(frame7)])
btn_before.place(x=100,y=530)
############################################################문항7
# 문제화면7 : frame9 - q7
# frame9 사진 호출
img_q7 = PhotoImage(file='image/q7.PNG') # 배경 - canvas
img_q7_1 = PhotoImage(file='image/q7_1.PNG')
img_q7_1 = img_q7_1.subsample(1)
img_q7_2 = PhotoImage(file='image/q7_2.PNG')
img_q7_2 = img_q7_2.subsample(1)

# fram9 생성 및 위치 지정
frame9 = Frame(window)
frame9.place(x=0,y=0) # 프레임 위치 (x=0,y=0) 통일

canvas9 = Canvas(frame9,height=710,width=503,bg='white')
canvas9.pack()
canvas9.create_image(250,335,image=img_q7)

# 문항7-체크하는 라디오 버튼 생성
q7 = IntVar()
rd13 = Radiobutton(frame9,image=img_q7_1,variable=q7,value=3,indicatoron=False,overrelief='solid',selectcolor='red') # S성향 - value : 3
rd13.place(x=46,y=300)
rd14 = Radiobutton(frame9,image=img_q7_2,variable=q7,value=4,indicatoron=False,overrelief='solid',selectcolor='red') # N성향 - value : 4
rd14.place(x=46,y=400)

# 다음문항 버튼
btn_next = Button(frame9, image=img_next,borderwidth=1,overrelief='solid',command= lambda: [NextBtn(q7,frame10)])
btn_next.place(x=270,y=530)

# 이전문항 버튼
btn_before = Button(frame9, image=img_before,borderwidth=1,overrelief='solid',command= lambda:[OpenFrame(frame8)])
btn_before.place(x=100,y=530)
############################################################문항8
# 문제화면8 : frame10 - q8
# frame10 사진 호출
img_q8 = PhotoImage(file='image/q8.PNG') # 배경 - canvas
img_q8_1 = PhotoImage(file='image/q8_1.PNG')
img_q8_1 = img_q8_1.subsample(1)
img_q8_2 = PhotoImage(file='image/q8_2.PNG')
img_q8_2 = img_q8_2.subsample(1)

# fram10 생성 및 위치 지정
frame10 = Frame(window)
frame10.place(x=0,y=0) # 프레임 위치 (x=0,y=0) 통일

canvas10 = Canvas(frame10,height=710,width=503,bg='white')
canvas10.pack()
canvas10.create_image(250,335,image=img_q8)

# 문항8-체크하는 라디오 버튼 생성
q8 = IntVar()
rd15 = Radiobutton(frame10,image=img_q8_1,variable=q8,value=6,indicatoron=False,overrelief='solid',selectcolor='red') # F성향 - value : 6
rd15.place(x=46,y=300)
rd16 = Radiobutton(frame10,image=img_q8_2,variable=q8,value=5,indicatoron=False,overrelief='solid',selectcolor='red') # T성향 - value : 5
rd16.place(x=46,y=400)

# 다음문항 버튼
btn_next = Button(frame10, image=img_next,borderwidth=1,overrelief='solid',command= lambda: [NextBtn(q8,frame11)])
btn_next.place(x=270,y=530)

# 이전문항 버튼
btn_before = Button(frame10, image=img_before,borderwidth=1,overrelief='solid',command= lambda:[OpenFrame(frame9)])
btn_before.place(x=100,y=530)
############################################################문항9
# 문제화면9 : frame11 - q9
# frame11 사진 호출
img_q9 = PhotoImage(file='image/q9.PNG') # 배경 - canvas
img_q9_1 = PhotoImage(file='image/q9_1.PNG')
img_q9_1 = img_q9_1.subsample(1)
img_q9_2 = PhotoImage(file='image/q9_2.PNG')
img_q9_2 = img_q9_2.subsample(1)

# fram10 생성 및 위치 지정
frame11 = Frame(window)
frame11.place(x=0,y=0) # 프레임 위치 (x=0,y=0) 통일

canvas11 = Canvas(frame11,height=710,width=503,bg='white')
canvas11.pack()
canvas11.create_image(250,335,image=img_q9)

# 문항9-체크하는 라디오 버튼 생성
q9 = IntVar()
rd17 = Radiobutton(frame11,image=img_q9_1,variable=q9,value=7,indicatoron=False,overrelief='solid',selectcolor='red') # J성향 - value : 7
rd17.place(x=46,y=300)
rd18 = Radiobutton(frame11,image=img_q9_2,variable=q9,value=8,indicatoron=False,overrelief='solid',selectcolor='red') # P성향 - value : 8
rd18.place(x=46,y=430) # 좀 더 떨으뜨리기.

# 다음문항 버튼
btn_next = Button(frame11, image=img_next,borderwidth=1,overrelief='solid',command= lambda: [NextBtn(q9,frame12)])
btn_next.place(x=270,y=530)

# 이전문항 버튼
btn_before = Button(frame11, image=img_before,borderwidth=1,overrelief='solid',command= lambda:[OpenFrame(frame10)])
btn_before.place(x=100,y=530)
############################################################문항10
# 문제화면10 : frame12 - q10
# frame12 사진 호출
img_q10 = PhotoImage(file='image/q10.PNG') # 배경 - canvas
img_q10_1 = PhotoImage(file='image/q10_1.PNG')
img_q10_1 = img_q10_1.subsample(1)
img_q10_2 = PhotoImage(file='image/q10_2.PNG')
img_q10_2 = img_q10_2.subsample(1)

# fram10 생성 및 위치 지정
frame12 = Frame(window)
frame12.place(x=0,y=0) # 프레임 위치 (x=0,y=0) 통일

canvas12 = Canvas(frame12,height=710,width=503,bg='white')
canvas12.pack()
canvas12.create_image(250,335,image=img_q10)

# 문항10-체크하는 라디오 버튼 생성
q10 = IntVar()
rd19 = Radiobutton(frame12,image=img_q10_1,variable=q10,value=6,indicatoron=False,overrelief='solid',selectcolor='red') # F성향 - value : 6
rd19.place(x=46,y=300)
rd20 = Radiobutton(frame12,image=img_q10_2,variable=q10,value=5,indicatoron=False,overrelief='solid',selectcolor='red') # T성향 - value : 5
rd20.place(x=46,y=400) # 좀 더 떨으뜨리기.

# 다음문항 버튼
btn_next = Button(frame12, image=img_next,borderwidth=1,overrelief='solid',command= lambda: [NextBtn(q10,frame13)])
btn_next.place(x=270,y=530)

# 이전문항 버튼
btn_before = Button(frame12, image=img_before,borderwidth=1,overrelief='solid',command= lambda:[OpenFrame(frame11)])
btn_before.place(x=100,y=530)
############################################################문항11
# 문제화면11 : frame13 - q11
# frame13 사진 호출
img_q11 = PhotoImage(file='image/q11.PNG') # 배경 - canvas
img_q11_1 = PhotoImage(file='image/q11_1.PNG')
img_q11_1 = img_q11_1.subsample(1)
img_q11_2 = PhotoImage(file='image/q11_2.PNG')
img_q11_2 = img_q11_2.subsample(1)

# fram10 생성 및 위치 지정
frame13 = Frame(window)
frame13.place(x=0,y=0) # 프레임 위치 (x=0,y=0) 통일

canvas13 = Canvas(frame13,height=710,width=503,bg='white')
canvas13.pack()
canvas13.create_image(250,335,image=img_q11)

# 문항11-체크하는 라디오 버튼 생성
q11 = IntVar()
rd21 = Radiobutton(frame13,image=img_q11_1,variable=q11,value=4,indicatoron=False,overrelief='solid',selectcolor='red') # N성향 - value : 4
rd21.place(x=46,y=300)
rd22 = Radiobutton(frame13,image=img_q11_2,variable=q11,value=3,indicatoron=False,overrelief='solid',selectcolor='red') # S성향 - value : 3
rd22.place(x=46,y=400)

# 다음문항 버튼
btn_next = Button(frame13, image=img_next,borderwidth=1,overrelief='solid',command= lambda: [NextBtn(q11,frame14)])
btn_next.place(x=270,y=530)

# 이전문항 버튼
btn_before = Button(frame13, image=img_before,borderwidth=1,overrelief='solid',command= lambda:[OpenFrame(frame12)])
btn_before.place(x=100,y=530)
############################################################문항12
# 문제화면12 : frame14 - q12
# frame14 사진 호출
img_q12 = PhotoImage(file='image/q12.PNG') # 배경 - canvas
img_q12_1 = PhotoImage(file='image/q12_1.PNG')
img_q12_1 = img_q12_1.subsample(1)
img_q12_2 = PhotoImage(file='image/q12_2.PNG')
img_q12_2 = img_q12_2.subsample(1)

# fram14 생성 및 위치 지정
frame14 = Frame(window)
frame14.place(x=0,y=0) # 프레임 위치 (x=0,y=0) 통일

canvas14 = Canvas(frame14,height=710,width=503,bg='white')
canvas14.pack()
canvas14.create_image(250,335,image=img_q12)

# 문항12-체크하는 라디오 버튼 생성
q12 = IntVar()
rd23 = Radiobutton(frame14,image=img_q12_1,variable=q12,value=2,indicatoron=False,overrelief='solid',selectcolor='red') # E성향 - value : 2
rd23.place(x=46,y=300)
rd24 = Radiobutton(frame14,image=img_q12_2,variable=q12,value=1,indicatoron=False,overrelief='solid',selectcolor='red') # I성향 - value : 1
rd24.place(x=46,y=400)

# 제출하기 버튼
btn_submmit = Button(frame14, image=img_submmit,borderwidth=1,overrelief='solid',\
                    command= lambda:[SubmmitBtn(q12,frame15)])
btn_submmit.place(x=270,y=480)

# 이전문항 버튼
btn_before = Button(frame14, image=img_before,borderwidth=1,overrelief='solid',command= lambda:[OpenFrame(frame13)])
btn_before.place(x=100,y=530)
############################################################결과보기
# 결과화면 : frame15
# frame15 사진호출
img_resultpage = PhotoImage(file='image/resultpage.PNG') # 배경 - canvas

# fram15 생성 및 위치 지정

frame15 = Frame(window)
frame15.place(x=0,y=0) # 프레임 위치 (x=0,y=0) 통일

canvas15 = Canvas(frame15,height=710,width=503,bg='white')
canvas15.pack()
canvas15.create_image(250,335,image=img_resultpage)

# 결과보기 버튼
btn_result = Button(frame15, image= img_result,borderwidth=1,overrelief='solid',command= ResultBtn)
btn_result.place(x=145,y=285)
#############################################################

q_list = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12]
mbti_list = [0,0,0,0,0,0,0,0,0] 
result_list=[]
#인덱스 기준: 1-I / 2-E / 3-S / 4-N / 5-T / 6-F / 7-J / 8-P

#############################################################1457: #INTJ-전략가/frame16
# 최종 결과화면 : frame16
# fram16 생성 및 위치 지정 및 캔버스 생성
frame16 = Frame(window)
frame16.place(x=0,y=0) # 프레임 위치 (x=0,y=0) 통일

canvas16 = Canvas(frame16,height=710,width=503,bg='white')
canvas16.pack()
canvas16.create_image(250,335,image=img_f16)

# 다시하기 버튼
btn_restart= Button(frame16, image=img_restart,borderwidth=1,overrelief='solid',command=lambda:[OpenFrame(frame1)])
btn_restart.place(x=100,y=530)

# 종료하기 버튼
btn_end = Button(frame16, image=img_end,borderwidth=1,overrelief='solid',command= close)
btn_end.place(x=320,y=532)

# 링크 연결 버튼 및 종료
btn_web = Button(frame16,image=img_web,borderwidth=1,overrelief='solid',\
    command= lambda:[web('https://www.16personalities.com/ko/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95-intj'),close()])
btn_web.place(x=230,y=390)
#############################################################1458: #INTP-논리술사/frame17
# 최종 결과화면 : frame17
# fram17 생성 및 위치 지정 및 캔버스 생성
frame17 = Frame(window)
frame17.place(x=0,y=0) # 프레임 위치 (x=0,y=0) 통일

canvas17 = Canvas(frame17,height=710,width=503,bg='white')
canvas17.pack()
canvas17.create_image(250,335,image=img_f17)

# 다시하기 버튼
btn_restart= Button(frame17, image=img_restart,borderwidth=1,overrelief='solid',command=lambda:[OpenFrame(frame1)])
btn_restart.place(x=100,y=530)

# 종료하기 버튼
btn_end = Button(frame17, image=img_end,borderwidth=1,overrelief='solid',command= close)
btn_end.place(x=320,y=532)

# 링크 연결 버튼 및 종료
btn_web = Button(frame17,image=img_web,borderwidth=1,overrelief='solid',\
    command= lambda:[web('https://www.16personalities.com/ko/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95-intp'),close()])
btn_web.place(x=230,y=390)
############################################################# 2457: #ENTJ-통솔자/fram18
# 최종 결과화면 : frame18
# fram18 생성 및 위치 지정 및 캔버스 생성
frame18 = Frame(window)
frame18.place(x=0,y=0) # 프레임 위치 (x=0,y=0) 통일

canvas18 = Canvas(frame18,height=710,width=503,bg='white')
canvas18.pack()
canvas18.create_image(250,335,image=img_f18)

# 다시하기 버튼
btn_restart= Button(frame18, image=img_restart,borderwidth=1,overrelief='solid',command=lambda:[OpenFrame(frame1)])
btn_restart.place(x=100,y=530)

# 종료하기 버튼
btn_end = Button(frame18, image=img_end,borderwidth=1,overrelief='solid',command= close)
btn_end.place(x=320,y=532)

# 링크 연결 버튼 및 종료
btn_web = Button(frame18,image=img_web,borderwidth=1,overrelief='solid',\
    command= lambda:[web('https://www.16personalities.com/ko/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95-entj'),close()])
btn_web.place(x=242,y=390)
############################################################# 2458: #ENTP-변론가/frame19
# 최종 결과화면 : frame19
# fram19 생성 및 위치 지정 및 캔버스 생성
frame19 = Frame(window)
frame19.place(x=0,y=0) # 프레임 위치 (x=0,y=0) 통일

canvas19 = Canvas(frame19,height=710,width=503,bg='white')
canvas19.pack()
canvas19.create_image(250,335,image=img_f19)

# 다시하기 버튼
btn_restart= Button(frame19, image=img_restart,borderwidth=1,overrelief='solid',command=lambda:[OpenFrame(frame1)])
btn_restart.place(x=100,y=530)

# 종료하기 버튼
btn_end = Button(frame19, image=img_end,borderwidth=1,overrelief='solid',command= close)
btn_end.place(x=320,y=532)

# 링크 연결 버튼 및 종료
btn_web = Button(frame19,image=img_web,borderwidth=1,overrelief='solid',\
    command= lambda:[web('https://www.16personalities.com/ko/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95-entp'),close()])
btn_web.place(x=242,y=363)
############################################################# 1467: #INFJ-옹호자/frame20
# 최종 결과화면 : frame20
# fram20 생성 및 위치 지정 및 캔버스 생성
frame20 = Frame(window)
frame20.place(x=0,y=0) # 프레임 위치 (x=0,y=0) 통일

canvas20 = Canvas(frame20,height=710,width=503,bg='white')
canvas20.pack()
canvas20.create_image(250,335,image=img_f20)

# 다시하기 버튼
btn_restart= Button(frame20, image=img_restart,borderwidth=1,overrelief='solid',command=lambda:[OpenFrame(frame1)])
btn_restart.place(x=100,y=530)

# 종료하기 버튼
btn_end = Button(frame20, image=img_end,borderwidth=1,overrelief='solid',command= close)
btn_end.place(x=320,y=532)

# 링크 연결 버튼 및 종료
btn_web = Button(frame20,image=img_web,borderwidth=1,overrelief='solid',\
    command= lambda:[web('https://www.16personalities.com/ko/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95-infj'),close()])
btn_web.place(x=242,y=390)
#############################################################1468: #INFP-중재자/frame21
# 최종 결과화면 : frame21
# fram21 생성 및 위치 지정 및 캔버스 생성
frame21 = Frame(window)
frame21.place(x=0,y=0) # 프레임 위치 (x=0,y=0) 통일

canvas21 = Canvas(frame21,height=710,width=503,bg='white')
canvas21.pack()
canvas21.create_image(250,335,image=img_f21)

# 다시하기 버튼
btn_restart= Button(frame21, image=img_restart,borderwidth=1,overrelief='solid',command=lambda:[OpenFrame(frame1)])
btn_restart.place(x=100,y=530)

# 종료하기 버튼
btn_end = Button(frame21, image=img_end,borderwidth=1,overrelief='solid',command= close)
btn_end.place(x=320,y=532)

# 링크 연결 버튼 및 종료
btn_web = Button(frame21,image=img_web,borderwidth=1,overrelief='solid',\
    command= lambda:[web('https://www.16personalities.com/ko/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95-infp'),close()])
btn_web.place(x=230,y=390)
#############################################################2467: #ENFJ-선도자/frame22
# 최종 결과화면 : frame22
# fram22 생성 및 위치 지정 및 캔버스 생성
frame22 = Frame(window)
frame22.place(x=0,y=0) # 프레임 위치 (x=0,y=0) 통일

canvas22 = Canvas(frame22,height=710,width=503,bg='white')
canvas22.pack()
canvas22.create_image(250,335,image=img_f22)

# 다시하기 버튼
btn_restart= Button(frame22, image=img_restart,borderwidth=1,overrelief='solid',command=lambda:[OpenFrame(frame1)])
btn_restart.place(x=100,y=530)

# 종료하기 버튼
btn_end = Button(frame22, image=img_end,borderwidth=1,overrelief='solid',command= close)
btn_end.place(x=320,y=532)

# 링크 연결 버튼 및 종료
btn_web = Button(frame22,image=img_web,borderwidth=1,overrelief='solid',\
    command= lambda:[web('https://www.16personalities.com/ko/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95-enfj'),close()])
btn_web.place(x=230,y=390)
#############################################################2468: #ENFP-활동가/frame23
# 최종 결과화면 : frame23
# fram23 생성 및 위치 지정 및 캔버스 생성
frame23 = Frame(window)
frame23.place(x=0,y=0) # 프레임 위치 (x=0,y=0) 통일

canvas23 = Canvas(frame23,height=710,width=503,bg='white')
canvas23.pack()
canvas23.create_image(250,335,image=img_f23)

# 다시하기 버튼
btn_restart= Button(frame23, image=img_restart,borderwidth=1,overrelief='solid',command=lambda:[OpenFrame(frame1)])
btn_restart.place(x=100,y=530)

# 종료하기 버튼
btn_end = Button(frame23, image=img_end,borderwidth=1,overrelief='solid',command= close)
btn_end.place(x=320,y=532)

# 링크 연결 버튼 및 종료
btn_web = Button(frame23,image=img_web,borderwidth=1,overrelief='solid',\
    command= lambda:[web('https://www.16personalities.com/ko/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95-enfp'),close()])
btn_web.place(x=242,y=350)
#############################################################1357: #ISTJ-현실주의자/frame24
# 최종 결과화면 : frame24
# fram24 생성 및 위치 지정 및 캔버스 생성
frame24 = Frame(window)
frame24.place(x=0,y=0) # 프레임 위치 (x=0,y=0) 통일

canvas24 = Canvas(frame24,height=710,width=503,bg='white')
canvas24.pack()
canvas24.create_image(250,335,image=img_f24)

# 다시하기 버튼
btn_restart= Button(frame24, image=img_restart,borderwidth=1,overrelief='solid',command=lambda:[OpenFrame(frame1)])
btn_restart.place(x=100,y=530)

# 종료하기 버튼
btn_end = Button(frame24, image=img_end,borderwidth=1,overrelief='solid',command= close)
btn_end.place(x=320,y=532)

# 링크 연결 버튼 및 종료
btn_web = Button(frame24,image=img_web,borderwidth=1,overrelief='solid',\
    command= lambda:[web('https://www.16personalities.com/ko/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95-istj'),close()])
btn_web.place(x=242,y=385)
#############################################################1367: #ISFJ-수호자/frame25
# 최종 결과화면 : frame25
# fram25 생성 및 위치 지정 및 캔버스 생성
frame25 = Frame(window)
frame25.place(x=0,y=0) # 프레임 위치 (x=0,y=0) 통일

canvas25 = Canvas(frame25,height=710,width=503,bg='white')
canvas25.pack()
canvas25.create_image(250,335,image=img_f25)

# 다시하기 버튼
btn_restart= Button(frame25, image=img_restart,borderwidth=1,overrelief='solid',command=lambda:[OpenFrame(frame1)])
btn_restart.place(x=100,y=530)

# 종료하기 버튼
btn_end = Button(frame25, image=img_end,borderwidth=1,overrelief='solid',command= close)
btn_end.place(x=320,y=532)

# 링크 연결 버튼 및 종료
btn_web = Button(frame25,image=img_web,borderwidth=1,overrelief='solid',\
    command= lambda:[web('https://www.16personalities.com/ko/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95-isfj'),close()])
btn_web.place(x=242,y=380)
#############################################################2357: #ESTJ-경영자/frame26
# 최종 결과화면 : frame26
# fram26 생성 및 위치 지정 및 캔버스 생성
frame26 = Frame(window)
frame26.place(x=0,y=0) # 프레임 위치 (x=0,y=0) 통일

canvas26 = Canvas(frame26,height=710,width=503,bg='white')
canvas26.pack()
canvas26.create_image(250,335,image=img_f26)

# 다시하기 버튼
btn_restart= Button(frame26, image=img_restart,borderwidth=1,overrelief='solid',command=lambda:[OpenFrame(frame1)])
btn_restart.place(x=100,y=530)

# 종료하기 버튼
btn_end = Button(frame26, image=img_end,borderwidth=1,overrelief='solid',command= close)
btn_end.place(x=320,y=532)

# 링크 연결 버튼 및 종료
btn_web = Button(frame26,image=img_web,borderwidth=1,overrelief='solid',\
    command= lambda:[web('https://www.16personalities.com/ko/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95-estj'),close()])
btn_web.place(x=242,y=380)
#############################################################2367: #ESFJ-집정관/frame27
# 최종 결과화면 : frame27
# fram27 생성 및 위치 지정 및 캔버스 생성
frame27 = Frame(window)
frame27.place(x=0,y=0) # 프레임 위치 (x=0,y=0) 통일

canvas27 = Canvas(frame27,height=710,width=503,bg='white')
canvas27.pack()
canvas27.create_image(250,335,image=img_f27)

# 다시하기 버튼
btn_restart= Button(frame27, image=img_restart,borderwidth=1,overrelief='solid',command=lambda:[OpenFrame(frame1)])
btn_restart.place(x=100,y=530)

# 종료하기 버튼
btn_end = Button(frame27, image=img_end,borderwidth=1,overrelief='solid',command= close)
btn_end.place(x=320,y=532)

# 링크 연결 버튼 및 종료
btn_web = Button(frame27,image=img_web,borderwidth=1,overrelief='solid',\
    command= lambda:[web('https://www.16personalities.com/ko/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95-esfj'),close()])
btn_web.place(x=242,y=340)
#############################################################1358: #ISTP-장인/frame28
# 최종 결과화면 : frame28
# fram28 생성 및 위치 지정 및 캔버스 생성
frame28 = Frame(window)
frame28.place(x=0,y=0) # 프레임 위치 (x=0,y=0) 통일

canvas28 = Canvas(frame28,height=710,width=503,bg='white')
canvas28.pack()
canvas28.create_image(250,335,image=img_f28)

# 다시하기 버튼
btn_restart= Button(frame28, image=img_restart,borderwidth=1,overrelief='solid',command=lambda:[OpenFrame(frame1)])
btn_restart.place(x=100,y=530)

# 종료하기 버튼
btn_end = Button(frame28, image=img_end,borderwidth=1,overrelief='solid',command= close)
btn_end.place(x=320,y=532)

# 링크 연결 버튼 및 종료
btn_web = Button(frame28,image=img_web,borderwidth=1,overrelief='solid',\
    command= lambda:[web('https://www.16personalities.com/ko/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95-istp'),close()])
btn_web.place(x=239,y=375)
#############################################################1368: #ISFP-모험가/frame29
# 최종 결과화면 : frame29
# fram29 생성 및 위치 지정 및 캔버스 생성
frame29 = Frame(window)
frame29.place(x=0,y=0) # 프레임 위치 (x=0,y=0) 통일

canvas29 = Canvas(frame29,height=710,width=503,bg='white')
canvas29.pack()
canvas29.create_image(250,335,image=img_f29)

# 다시하기 버튼
btn_restart= Button(frame29, image=img_restart,borderwidth=1,overrelief='solid',command=lambda:[OpenFrame(frame1)])
btn_restart.place(x=100,y=530)

# 종료하기 버튼
btn_end = Button(frame29, image=img_end,borderwidth=1,overrelief='solid',command= close)
btn_end.place(x=320,y=532)

# 링크 연결 버튼 및 종료
btn_web = Button(frame29,image=img_web,borderwidth=1,overrelief='solid',\
    command= lambda:[web('https://www.16personalities.com/ko/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95-isfp'),close()])
btn_web.place(x=242,y=363)
#############################################################2358: #ESTP-사업가/frame30
# 최종 결과화면 : frame30
# fram30 생성 및 위치 지정 및 캔버스 생성
frame30 = Frame(window)
frame30.place(x=0,y=0) # 프레임 위치 (x=0,y=0) 통일

canvas30 = Canvas(frame30,height=710,width=503,bg='white')
canvas30.pack()
canvas30.create_image(250,335,image=img_f30)

# 다시하기 버튼
btn_restart= Button(frame30, image=img_restart,borderwidth=1,overrelief='solid',command=lambda:[OpenFrame(frame1)])
btn_restart.place(x=100,y=530)

# 종료하기 버튼
btn_end = Button(frame30, image=img_end,borderwidth=1,overrelief='solid',command= close)
btn_end.place(x=320,y=532)

# 링크 연결 버튼 및 종료
btn_web = Button(frame30,image=img_web,borderwidth=1,overrelief='solid',\
    command= lambda:[web('https://www.16personalities.com/ko/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95-estp'),close()])
btn_web.place(x=238,y=375)
#############################################################
# 최종 결과화면 : frame31
# fram31 생성 및 위치 지정 및 캔버스 생성
frame31 = Frame(window)
frame31.place(x=0,y=0) # 프레임 위치 (x=0,y=0) 통일

canvas31 = Canvas(frame31,height=710,width=503,bg='white')
canvas31.pack()
canvas31.create_image(250,335,image=img_f31)

# 다시하기 버튼
btn_restart= Button(frame31, image=img_restart,borderwidth=1,overrelief='solid',command=lambda:[OpenFrame(frame1)])
btn_restart.place(x=100,y=530)

# 종료하기 버튼
btn_end = Button(frame31, image=img_end,borderwidth=1,overrelief='solid',command= close)
btn_end.place(x=320,y=532)

# 링크 연결 버튼 및 종료
btn_web = Button(frame31,image=img_web,borderwidth=1,overrelief='solid',\
    command= lambda:[web('https://www.16personalities.com/ko/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95-esfp'),close()])
btn_web.place(x=239,y=340)
#############################################################
OpenFrame(frame1)
window.mainloop()