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
#파이썬에서 .2f등으로 소수점 자리를 줄이면 반올림한다

#세자리수입력후 각 자리수 출력
num=int(input())
print("{}".format(num-(num//10*10)))
print("{}".format(num-(num//100*100)))
print(num)
# // =몫 , %=나머지 , / = 실수형태로 나누기 