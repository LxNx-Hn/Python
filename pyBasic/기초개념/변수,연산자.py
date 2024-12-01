#변수 : 값을 저장할때 사용하는 식별자
#변수선언 : pi=3.1415926535897977245485.... (변수생성)
#변수 할당 : print(pi) (변수에 값할당)
#변수참조 : >>3.14 (번수에서 값을 꺼냄)
#정수(int),실수(float),문자열(str)... 할당가능
a=int(1234)
b=float(3.14)
c=str("str")
print(a,b,c, sep=",")
print(type(a)) #타입확인가능 타입에러 발생시 타입확인하기
#식별자 : 프로그래밍 언어에서 이름을 붙일때 사용하는단어, 변수 또는 함수의 이름으로 사용
# 키워드 사용불가, 특수문자는 _만 허용, 숫자로 시작하면 사용불가,공백을 포함할수없음
import keyword
print(keyword.kwlist)
#키워드 클래스안에 있는 키워드 확인가능
#print는 키워드가 아니지만, 만약 이를 변수로 사용해 할당한다면 더이상 출력기능을 하지못함 (메소드 오버라이딩)
#저런함수 판별법 -> 쳐봤는데 색깔나오면 이미 정의된 함수임
#변수 이름은 변수가 담고있는 내용을 한눈에 알수있게 지어야편하다
# 클래스명은 대문자시작 명사, 메소드명은 소문자시작 동사, 여러개의 단어를 사용할때는 camel case{카멜케이스(각단어의 시작은 대문자로) }사용하기



# **2 ->제곱계산법
# 파이썬은 / 연산자 사용시 자동으로 실수로 처리해준다
# a = int(input(---)) 변수안에 n타입을 저장 --- =입력받을떄 출력할 문구 // 타입기본은 문자열
""" name = input("이름을 입력하세요")
age =  input('나이를 입력하세요')
mail=input('메일을입력하세요')
print(name,age,mail)
 """
#두수를 입력후 +-연산출력프로그램
#cmd+[,]= 왼쪽, 오른쪽 들여쓰기
""" print("두정수의 합과 차를 구하는 프로그램입니다")
try:
    num1=int(input("첫번째 수 입력 : "))
    num2=int(input("두번째 수 입력 : "))
except ValueError:
    print("정수를 입력해주시기 바랍니다")
else:
    sum=int(num1+num2)
    sub=num1-num2
    print("두 정수의 합=",sum,sep="",end='')
    print("  두 정수의 차=",sub,sep='') """
#여기서 sum의 타입을 int로 지정할때 int(sum)형태로 감싸면 왜 안될까....
#int() - 괄호안의 자료 형변환 , 따라서 int(sum)에서 sum안에 자료가 없기때문에 에러가 난다
#int 지정법 -> 변수 선언 = 자료형()
#sum = int(sum) <- 자료형변경 예시
#a : int =3 <-자료형 설정법
""" math = int(input('수학점수를 입력하세요'))
eng  = int(input("영어점수를 입력하세요"))
avg  = float((math+eng)/2)
print("평균은 {:.1f}점 입니다".format(avg)) """
#cmd + opt ^ 커서 줄 늘리기(여러줄 선택할때 좋음)
""" hour=int(input("시 입력 : "))
min=int(input("분 입력 : "))
sec=int(input("초 입력 : "))
total=hour*3600 + min*60 +sec
print(total) """
#리스트버전
#a, b=input().split() 처럼 쓰면 cin<<과 비슷하게 사용가능함.
""" HMS=input("시,분,초 입력")
HMS=HMS.split()
hour=int(HMS[0])
min=int(HMS[1])
sec=int(HMS[2])
total=hour*3600 + min*60 +sec
print(total) """
""" celcius =float(input())
farenheit=celcius*1.8+32
print("{:.2f}°F".format(farenheit)) """
#celcius : float로 변수정의를 하면 왜 아래쪽에서 에러가 뜰까..
#celcius:float=input() <- 실수형 선언후 스트링값을 집어넣었기때문?
#파이썬에서는 자료형지정이 완벽하지않아서, 실수로 선언했지만 스트링값을 넣으면 스트링값이 된다.
#파이썬에서 .2f등으로 소수점 자리를 줄이면 반올림한다

#세자리수입력후 각 자리수 출력
""" num=int(input())
num1 = num%10
num2 = num%100
num3 = num%1000
print("{}".format(num1))
print("{}".format(num2))
print(num3)
print(num1)
print(num2//10)
print(num3//100) """
# // =몫 , %=나머지 , / = 실수형태로 나누기 
#여러 실행단위 코드를 짜면 주석처리하기 귀찮으니 함수로 해보기
#제발 깃허브 공부하기 제발... 기본용어같은거 정리한번 해야할듯 
""" def birth():
    try:
        birth=int(input()) #00000000
    except ValueError:
        print('유효한 값을 입력해주세요')
    else:
        if birth>=10000000 and birth<=99999999:
            year= birth//10000
            day=birth%100
            month=(birth%10000)//100
            print(year,month,day)
        else:
            print('유효한 값을 입력해주세요')
birth() """
#기준점을 잡고 몇으로 나눌지 정한뒤 왼쪽값=// 오른쪽값= %