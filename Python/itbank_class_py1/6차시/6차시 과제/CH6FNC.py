#쌀1통=1kg, 100통 저장
#쥐는 암수한쌍이며 한마리당 하루에 20g씩 먹고 10일마다 쥐의수가 2배씩 증가, 며칠만에 쌀이 다 사라지며 쥐는 총 몇마리일까
#쌀을 먹은뒤 두배증가함
def Q1():
    rat=2
    rice=100000
    roopcnt=0
    while rice>0:
        rice-= 20*rat
        roopcnt+=1
        if roopcnt%10== 0:
            rat*=2
    print("쌀이사라지는데 {}일, 쥐의수={}마리".format(roopcnt,rat))
#자판기 프로그램
def Q2():
    m = 0
    while True:
        print("---- Menu ----")
        print("1. 콜라 / 300")
        print("2. 사이다 / 300")
        print("3. 커피 / 300")
        print("4. 돈 넣기")
        print("5. 잔돈 반환")
        print("6. 종료")
        print("---------------")
        print("현재 금액", m)
        menu = int(input("메뉴 선택: "))
        print()
        if menu == 1:
            if m < 300:
                print("금액이 부족합니다.")
            else:
                print("콜라 맛있게 드세요!")
                m -= 300

        elif menu == 2:
            if m < 300:
                print("금액이 부족합니다.")
            else:
                print("사이다 맛있게 드세요!")
                m -= 300

        elif menu == 3:
            if m < 200:
                print("금액이 부족합니다.")
            else:
                print("커피 맛있게 드세요!")
                m -= 300

        elif menu == 4:
            money = int(input("돈을 넣어주세요: "))
            m += money

        elif menu == 5:
            print("{:,}원의 잔액이 반환됩니다.".format(m))

        elif menu == 6:
            print("종료")
            break

        else:
            print("잘못입력하셨습니다.")
    
#시작값과 끝값사이의 7의배수 한줄출력
def Q3():
    st,en=map(int,input("시작값과 끝값을 입력하세요 :").split())
    for i in range(st,en+1):
        if i%7==0:
            print(i)
        else:
            print(i,end="\t") 
#1-10까지 짝수 홀수합을 for로 구현
def Q4():
    num=10
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
    print("1부터 10까지 짝수는{}이고 합은{},\n 홀수는{}이며 합은{}입니다".format(ev,even,od,odd))
#1-10짝수 홀수합 while로 구현
def Q5():
    num=10
    odd=0
    even=0
    od=[]
    ev=[]
    i=1
    while i<=num:
        if i%2==0:
            even+=i
            ev.append(i)
            i+=1
            continue
        else:
            odd+=i
            od.append(i)
            i+=1
            continue
    print("1부터 10까지 짝수는{}이고 합은{},\n 홀수는{}이며 합은{}입니다".format(ev,even,od,odd))

#첫날에 10원예금,다음날에는 전날의 2배 예금할때 30일동안 저축한 금액
def Q6():
    total=0
    inp=10
    for i in range(1,31):
        total+=inp
        inp*=2
    print("30일 예금 총금액 = {}".format(total))
#두가지방법으로 이중for문활용 , 12345 \n 678910 ...~25까지 출력
def Q7():
    for i in range(0,21,5):
        for j in range(i+1,i+6):
            print(j,end ="\t")
        print("")
    
    for loop in range(5):
        for num in range(1,6):
            print(num+loop*5,end="\t")
            num+=1
        print()
        loop+=1

            
#계절구하기 While사용
def Q8(): #월을 입력받은후 해당하는 계절출력
    try:
        while True:
            month=int(input("월을 입력해주세요 :"))
            if month>=1 and month<=3:
                print("{}월의 계절은 봄입니다".format(month))
                break
            elif month>=4 and month<=6:
                print("{}월의 계절은 여름입니다".format(month))
                break
            elif month>=7 and month<=9:
                print("{}월의 계절은 가을입니다".format(month))
                break
            elif month>=10 and month<=12:
                print("{}월의 계절은 겨울입니다".format(month))
                break
            else:
                print('입력이 바르지 않습니다')
                continue
    except ValueError:
       print('입력이 바르지 않습니다')
       
    except TypeError:
        print('입력이 바르지 않습니다')

#중첩 for로 10^5 사이즈 별
def Q9():
    for i in range(5):
        for j in range(10):
            print("*",end="  ")
        print()
#while로도
def Q10():
    i=6
    while i>0:
        j=10
        while j>0:
            print("*",end="  ")
            j-=1
        print()
        i-=1
#13579....별피라미드
#피라미드 다시 생각해서 해보기

#5줄의 피라미드 찍기시 
#공백 5칸과 별 1칸
#4 3
#3 5
#2 7
#1 9

#i가 5->1으로 갈떄 공백과 별의개수  = 루프카운트+6
#공백=i
#5->1일때 공백은 n 별은 루프카운트 *2-1

#1가 1에서 5로가게되면
#공백 = 5->1
#별 = i*2-1

#무엇을 기준으로 잡아도 가능하다
#반복문에서 변수로 사용해야할 인자를 찾고, 각인자간의 관계, 루프카운트와의 관계를 파악하면 쉬워진다

def Q11():
    output = ""
    print()
    for i in range(1, 10):
        for j in range(9, i, -1):
            output += ' '
        for j in range(0, 2 * i -1):
            output += '*'
        output += '\n'

    print(output)

#역피라미드
def Q12():
    output = ""
    for i in reversed(range(1, 10)):
        for j in range(9, i, -1):
            output += ' '
        for j in range(0, 2 * i -1):
            output += '*'
        output += '\n'

    print(output)
""" for i in range(10,9,-1):
    print("*") """

def ex():
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
    print("a의 개수는{}개, s의 개수는{}개 입니다.".format(a_cnt,s_cnt))
def Q13():
    # 별 피라미드 만들기
    leng=int(input("높이를 입력해주세요"))
    for i in range(leng+1):
        output=""
        #높이 5 -> 별= 13579일때 높이 *2-1만큼이 최종별의개수
        #51 43 35 27 19
        for j in range(leng,i,-1):
            output+=" "
        for j in range(i*2-1):
            output+="*"
            pass
        print(output)
