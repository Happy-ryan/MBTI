from tkinter import *
from tkinter import messagebox
import webbrowser
# 전체적 구조 : 총 31개(3+12+16)의 frame(page) 존재
# 버튼 1개(시작하기,넘어가기,결과보기) 있는 startpage,explainpage,donepage 3개 존재 > class StartPage
# 버튼 2개(이전문항, 다음문항) 있는 q1~q12 12개 > class QusetionPage
# 버튼 3개(다시하기,종료하기,링크연결하기) 있는 mbti 결과 16개 > class ResultPage
# main_happy의 전체적 순서
# 0. 사용할 이미지 호출
# 1. 전체 31개의 페이지 생성(이유 : 그래야 OpneFrame 함수 작동가능) 
# 2. 페이지 생성 후 버튼 추가(버튼은 각 클래스 메서드로 추가해놓는다.)
# 사용할 파일들
# main_happy > 메인실행코드
# class StartPage > 상속용
# class QusetionPage > 상속용
# class ResultPage > 상속용
# Uitls > 함수관리용
# Params > 변수관리용
from StartPage import StartPage
from QuestionPage import QuestionPage
from ResultPage import ResultPage
from Utils import *
from Params import *
############################################################
# 종료하기
def close():
    window.destroy()
# 외부 링크 열기
def web(web):
    webbrowser.open(web)
############################################################
window = Tk()
window.title('M Bㅏ프 T I')
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
# 시작화면: frame1

start_page = StartPage(window=window, 
                       img_background_path='image/startpage.PNG')

explain_page = StartPage(window=window, 
                       img_background_path='image/explainpage.PNG')

done_page = StartPage(window=window, 
                       img_background_path='image/resultpage.PNG')

question_pages = [ QuestionPage(window=window,
                      img_q_path=f'image/q{i}.PNG',
                      img_o1_path=f'image/q{i}_1.PNG',
                      img_o2_path=f'image/q{i}_2.PNG',
                      o1_pos=o_pos[i - 1][0],
                      o2_pos=o_pos[i - 1][1],
                      o1_value=o_values[i - 1][0],
                      o2_value=o_values[i - 1][1],
                    ) for i in range(1, 13)
                ]

result_pages = [ ResultPage(window=window,
                            img_background_path=f'image/f{i}.PNG'
                            ) for i in range(16, 32)]

#############################################################

start_page.add_next(img=img_click, pos=(120, 480), command=lambda: [OpenFrame(explain_page)])
explain_page.add_next(img=img_pass, pos=(135, 480), command=lambda: [OpenFrame(question_pages[0])])

question_pages[0].add_before(img=img_before, pos=(100, 530), command=NoBeforeBtn)
question_pages[0].add_next(img=img_next, pos=(270, 530), command=lambda: [NextBtn(question_pages[0].q_var, question_pages[1])])

question_pages[1].add_before(img=img_before, pos=(100, 530), command=lambda: [OpenFrame(question_pages[0])])
question_pages[1].add_next(img=img_next, pos=(270, 530), command=lambda: [NextBtn(question_pages[1].q_var, question_pages[2])])

question_pages[2].add_before(img=img_before, pos=(100, 530), command=lambda: [OpenFrame(question_pages[1])])
question_pages[2].add_next(img=img_next, pos=(270, 530), command=lambda: [NextBtn(question_pages[2].q_var, question_pages[3])])

question_pages[3].add_before(img=img_before, pos=(100, 530), command=lambda: [OpenFrame(question_pages[2])])
question_pages[3].add_next(img=img_next, pos=(270, 530), command=lambda: [NextBtn(question_pages[3].q_var, question_pages[4])])

question_pages[4].add_before(img=img_before, pos=(100, 530), command=lambda: [OpenFrame(question_pages[3])])
question_pages[4].add_next(img=img_next, pos=(270, 530), command=lambda: [NextBtn(question_pages[4].q_var, question_pages[5])])

question_pages[5].add_before(img=img_before, pos=(100, 530), command=lambda: [OpenFrame(question_pages[4])])
question_pages[5].add_next(img=img_next, pos=(270, 530), command=lambda: [NextBtn(question_pages[5].q_var, question_pages[6])])

question_pages[6].add_before(img=img_before, pos=(100, 530), command=lambda: [OpenFrame(question_pages[5])])
question_pages[6].add_next(img=img_next, pos=(270, 530), command=lambda: [NextBtn(question_pages[6].q_var, question_pages[7])])

question_pages[7].add_before(img=img_before, pos=(100, 530), command=lambda: [OpenFrame(question_pages[6])])
question_pages[7].add_next(img=img_next, pos=(270, 530), command=lambda: [NextBtn(question_pages[7].q_var, question_pages[8])])

question_pages[8].add_before(img=img_before, pos=(100, 530), command=lambda: [OpenFrame(question_pages[7])])
question_pages[8].add_next(img=img_next, pos=(270, 530), command=lambda: [NextBtn(question_pages[8].q_var, question_pages[9])])

question_pages[9].add_before(img=img_before, pos=(100, 530), command=lambda: [OpenFrame(question_pages[8])])
question_pages[9].add_next(img=img_next, pos=(270, 530), command=lambda: [NextBtn(question_pages[9].q_var, question_pages[10])])

question_pages[10].add_before(img=img_before, pos=(100, 530), command=lambda: [OpenFrame(question_pages[9])])
question_pages[10].add_next(img=img_next, pos=(270, 530), command=lambda: [NextBtn(question_pages[10].q_var, question_pages[11])])

question_pages[-1].add_before(img=img_before, pos=(100, 530), command=lambda: [OpenFrame(question_pages[10])])
question_pages[-1].add_next(img=img_submmit, pos=(270, 480), command=lambda: SubmitBtn(question_pages[-1].q_var, done_page, question_pages))

# for i in range(0, 11): # !! 람다 정의가 cur로 코드로 들어가서 문제가 됨 !!
#     cur = question_pages[i]
#     nxt = question_pages[i + 1]
#     print(f'cur: {cur.name}, nxt: {nxt.name}')
#     cur.add_next(img=img_next, pos=(270, 530), command=lambda: [NextBtn(cur.q_var, nxt)])
#     nxt.add_before(img=img_before, pos=(100, 530), command=lambda: [OpenFrame(cur)])
    
done_page.add_next(img=img_result, pos=(145, 285), command=lambda: [ResultBtn(result_pages)])

for page, pos, url in zip(result_pages, link_pos, link_urls):
    page.add_next(img=img_restart, pos=(100, 530), command=lambda:[OpenFrame(start_page)])
    page.add_end(img=img_end, pos=(320, 532), command=close)
    page.add_link(img=img_web, pos=pos, command=lambda: [web(url), close()])

OpenFrame(start_page)
window.mainloop()
