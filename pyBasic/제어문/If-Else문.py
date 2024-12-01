#제어문(조건문,반복문)
#조건문 : 주어진 조건에 맞는 구문이 실행된다(ifelse)
#반복문 : 주어진 횟수만큼 반복(for,while)
#비교연산자 == != > < >= <=
#비교시 리터럴은 Bool 자료형으로 나옴(True,False)
#논리연산자 and(양쪽모두 true일때) or(둘중하나라도 1일때) not
#Ifelse문의 구조
#if 조건식 :
#   수행코드
""" a=int(input("숫자를 입력하세요"))
if a==1:
    print('1입니다')
else:
    print('1이 아닙니다 ') """
#양수음수 구분
""" a=int(input("숫자를 입력하세요"))
n:bool=a==1
print('{}입니다'.format(n)) """
""" def plsub(a):
    if a>0:
        print('양수입니다')
    elif a<0:
            print('음수입니다')
    else:
        print('0입니다')
num=int(input())
plsub(num) """
#홀수짝수 구분
""" num=int(input())
end=num%10
if end%2==0:
    print("짝수입니다")
else:
    print("홀수입니다") """
#세수중 가장큰수 출력
""" a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
if a>b:
    if a>c:
        print(a) 
    else:
        print(c)
else:
    if b>c:
        print(b)
    else:
        print(c) """
#논리 연산활용해서 줄이기 가능함(A가 가장큰경우,B가가장 큰경우....)
""" a,b=input().split()
a=int(a)
b=int(b)
if a>b and a%2==0:
    print(a)
if b>a and b%2==0:
    print(b) """
#if(첫조건) elif(이전조건이 아난 N번째 조건) else(아무것도 아니면)
""" num=int(input())
if num>=1 and num<=4:
    print(num) """
