

#예제 기본 ver
print("{:>32}".format("파이썬 쇼핑몰"))
print("{}".format("번호 : 1078718855"))
print("{}".format("주소 : 서울시 종로구 종로3가"))
print("{}".format("성명 : 김사장"))
print("{}".format("전화 : 070-1234-5678"))
print("{:-<64}".format("")) # print("-"*64)로도 가능했음
print("{:>8}{:>16}{:>12}{:>16}".format("품명","단가","수량","금액"))
#비트계산대신 \t로 간격 설정했어도 가능, 총길이를 지정하지 않았다면 탭이더 간편함
#탭사용하면 앞쪽 비트가 바뀌어도 거의 뒷간격이 동일함 탭1번당 칸수를 계산해서 사용가능
print("{:-<64}".format(""))
print("{:16}{:<16,}{:<16}{:>8,}".format(" 블루투스이어폰",85000,"1",85000))
print("{:>12}{:>17,}{:>11}{:>23,}".format("USB3.0 8G",8000,"1",8000))
#print("{:>14}\t\t{:6,}\t{:>4}\t{:>6,}".format("USB3.0 8G",8000,"1",8000))
print("{:-<64}".format(""))
print("{:32}{:29,}".format("소 계",93000))
print("{:-<64}".format(""))
print("{:32}{:27,}".format("청구금액",93000))
print("{:32}{:27,}".format("받은금액",100000))
print("{:32}{:27,}".format("거스름돈",7000))
print("{:-<64}".format(""))

"""
#변수ver
print("{:>32}".format("파이썬 쇼핑몰"))
print("{}".format("번호 : 1078718855"))
print("{}".format("주소 : 서울시 종로구 종로3가"))
print("{}".format("성명 : 김사장"))
print("{}".format("전화 : 070-1234-5678"))
print("{:-<64}".format(""))
print("{:>8}{:>16}{:>12}{:>16}".format("품명","단가","수량","금액"))
print("{:-<64}".format(""))
bt=int(85000)
usb=int(8000)
print("{:16}{:<16,}{:<16}{:>8,}".format("블루투스이어폰",bt,"1",bt))
print("{:>12}{:>17,}{:>11}{:>23,}".format("USB3.0 8G",usb,"1",usb))
print("{:-<64}".format(""))
print("{:32}{:29,}".format("소 계",bt+usb))
print("{:-<64}".format(""))
print("{:32}{:27,}".format("청구금액",bt+usb))
total=int(100000)
print("{:32}{:27,}".format("받은금액",total))
print("{:32}{:27,}".format("거스름돈",total-bt+usb))
print("{:-<64}".format(""))
"""