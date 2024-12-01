import CH4Function

def prompt() :
    print("0 : 종료")
    print('문제1번 : 성적의 평균과 학점')
    print('문제2번 : 두수와 연산자를 받아 계산')
    print('문제3번 : 월에따른 계절출력')
    print('문제4번 : 절댓값')
    print('문제5번 : 사과와 배, 거스름돈과 잔돈')
    print('문제6번 : 15,5,3의배수 판정')
    print('문제7번 : 비만도')
    print('문제8번 : A-B-C-D가 번갈아 청소할때 N일뒤의 당번')
    print('문제9번 : N일후의 요일')
    print('문제10번 : 세자리수 둘을 거꾸로 뒤집었을때 큰수출력')
    print('문제11번 : 태어난 년도와 띠 출력')
    print('문제12번 : 윤년판정')
    print('문제13번 : 30분후 시간출력')
    print('문제14번 : 30분전 시간출력')
    print('문제15번 : 커피주문 프로그램')
    print("16 : 프롬포트 다시보기")
    
def Choose():
    Num=int(input("확인할 문제의 번호를 입력하세요"))
    #if-else로 구분하는게 아니라 함수를 다넣은 클래스에 값을 입력해서 가져와보자
    if Num ==0:
        print("종료합니다..")
    elif Num==1:
        print("{}번문제 불러오는중...".format(Num))
        CH4Function.Q1()
        Choose()
    elif Num==2:
        print("{}번문제 불러오는중...".format(Num))
        CH4Function.Q2()
        Choose()
    elif Num==3:
        print("{}번문제 불러오는중...".format(Num))
        CH4Function.Q3()
        Choose()
    elif Num==4:
        print("{}번문제 불러오는중...".format(Num))
        CH4Function.Q4()
        Choose()
    elif Num==5:
        print("{}번문제 불러오는중...".format(Num))
        CH4Function.Q5()
        Choose()
    elif Num==6:
        print("{}번문제 불러오는중...".format(Num))
        CH4Function.Q6()
        Choose()
    elif Num==7:
        print("{}번문제 불러오는중...".format(Num))
        CH4Function.Q7()
        Choose()
    elif Num==8:
        print("{}번문제 불러오는중...".format(Num))
        CH4Function.Q8()
        Choose()
    elif Num==9:
        print("{}번문제 불러오는중...".format(Num))
        CH4Function.Q9()
        Choose()
    elif Num==10:
        print("{}번문제 불러오는중...".format(Num))
        CH4Function.Q10()
        Choose()
    elif Num==11:
        print("{}번문제 불러오는중...".format(Num))
        CH4Function.Q11()
        Choose()
    elif Num==12:
        print("{}번문제 불러오는중...".format(Num))
        CH4Function.Q12()
        Choose()
    elif Num==13:
        print("{}번문제 불러오는중...".format(Num))
        CH4Function.Q13()
        Choose()
    elif Num==14:
        print("{}번문제 불러오는중...".format(Num))
        CH4Function.Q14()
        Choose()
    elif Num==15:
        print("{}번문제 불러오는중...".format(Num))
        CH4Function.Q15()
        Choose()
    elif Num==16:
        prompt()
        Choose()
    else:
        print("유효한 번호를 입력해주세요")