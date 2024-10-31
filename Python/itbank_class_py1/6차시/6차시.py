#중첩 반복문
#for(i;i<5;i++) {for(j<=i;j=0,j--) } 형태의 반복문
""" for i in range(3):
    print(1)
    for j in range(2):
        print(2) """
"""for i in range(3):
    for j in range(3):
        print("i : {}   j={}".format(i,j))"""
""" for j in range(2,10):
    for i in range(1,10):
        print("{}X{}={}".format(i,j,i*j),end=" ")
    print() """
#while 반복문
#while 조건식 : 코드 형태로 이루어짐
""" i=0
while i<=5:
    print(i)
    i+=1 """
#While 조건식 자리에 True가 들어오면 무한반복이 가능함
#break 사용시에 반복이 종료됨 이후에 코드가 있더라도 즉시 해당반복문을 나가기떄문에 break뒤쪽 코드는 실행이 안됨
#continue <- 반복문의 처음으로 돌아감, 이것도 아래코드는 실행하지않고 처음으로 돌아감
#횟수를 중요시하는 반복은 FOR문 사용 , 특정 조건을 중요시하는 반복문은 While사용
""" while True:
    key=input("수를 입력하세요")
    key=int(key)
    if key==0:
        print("중단합니다")
        break
    else:
        print(key)
        continue#(생략가능) """
#import <-time(코드 실행시간 제어), os = 터미널 명령어 사용가능