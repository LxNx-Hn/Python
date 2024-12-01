#GUI Graphic User Interface
#윈도우 프로그래밍의 기본문장
""" from tkinter import *   #tkinter(GUI관련 모듈을 제공하는 표준 윈도우 라이브러리)안의 모든내용 가져옴
window=Tk()                 #기본이되는 윈도우 반환, 루트윈도우/윈도우 베이스라고 하며 실행시 화면에 출력
window.mainloop() """       #함수실행

#윈도우 크기조절
""" from tkinter import * 
window=Tk()
window.title("윈도우창 연습")                      #제목 설정
window.geometry("400x100")                      #초기 창크기 설정(단위=픽셀)
window.resizable(width=FALSE,height=FALSE)      #창크기 고정 ,True인자 사용시 조정가능
window.mainloop() """

#레이블 - 문자를 표현할수있는 위젯
""" from tkinter import *  
window=Tk()
lable1=Label(window,text="Jinx")
lable2=Label(window,text="Was" ,font=("Marker felt",30),fg="skyblue")
lable3=Label(window,text="Here",font=("Marker felt",30) ,fg="magenta",bg="blue",width=20,height=5,anchor=SE)
lable1.pack() #실행함수
lable2.pack()
lable3.pack()
window.mainloop() """
#사진 표현
#PhotoImage는 GIF파일만 지원함,
""" from tkinter import *  
window=Tk()
photo=PhotoImage(file='/Users/haru/Jinx/Jinx 색감조정.png')  #이미지파일 준비
label1=Label(window, image=photo) #Label의 옵션 image속성을 가짐
label1.pack()
window.mainloop() """

#버튼 만들기(종료)
""" from tkinter import *  
window=Tk()
button1=Button(window,text="QUIT",fg="Red",width=10,height=5,command=quit)
button1.pack()
window.mainloop() """
#버튼만들기(이미지 버튼)
""" from tkinter import *  
from tkinter import messagebox #메세지박스
window=Tk()
def Fnc():  #화면에 메세지 출력
    messagebox.showinfo("BUTTON","내용") #제목,내용 형식으로 출력
photo=PhotoImage('file=/Users/haru/Jinx/ICON.gif')
button1=Button(window,image=photo,command=Fnc)
button1.pack()
window.mainloop()  """
#체크 버튼 만들기
""" from tkinter import * 
from tkinter import messagebox
window=Tk()
def check():
    if chk.get()==0:
        messagebox.showinfo("","State=Off")
    else:
        messagebox.showinfo("","State=On")
chk=IntVar()
ch1=Checkbutton(window,text="Do click",variable=chk,command=check)
ch1.pack()
window.mainloop() """
#라디오 버튼
""" from tkinter import *  
window=Tk()
def Fnc():
    if var.get()==1:
        lable1.configure(text="Get")
    elif var.get()==2:
        lable1.configure(text="HERE")
    elif var.get()==3:
        lable1.configure(text="C")

var=IntVar() #정수형 변수 var준비
rb1=Radiobutton(window,text="Pew",variable=var,value=1, command=Fnc)
rb2=Radiobutton(window,text="Pew",variable=var,value=2, command=Fnc)
rb3=Radiobutton(window,text="Pew",variable=var,value=3, command=Fnc)
lable1=Label(window,text="Choise:",fg="red")
rb1.pack()
rb2.pack()
rb3.pack()
lable1.pack()
window.mainloop() """
#버튼 3개 배치
#수평정렬= Pack옵션중 left,right
#수직= top,buttom
""" from tkinter import *  
window=Tk()
buttonList=[]
buttonList.append(Button(window,text="1"))
buttonList.append(Button(window,text="2"))
buttonList.append(Button(window,text="3"))
for s in buttonList:
    s.pack(side=TOP,fill=X) #윈도우창 폭에 맞추는 방범, padx pady를 이용해서 여백설정도 가능함
                            #ipadx, ipady <-버튼 내부 여백설정
window.mainloop() """
#사진 9장을 버튼에 넣어 3X3으로 배치하는 코드
""" from tkinter import *  
from random import *
btnList=[""]*9
fnameList=["file=/Users/haru/Jinx/ICON.gif",...] #버튼저장용 9개 리스트
photoList=[None]*9 #PhotoImage로 생성할 리스트
i,k=0,0
xPos,yPos=0,0
num=0
window=Tk()
window.geometry("210x210")
shuffle(fnameList) #리스트 섞기
for i in range(0,9):
    photoList[i]=PhotoImage(file=fnameList[i])
    btnList[i]=Button(window,image=photoList[i])

for i in range(0,3): # 3x3번 반복하며 버튼생성
    for k in range(0,3):
        btnList[num].place(x=xPos,y=yPos) #그림출력 좌표사용,위젯을 고정위치에 배치시에는 pack대신 place사용
        num+=1
        xPos+=70# 그림을 x축으로 70픽셀 이동
    xPos =0
    yPos+=70 # Y축으로 70픽셀이동
window.mainloop() """

#이벤트 처리
#마우스 이벤트 처리
#<Button>모든버튼, <Button-1,2,3>왼쪽,가운데,오른쪽 -맥에서는 2가 오른쪽 클릭임
""" from tkinter import *  
from tkinter import messagebox

def click_left(event): #이벤트 발생시에 작동할 함수 정의
    messagebox.showinfo("MOUSE","GET JINXED")   
window=Tk()
window.geometry("100x100")
photo=PhotoImage(file='/Users/haru/Jinx/ICON.png')
lable1=Label(window,image=photo)
window.bind("<Button-1>",click_left) #클릭 감지 함수
lable1.pack(expand=1,anchor=CENTER)
#expand옵션을 yes로 사용할시 모든공간 사용
window.mainloop() """
#전체버튼 감지
""" from tkinter import *  
def click_mouse(event):
    txt=""
    if event.num==1:
        txt+="LEFT_CLICK("
    elif event.num==2:
        txt+="Right_CLICK("
    txt+=str(event.y) + ","+str(event.x)+")에서클릭됨"
    lable1.configure(text=txt)
window=Tk()
window.geometry("100x100")
lable1=Label(window,text="change")
window.bind("<Button>",click_mouse) #클릭 감지 함수
lable1.pack(expand=1,anchor=CENTER)
window.mainloop() """

#메뉴 만들기
""" from tkinter import *
window=Tk()
mainMenu=Menu(window) #부모윈도우로 메인메뉴 생성
window.config(menu=mainMenu)#생성된 메뉴를 윈도우의 메뉴로 지정
fileMenu=Menu(mainMenu) #상위메뉴 생성후 메뉴에 부착
mainMenu.add_cascade(label="파일",menu=fileMenu) #메뉴가 확장되어야 하므로  cascade사용
fileMenu.add_command(label="열기") #누를때 작동을 해야하므로 add_command사용
fileMenu.add_separator() #구분선 만들기
fileMenu.add_command(label="종료",command=quit)
window.mainloop()"""
#메뉴에 함수 연결하기
""" from tkinter import *
from tkinter import messagebox
def openMessage() :
    messagebox.showinfo("Open","파일 여는중")
window=Tk()
mainMenu=Menu(window) 
window.config(menu=mainMenu)
fileMenu=Menu(mainMenu) 
mainMenu.add_cascade(label="파일",menu=fileMenu)
fileMenu.add_command(label="열기",command=openMessage) 
fileMenu.add_separator()
fileMenu.add_command(label="종료",command=quit)
window.mainloop() """
#다이얼메뉴
""" from tkinter import*
from tkinter.simpledialog import*
window=Tk()
window.geometry("400x120")
lable1=Label(window,text="입력")
lable1.pack()

value=askinteger("확대변수",'주사위숫자를 입력하세요',minvalue=1,maxvalue=6)
lable1.configure(text=str(value))
window.mainloop() """



""" from tkinter import *  
window=Tk()
window.mainloop() """

#tkdesigner 사용으로 피그마랑 연결가능 <- 공부해보기