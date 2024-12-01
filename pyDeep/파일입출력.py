# I/O Stream
#표준 입/출력함수 -> input() / print()
#파일 입/출력함수 -> read(),readline(),readlines() / write(),writelines
#파일 입출력 과정 (파일열기->읽기,쓰기->닫기)
#파일 열기 -> 변수명=open("파일명","인자") /읽기용=r 쓰기용=w , r+=읽기/쓰기겸용, a=이어쓰기 , t=기본값(텍스트모드), b=이진파일 처리
#파일 닫기 -> 변수명.close()

#파일을 입력받아 표준출력 예시
""" inFb=None #입력파일
inStr="" #읽어온 문자열
inFb=open("/Users/haru/Data1.txt","r") #읽기전용으로 파일 열기 함수
inStr=inFb.readline() #첫라인 읽어오기
print(inStr,end="")
inStr=inFb.readline()
print(inStr,end="")
inStr=inFb.readline()
print(inStr,end="")
inFb.close() #파일 닫기 """
#표준출력 예시2
""" inFb=None 
inStr="" 
inFb=open("/Users/haru/Data1.txt","r")
while True:
    inStr=inFb.readline()
    if inStr == "":
        break
    else:
        print(inStr, end="")
inFb.close() """
#표준출력 예시3 - readlines사용
""" inFb=None 
inStr="" 
inFb=open("/Users/haru/Data1.txt","r")
inStr=inFb.readlines() #읽어온 문자열을 리스트형태로 저장
for s in inStr:
    print(s,end="")
inFb.close() """
#파일이 없을때 오류가 발생하지않게 하려면 os.path.exists(파일명)형식 사용
""" import os
inFb=None 
inStr="" 
fName=input("파일명 입력")
if os.path.exists(fName):
    inFb=open(fName,"r")
    inStr=inFb.readlines() #읽어온 문자열을 리스트형태로 저장
    for s in inStr:
        print(s,end="")
else:
    print("{}파일이 없습니다".format(fName))
inFb.close() """
#os.system(터미널명령어)이용해서 터미널 명령어 사용가능

#표준입력을 받아 파일출력 예시
""" outFp = None 
outStr = ""
outFp=open("/Users/haru/Data2.txt","w")
while True:
    outStr=input("내용입력")
    if outStr=="":
        break
    else:
        outFp.writelines(outStr+"\n")
outFp.close()
print("파일생성완료") """

#파일 입력->파일출력
""" inFp,outFp=None,None
inStr=""
inFp=open("/Users/haru/Data1.txt","r")
outFp=open("/Users/haru/Data2.txt","w")
inStr=inFp.readlines()
for s in inStr:
    outFp.writelines(s)
print("복사완료") """

#파일 암호화 및 암호해독
#파일의 내용을 암호화하고 파일을 다시 해독
#ord(문자를 숫자로 변경),chr(숫자를 문자로 바꿔주는 함수)
#print(ord("파"))
#print(chr(54028))
""" inFp,outFp=None,None
inStr,outStr="",""
i=0
securityCode=0                  #암호화 키값
secuYN=input("1.암호화,2.복호화")
inFname = input("입력파일명을 선택하세요")
outFname = input("출력파일명을 선택하세요")
if secuYN=="1":
    securityCode=100
elif secuYN=="2":
    securityCode=-100
inFp=open(inFname,'r',encoding="utf-8")
temp=[]
while True:
    inStr=inFp.readline()
    if not inStr: #읽어온값이 아무것도없을때 실행
        break
    outStr=""
    for i in range(0,len(inStr)): #암호화/복호화 알고리즘
        ch=inStr[i]
        chNum=ord(ch)
        chNum+=securityCode
        ch2=chr(chNum)
        outStr=outStr+ch2
    temp.append(outStr)
    #outFp.write(outStr)
outFp=open(outFname,'w',encoding="utf-8") #파일을 열때 파일내용을 다 지우고 시작함
for i in temp:
    outFp.writelines(i)
    print(i)
outFp.close()
inFp.close()
print("처리완료") """
#with A as B
#   Code
#형태로 작성시 A의 파일을 B에 저장후 해당 구문이 끝날때 자동으로 Close함