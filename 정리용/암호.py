#파일 선택
#확장자가 Txt인지 확인
#암호키 입력
#암호키 스트링셋업
#개별 암호키 암호화
#문서 암호화
#문서와 개별암호키 스트링 순회하며 Xor연산

#복호화시에도 동일함

#암호화
st=ord("a")
key=ord("2")
res=bin(st^key)
#복호화
res=int(res,2)
res=bin(res^key)
res=int(res,2)
chr(res)
""" 
inFp,outFp=None,None
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