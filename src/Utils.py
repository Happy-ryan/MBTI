from tkinter import *
from tkinter import messagebox
import webbrowser
import Params

def OpenFrame(page): # 넘어가기, 다음문항 - 화면 전환 이벤트
    page.frame.tkraise()

def NoBeforeBtn(): # 이전문항 - frame3에서 이전 문항 없을 때 발생하는 이벤트
    messagebox.askokcancel('알림','이전문항이 존재하지 않습니다.')

def NextBtn(q, page): # 다음문항 - 다음문항 버튼 클릭할 때 발생하는 이벤트
    if q.get() == 0: # 응답하지 않았을 때 알림창
        messagebox.askokcancel('알림','응답하지 않은 항목이 있습니다.')
    else: # 다음 문항으로 넘어가도록 만들기
        OpenFrame(page)

def SubmitBtn(q, page, pages): # 제출하기버튼의 이벤트-q1~q12.get()값을 리스트에 넣고 mbti 결과 내는 함수
    mbti_list = [0 for _ in range(9)]
    if q.get() == 0:
        messagebox.askokcancel('알림','마지막 문항에 응답하지 않았습니다.')
    else:
        for p in pages:
            mbti_list[p.q_var.get()] += 1
        result_list = [i for i, x in enumerate(mbti_list) if x >= 2]
        Params.result = sum([x * 10**(3-i) for i, x in enumerate(result_list)])
        OpenFrame(page)
        print(mbti_list) 
        print(result_list)
        print(Params.result)

def ResultBtn(result_pages):
    if Params.result == 1457: #INTJ-전략가/frame16
        print('INTJ-전략가')
        OpenFrame(result_pages[0])
    elif Params.result ==1458: #INTP-논리술사/frame17
        print('INTP-논리술사')
        OpenFrame(result_pages[1])
    elif Params.result ==2457: #ENTJ-통솔자/fram18
        print('ENTJ-통솔자')
        OpenFrame(result_pages[2])
    elif Params.result ==2458: #ENTP-변론가/frame19
        print('ENTP-변론가')
        OpenFrame(result_pages[3])
    elif Params.result ==1467: #INFJ-옹호자/frame20
        print('INFJ-옹호자')
        OpenFrame(result_pages[4])
    elif Params.result ==1468: #INFP-중재자/frame21
        print('INFP-중재자')
        OpenFrame(result_pages[5])
    elif Params.result ==2467: #ENFJ-선도자/frame22
        print('ENFJ-선도자')
        OpenFrame(result_pages[6])
    elif Params.result ==2468: #ENFP-활동가/frame23
        print('ENFP-활동가')
        OpenFrame(result_pages[7])
    elif Params.result ==1357: #ISTJ-현실주의자/frame24
        print('ISTJ-현실주의자')
        OpenFrame(result_pages[8])
    elif Params.result ==1367: #ISFJ-수호자/frame25
        print('ISFJ-수호자')
        OpenFrame(result_pages[9])
    elif Params.result ==2357: #ESTJ-경영자/frame26
        print('ESTJ-경영자')
        OpenFrame(result_pages[10])
    elif Params.result ==2367: #ESFJ-집정관/frame27
        print('ESFJ-집정관')
        OpenFrame(result_pages[11])
    elif Params.result ==1358: #ISTP-장인/frame28
        print('ISTP-장인')
        OpenFrame(result_pages[12])
    elif Params.result ==1368: #ISFP-모험가/frame29
        print('ISFP-모험가')
        OpenFrame(result_pages[13])
    elif Params.result ==2358: #ESTP-사업가/frame30
        print('ESTP-사업가')
        OpenFrame(result_pages[14])
    elif Params.result ==2368: #ESFP-연예인/frame31
        print('ESFP-연예인')
        OpenFrame(result_pages[15])
