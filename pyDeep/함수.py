#함수
#def 함수명(매개변수,...)
""" def plus(v1,v2):
    sum=v1+v2
    return int(sum)
print("1+2={}".format(plus(1,2))) """ #C스타일의 서식문자 복습하기
#사칙연산함수
""" def psmd(n1,n2,oper):
    res=0
    if oper == "*":
        res=n1*n2
    elif oper=='+':
        res=n1+n2
    elif oper=='-':
        res=n1-n2
    elif oper=='/':
        res=n1/n2 
    return res """

#두수의 공약수 찾기
""" num1,num2=map(int,input().split())
a_list=[]
if num1<num2:
    for i in range(1,num1+1):
        if num1 % i==0 and num2%i==0:
            j=i
            a_list.append(i)
else:
    temp=num1
    num1=num2
    num2=temp
    for i in range(1,num1+1):
        if num1 % i==0 and num2%i==0:
            j=i
            a_list.append(i)
print(a_list)
print(j) """#논리연산자 활용 잘하기
#약수개수 출력함수
#변수,함수 이름을 한글로 해도 된다.
""" def 약수개수(약수의개수):
    li_1=[]
    for i in range(1,약수의개수+1):
        if 약수의개수%i ==0:
            li_1.append(i)
    return len(li_1)
print(약수개수(int(input("수를 입력하세요:"))))
 """
#소수판별
""" li_1=[]
n=int(input())
for i in range(1,n+1):
    if n%i ==0:
        li_1.append(i)
if len(li_1)==2:
    print("소수입니다")
else:
    print("소수가 아닙니다") """
#소수판별 함수Ver.
""" def minor (N):
    cnt=0
    for i in range(2,N):
        if N%i==0:
            return False
    return True
num=int(input())
print(minor(num)) """
#완전수 출력프로그램
#자기자신을 제외한 약수를 모두 더했을때 합이 자신인수
""" def perfection(N):
    li_1=[]
    li_2=[]

    for i in range(1,N+1):  
        sum=0 
        for j in range(1,i):
            if i%j ==0:m
                sum+=j 
        if sum==i:
            li_2.append(i)

    return li_2
num = int(input("수를 입력하세요"))
print(perfection(num)) """


#지역변수와 전역변수
#함수,클래스내부에 선언된변수 -> 지역변수
#함수,클래스 외부에 선언된변수 ->전역변수
#지역변수는 해당함수, 해당클래스 안에서만 사용이 가능함
#전역변수는 프로그램 전체에서 사용이 가능함
#global 키워드 사용시에는 함수/클래스 안에서 전역변수를 생성할수있음

#재귀함수 팩토리얼
""" def fact(x):
    if x==1:
        return 1
    return x * fact(x-1)
 """
#반환값이 여러개인함수도 지정가능함
#리스트형태로 함수의 반환값을 설정
#함수의 입력값 위치에서 변수 초기화를 하면, 해당변수가 입력이 되지않아도 실행이 잘된다 <-기본값설정
# *변수 <- 가변인자
# *을 붙이면 인자를 튜플로 받는다는 의미임
""" def para(*par):
    res = 0
    for i in par:
        res+=i
    return res
print(para(3,2,1)) """
#딕셔너리형태의 입력 (**)
""" def dic_func (**para):
    for k in para.keys():
        print("{} ==> {}명 입니다".format(k,para[k]))
dic_func(a=1,b=2,c=3) """
#딕셔너리 형태로 값을 받음 a=1형태의 값을 입력할시 =을 기준으로 키와 값을 나눔
#딕셔너리의 키를 리스트형태로 이용하는 원리

#과제 - 로또추첨프로그램
#함수이용해서 1~45까지의 난수생성
#무한반복, 중복검사, 오름차순으로 정렬, for문을 이용해 로또번호 출력
""" def getNumber():
    numbers=random.sample(range(1,46),6)
    return numbers
numbers = getNumber()
numbers.sort()
print(numbers) """

""" def quick_sort(array): #퀵정렬 알고리즘
	if len(array) <= 1:
		return array
	pivot = len(array) // 2
	front_arr, pivot_arr, back_arr = [], [], []
	for value in array:
		if value < array[pivot]:
			front_arr.append(value)
		elif value > array[pivot]:
			back_arr.append(value)
		else:
			pivot_arr.append(value)
	return quick_sort(front_arr) + quick_sort(pivot_arr) + quick_sort(back_arr)

import random
def getNumber():
    num=random.randrange(1,46) # 1~45까지의 정수 랜덤 추출
    return num
res=[]                          #결과값배열
while len(res)<6:               #숫자 6개가 되면 루프종료
    num=getNumber()             #선추출
    if num not in res:          #기존배열과 비교해 중복이 아닐시 삽입
        res.append(num)         
res=quick_sort(res)             #오름차순정렬
print(res) """
#람다함수 : 괄호없이 쓰는함수, 단순연산, 자료형 변환시에 사용하면 편하다
""" myList=[1,2,3,4,5]
def add10(num):
    return num+10
for i in range(len(myList)):
    myList[i] = add10(myList[i])
print(myList) """
#이렇게 선언
""" myList=[1,2,3,4,5]
add10 = lambda num : num+10
myList = list(map(add10,myList))
print(myList) """
#map(a,b) -> b의 모든값에 a함수 사용

""" def outFunc(v1,v2): #외부함수
    def inFunc(num1,num2): #내부함수
        return num1+num2
    return inFunc(v1,v2) """
#함수내부에 함수선언도가능함
#함수외부에서는 내부함수 호출이 불가능하다

#재귀함수
#함수내부에서 자기자신을 호출하는 함수
""" def recursion(num):
    if num<=1:
        return 1
    else:
        return num*recursion(num-1)
nm = recursion(5)
print(nm) """
#재귀함수 알고리즘 문제 풀어보기, 어려운 개념이라 활용할줄 알아야함

#369 알고리즘
""" def Check369(num):
    try:
        if int(num)<100 and int(num)>0:
            if "3" in num or "6" in num or "9" in num: print("crap")
            else: Check369((input("NextNumber")))
        else: print("유효값을 입력해주세요")
    except ValueError: print("유효값을 입력해주세요")
Check369(input("수 입력")) """

#1~10까지 범위의 자연수를 입력받아서 1이면 10까지, 2면 20까지의 합을 구하는 함수
def one2nt(num):
    sum=0
    for i in range(1,num*10+1): sum+=i
    return sum
num=int(input("숫자를 입력하세요"))
if num>0 and num<10: print("1부터{}까지의 합:{}".format(num*10,one2nt(num)))
else: print("유효값을 입혁하세요")