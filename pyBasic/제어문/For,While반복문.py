#for 반복문 구조
#for 변수명 in "range(횟수)": ""자리에는 String, List, Dicrionart, Tuple등의 자료형 위치가능함
#range()안의 숫자가 0부터 차례로 변수안에 들어가면서 반복하는 구조, 숫자만큼 반복함(5를 지정했다면 0,1,2,3,4 로 들어감)
#range(시작값,종료값,증가값) // 시작값기본:0, 종료값 -1까지 대입, 증가값기본= +1
""" for i in range(1,11):
    print("Out", i, end=" ") """
""" for i in range(10,0,-1):
    print("Str",i) """
# for i in reversed(range(11)):
""" for i in "string": # 문자열 순환
   print(i)
 """
""" sum=0
for i in range(1,11):
    sum+=i
print(sum) """
#복합연산자
#변수 연산자= 변수
#변수에 연산을 진행한 값을 다시 넣음
""" for i in range(1,31):
    if i%5==0:
        print(i)
    else:
        print(i,end="\t") """



#반복문 Ver
"""  
st="It is a fun Python class"
a_cnt,s_cnt=0,0
for i in st:
    if i=="a"or i=="A":
        a_cnt +=1
    elif i=="s"or i=="s":
        s_cnt+=1
print("a의 개수는{}개, s의 개수는{}개 입니다.".format(a_cnt,s_cnt)) """
#Iterator Ver
""" 
st="It is a fun Python class"
a_cnt,s_cnt=0,0
IT=iter(st)
while True:
    try:
        key = next(IT)
        if key=="s":
            s_cnt +=1
        elif key=="a":
            a_cnt +=1
    except StopIteration:
        break
print("a의 개수는{}개, s의 개수는{}개 입니다.".format(a_cnt,s_cnt)) """
#수를 입력받아 1~입력받은수까지 짝수의 합과 홀수의합 출력
""" num=int(input("수를 입력하세요"))
odd=0
even=0
od=[]
ev=[]
for i in range(1,num+1):
    if i%2==0:
        even+=i
        ev.append(i)
    else:
        odd+=i
        od.append(i)
print("1부터 {}까지 짝수는{}이고 합은{},\n 홀수는{}이며 합은{}입니다".format(num,ev,even,od,odd)) """
#두수를 입력받아 입력받은 두수의 범위내 합 구하기
a,b = map(int,input().split())
sum=0
if b>a:
    for i in range(a,b+1):
        sum+=i
elif a>b:
    for i in range(b,a+1):
        sum+=i
else:
    sum=a
print(sum)

#map(자료형,input().split()) <- 원하는 자료형으로 입력받기
#map(a,b) B리스트의 모든요소에 자료형을 a로 바꾸는 함수사용, # B의 모든 요소에 A함수 사용
#range()사용도 가능함 <- 반복가능한 모든 객체에 적용가능함

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