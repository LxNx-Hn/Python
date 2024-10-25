def Q1(): #수학과학 성적의 평균과 학점
    try:
        math,science = input('수학,과학성적을 입력하세요').split()
        math=int(math) 
        science=int(science)
        if math<0 or math>100 or science<0 or science>100:
            print('유효한 성적을 입력해주세요')
        else:
            total = float((math+science)/2)
            if total>=90:
                print("수학,과학성적의 평균은{}이며 학점은 A입니다".format(total))
            elif total>=80:
                print("수학,과학성적의 평균은{}이며 학점은 B입니다".format(total))
            elif total>=70:
                print("수학,과학성적의 평균은{}이며 학점은 C입니다".format(total))
            else:    
                print("수학,과학성적의 평균은{}이며 학점은 D입니다".format(total))
    except ValueError:
        print('유효한 숫자를 입력해주세요')
    except TypeError:
        print('입력이 바르지 않습니다')

def Q2(): #두수와 연산자 입력받은후 사칙연산 결과 출력, 연산자 값이 이상할시 오류출력
    num1,num2,oper = input("두 수와 연산자를 입력하세요").split()
    try:
        num1 = float(num1)
        num2 = float(num2)
        if oper=="+":
            print("{}{}{}={}입니다".format(num1,oper,num2,num1+num2))
        elif oper=="-":
            print("{}{}{}={}입니다".format(num1,oper,num2,num1-num2))
        elif oper=="*" or oper=="x" or oper=="X":
            print("{}{}{}={}입니다".format(num1,oper,num2,num1*num2))
        elif oper=="%":
            print("{}{}{}의 몫은{}, 나머지는{}입니다".format(num1, oper, num2, num1//num2, num1%num2))
        else:
            print("연산자가 이상해요")
    except ValueError:
        print('유효한 숫자를 입력해주세요')
    except TypeError:
        print('입력이 바르지 않습니다')

def Q3(): #월을 입력받은후 해당하는 계절출력
    try:
        month=int(input("월을 입력해주세요 :"))
        if month>=1 and month<=3:
            print("{}월의 계절은 봄입니다".format(month))
        elif month>=4 and month<=6:
            print("{}월의 계절은 여름입니다".format(month))
        elif month>=7 and month<=9:
            print("{}월의 계절은 가을입니다".format(month))
        elif month>=10 and month<=12:
            print("{}월의 계절은 겨울입니다".format(month))
        else:
            print('입력이 바르지 않습니다')
    except ValueError:
       print('입력이 바르지 않습니다')
    except TypeError:
        print('입력이 바르지 않습니다')

def Q4(): #수를 입력받고 절댓값출력
    try:
        num=int(input('수를 입력해주세요'))
        #print("{}의 절댓값은 {}입니다 ".format(num,abs(num))) <- ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
        if num>=0:
            print("{}의 절댓값은{}입니다".format(num,num))
        elif num<0:
            print("{}의 절댓값은{}입니다".format(num,num*-1))
    except ValueError:
       print('입력이 바르지 않습니다')
    except TypeError:
        print('입력이 바르지 않습니다')

def Q5(): #구입할 사과와 배의 개수,현재 소지금액을 입력받고 구매가 가능하면 잔돈출력, 구매불가시 필요한 금액 입력
    try:
        Apple=3000
        Pear=2000
        AppleCount=int(input('사과:{:,}원입니다. 구매할개수를 입력해주세요 :'.format(Apple)))
        PearCount=int(input('배:{:,}원입니다. 구매할개수를 입력해주세요 :'.format(Pear)))
        Cash=int(input('현재 소지하신 금액(원)을 입력해주세요:'))
        Total=Apple*AppleCount + Pear*PearCount
        Change=Total-Cash
        Change=abs(Change)
        if Total>Cash:
            print('구매불가, {:,}원이 더 필요합니다'.format(Change))
        else:
            print("구매가능, 거스름돈은{:,}원 입니다.".format(Change))
    except ValueError:
       print('입력이 바르지 않습니다')
    except TypeError:
        print('입력이 바르지 않습니다')

def Q6():# 수입력후 3,5,15배수 판정해주기
    try:
        num=int(input('수를 입력해주세요'))
        if num%15==0:
            ("{}은 15의 배수입니다".format(num))
        elif num%5==0:
            ("{}은 5의 배수입니다".format(num))
        elif num%3==0:
            ("{}은 3의 배수입니다".format(num))
        else:
            ("{}은 15,5,3의 배수가 아닙니다".format(num))
    except ValueError:
        print('입력이 바르지 않습니다')
    except TypeError:
        print('입력이 바르지 않습니다')

def Q7(): #이름,키,체중에따른 비만도와 비만정도 출력
    try:
        Name=input("이름을 입력해주세요 :")
        Length=float(input("키를 입력해주세요 :"))
        Weigth=float(input("몸무게를 입력해주세요 :"))
        AvgWeight=(Length-100)*0.9
        Fat=Weigth/AvgWeight*100
        if Fat<100:
            print("{}님의 체중은{}으로 저체중입니다. 표준체중={}".format(Name,Weigth,AvgWeight))
        elif Fat<110:
            print("{}님의 체중은{}으로 정상체중입니다. 표준체중={}".format(Name,Weigth,AvgWeight))
        elif Fat<120:
            print("{}님의 체중은{}으로 과체중입니다. 표준체중={}".format(Name,Weigth,AvgWeight))
        elif Fat<130:
            print("{}님의 체중은{}으로 비만입니다. 표준체중={}".format(Name,Weigth,AvgWeight))
        else:
            print("{}님의 체중은{}으로 고도비만입니다 살좀빼세요. 표준체중={}".format(Name,Weigth,AvgWeight))
    except ValueError:
       print('입력이 바르지 않습니다')
    except TypeError:
        print('입력이 바르지 않습니다')

def Q8 (): #A-B-C-D가 교대로 청소시에, 첫날 A가 당번이라면 N번째날의 당번은?
    try:
        print("A-B-C-D가 교대로 청소를 하며, 첫날 당번은 A입니다. N일에는 누가 당번일까요")
        NDay=int(input("N의 값을 입력하세요"))
        #4로 나누었을때 나머지에 따라 갈림
        Key=NDay%4
        if Key==0:
            print('{}일의 당번은 D입니다')
        elif Key==1:
            print('{}일의 당번은 A입니다')
        elif Key==2:
            print('{}일의 당번은 B입니다')
        elif Key==3:
            print('{}일의 당번은 C입니다')
    except ValueError:
        print('입력이 바르지 않습니다')
    except TypeError:
        print('입력이 바르지 않습니다')

def Q9 (): #오늘은 화요일일때 N일 후의 요일
    try:
        print("오늘이 화요일일때 N일뒤에는 무슨요일일까요") #리스트쓰면 편할거같은데..
        NDay=int(input("N의 값을 입력하세요 :"))
        Key=NDay%7
        Day=["화","수","목","금","토","일","월"]
        print("{}일뒤의 요일은 {}요일입니다".format(NDay,Day[Key]))
        #나머지가 0이면 화, 1이면수.....
        #IF 7개쓰기가 너무 귀찮았어요...
    except ValueError:
        print('입력이 바르지 않습니다')
    except TypeError:
        print('입력이 바르지 않습니다')

def Q10 () : #두수를 거꾸로 뒤집었을때 더큰수 출력
    def q10_1(num): #10번 풀이용 함수
        num=int(num)
        P1=num//100
        P2=num%100//10        
        P3=num%10
        rev=P1+P2*10+P3*100
        return rev
    try:
        num1=int(input("첫번째 수를 입력하세요"))
        num2=int(input("두번째 수를 입력하세요"))
        #숫자 뒤집기 알고리즘 : %10으로 뒷자리, %100//10으로 가운데자리, //100으로 첫자리 뽑아낸후에 *10,*100으로 다시조립
        RevNum1=q10_1(num1)
        RevNum2=q10_1(num2)
        if RevNum1 > RevNum2:
            print("{},{}을 거꾸로뒤집으면 {}, {} 이고 둘중더 큰값은 {}입니다".format(num1,num2,RevNum1,RevNum2,RevNum1))
        elif RevNum1 < RevNum2:
            print("{},{}을 거꾸로뒤집으면 {}, {} 이고 둘중더 큰값은 {}입니다".format(num1,num2,RevNum1,RevNum2,RevNum2))
        elif RevNum1 == RevNum2:
            print("{},{}을 거꾸로뒤집으면 {}, {} 이고 두값은 같습니다".format(num1,num2,RevNum1,RevNum2))
    except ValueError:
        print('입력이 바르지 않습니다')
    except TypeError:
        print('입력이 바르지 않습니다')

def Q11(): #태어난 년도를 입력받아 띠를 출력
    try: # 0년의 띠를 알수없기때문에 2024년의 띠(용)를 기준으로 -값에따라 계산
         #뱀,말,양,원숭이,닭,개,돼지,쥐,소,호랑이,토끼,용
        num=int(input("태어난 년도를 입력하세요"))
        key=(2024-num)%12
        #위에 7개 그냥 if-else로 했으면 여기서 리스트쓰는건데....
        if key<0:
            print("유효한 년도를 입력해주세요")
        elif key==0:
            print("{}년 출생의 띠는 용띠입니다".format(num))
        elif key==1:
            print("{}년 출생의 띠는 토끼띠입니다".format(num))
        elif key==2:
            print("{}년 출생의 띠는 호랑이띠입니다".format(num))
        elif key==3:
            print("{}년 출생의 띠는 소띠입니다".format(num))
        elif key==4:
            print("{}년 출생의 띠는 쥐띠입니다".format(num))
        elif key==5:
            print("{}년 출생의 띠는 돼지띠입니다".format(num))
        elif key==6:
            print("{}년 출생의 띠는 개띠입니다".format(num))
        elif key==7:
            print("{}년 출생의 띠는 닭띠입니다".format(num))
        elif key==8:
            print("{}년 출생의 띠는 원숭이띠입니다".format(num))
        elif key==9:
            print("{}년 출생의 띠는 양띠입니다".format(num))
        elif key==10:
            print("{}년 출생의 띠는 말띠입니다".format(num))
        elif key==11:
            print("{}년 출생의 띠는 뱀띠입니다".format(num))
    except ValueError:
       print('입력이 바르지 않습니다')
    except TypeError:
        print('입력이 바르지 않습니다')

def Q12(): #윤년구하기
    try:#4의배수는 윤년, 4의배수이면서 100의배수면 평년 400의배수면 윤년
        year = int(input("연도를 입력하세요 :"))
        #각조건을 ABC라고 할때 (A and !B) or C 일때 윤년이된다
        if ((year%4==0 and year%100!=0) or year%400==0):#논리회로가 생각난다...
            print("{}년은 윤년입니다.".format(year))
        else:
            print("{}년은 윤년이 아닙니다.".format(year))
    except ValueError:
       print('입력이 바르지 않습니다')
    except TypeError:
        print('입력이 바르지 않습니다')

def Q13(): #시간과 분입력후 30분후 시간 출력 ----조건문 사용X
    try:
        Hour=int(input("시간을 입력하세요 :"))
        Min=int(input("분을 입력하세요 :"))
        MinTime=Hour*60+Min+30 # 30값에 다른수를 넣으면 다른시간도 출력가능함
        After30Hour=(MinTime//60)%24
        #조건문없이 24를 초과하는 시간값을 처리하는방법 -> 24시==00시로 계산 결과시간을 24로 나눈 나머지로계산시 25시->1시로 변경됨 
        After30Min=MinTime%60
        print("30분후의 시간은 {}:{}입니다".format(After30Hour,After30Min))
    except ValueError:
       print('입력이 바르지 않습니다')
    except TypeError:
        print('입력이 바르지 않습니다')

def Q14(): #시간과 분 입력후 30분전 시간 출력
    try:
        Hour=int(input("시간을 입력하세요 :"))
        Min=int(input("분을 입력하세요 :"))
        if Min<=29:
            Hour=Hour-1
            if Hour < 0:
                Hour=Hour+24
            print("30분 전의 시간은{}:{}입니다".format(Hour,Min+30))
        if Min >= 30:
            print("30분 전의 시간은{}:{}입니다".format(Hour,Min-30))
    except ValueError:
       print('입력이 바르지 않습니다')
    except TypeError:
        print('입력이 바르지 않습니다')

def Q15(): #카페 음료선택..?
    try:
        print("="*32)
        print("1.아메리카노 \n2.카페라떼")
        print("="*32)
        MenuNum=int(input("메뉴선택: "))
        if MenuNum==1:
            Menu="아메리카노"
        elif MenuNum==2:
            Menu="카페라떼"
        else: 
            print("유효한 값을 입력해주세요")
        print("="*32)
        print("1.ICE \n2.HOT")
        TempNum=int(input("메뉴선택: "))
        if TempNum==1:
            Temp="아이스"
        elif TempNum==2:
            Temp="따뜻한"
        else: 
            print("유효한 값을 입력해주세요")
        print("선택하신 메뉴는 {} {}입니다".format(Temp,Menu))

    except ValueError:
       print('입력이 바르지 않습니다')
    except TypeError:
        print('입력이 바르지 않습니다')