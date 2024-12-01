#클래스명은 대문자시작 명사, 메소드명은 소문자시작 동사, 여러개의 단어를 사용할때는 camel case{카멜케이스(각단어의 시작은 대문자로) }사용하기
#함수를 모아둔파일->라이브러리

#클래스
#객체지향프로그래밍의 기초개념
#class 클래스명: 으로 선언
#현실세계의 사물을 컴퓨터안에서 구현하려고 고안된 개념
#필드(변수)/메소드(함수)로 이루어짐
#클래스를 통해 만들어진 객채 -> 인스턴스
#인스턴스 생성 -> 인스턴스명 = 클래스명()
#메소드 호출->인스턴스명.메소드()
""" class Car:
    color=""
    speed=0
    
    def speedUp(self,value):
        self.speed +=value
    def speedDown(self,value):
        self.speed -= value
car1=Car()
car1.color = "Red"
car1.speed = 0

car2=Car()
car2.color = "Blue"
car2.speed = 0
car1.speedUp(30)
car2.speedUp(20)
print(car1.color) """
#클래스내부 메소드에서 필드를 사용할때, 첫인자는 무조건 self이다(클래스내부의 변수에 접근한다는 의미)
#self = 생성자
#인스턴스명 = 클래스명(값,값2)...
""" class Car:
    def __init__(self): #기본생성자 - 매개변수가 self만 있는 생성자, 인스턴스가 생성될때 자동으로 호출
        self.speed=0
        self.color="빨강" #여기서 필드가 생성되므로 따로 초기화 해줄필요없음
    #def __init__(self,v1,v2): #기본생성자 - 매개변수가 있는 생성자
    #    self.speed=v1
    #    self.color=v2 
    #    파이썬은 메소드 오버로딩이 없기 때문에 이름이 같은 함수 2개가 존재할수없음
    def speedUp(self,value):
        self.speed +=value
    def speedDown(self,value):
        self.speed -= value
car1=Car()
car2=Car()
print(car2.color) """

#메소드,변수 이름이 __으로 시작할시 Private, _으로 시작할시 Protected이다
#Private <- 클래스내부에서만 사용가능
#Protected <-상속받은 클래스에서도 사용가능
""" class Car :
    count=0 #init함수에서 초기화를 해주지않을때는 이렇게 해줘야함 #init으로 받는값이 아니므로 클래스변수이다. 객채생성시에 초기화 되지않음
    def __init__(self,name,speed):
        self.__name=name
        self.__speed=speed
        Car.count +=1 #클래스변수 접근
    def getName(self):
        return self.__name
    def getSpeed(self):
        return self.__speed  
car1,car2=None,None 
#None = null값
car1=Car("Audi",0)
car2=Car("Benz",30)
print(car1.getName(),car1.getSpeed(),car1.count)
print(car2.getName(),car2.getSpeed(),car2.count) """
#클래스변수와 인스턴스변수
#인스턴스변수 -> 인스턴스에 존재하며, 각 인스턴스간 공유되지않는다
    #car 클래스안 두개의 필드, 각각의 값이 공유되지않음
#클래스변수 -> 클래스 내부에 존재하며, 각 인스턴스간 공유된다
    #car클래스 내부 count변수, 각각의 값이 공유된다

#클래스의 상속
#상위 클래스의 필드와 메소드를 그대로 물려받는 새 클래스 정의
#클래스명 뒤에(부모클래스명) 으로 선언한다
""" class Car:
    def __init__(self):
        self.speed:int=0
    def upSpeed(self,value):
        self.speed+=value
        print("현재속도()슈퍼클래스:{}".format(self.speed))

class Sedan(Car): #서브클래스 선언방법, 다중상속도 지원함
    def upSpeed(self,value): #메소드 오버라이딩, 부모클래스의 메소드 변경가능
        self.speed=value
        if self.speed>150:
            self.speed=150
        else:
            super().upSpeed() #부모클래스의 메소드 호출법
        print("현재속도()서브클래스:{}".format(self.speed)) """

#그외의 함수
""" class Line:
    def __init__(self,length):
        self.length=length
        print(self.length,"길이의 선이 생성되었습니다")
    def __del__(self): #소멸자, 생성자와 반대로 인스턴스 삭제시 자동호출
        print(self.length,"길이의 선이 제거되었습니다")
    def __repr__(self):# 인스턴스를 print문으로 출력시 실행
        return '선의길이:'+str(self.length)
    def __add__(self,other): #인스턴스간 덧셈이 일어날때 실행
        return self.length + other.length
    def __lt__(self,other):#인스턴스간 비교연산자 사용시 호출(> < >= <= == !=)
        return self.length > other.length
    def __eq__(self,other):
        return self.length == other.length   
myLine1 = Line(100)
myLine2 = Line(200)

print(myLine1)
print(myLine1+myLine2)
if myLine1<myLine2 :
    print("선분2가 더 길어요")
elif myLine1 == myLine2:
    print('길이가 같습니다')
else:
    print("null")
del(myLine2) """
#추상 메소드
#슈퍼클래스에서 메소드의 이름만 정의해두고 서브클래스에서 재정의하는것

#여러개의 함수를 동시에 실행시키는 Thread
""" import time
import threading #여러개의 함수가 동시에 실행되게할수있음
class RacingCar:
    def __init__(self,name):
        self.carName=name
    def runCar(self):
        for _ in range(0,3):
            carStr=self.carName+'Run\n'
            print(carStr,end='')
            time.sleep(1)# 1초 딜레이
car1=RacingCar("1")
car2=RacingCar("2")
car3=RacingCar("3")
th1 = threading.Thread(target=car1.runCar) #Thread 사용법
th2 = threading.Thread(target=car2.runCar) #Thread 타겟추가
th3 = threading.Thread(target=car3.runCar)
th1.start() #함수 실행
th2.start()
th3.start() """
