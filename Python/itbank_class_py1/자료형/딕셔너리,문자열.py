#딕셔너리 - 키를 사용하여 여러가지 자료를 저장함
#리스트는 인덱스기반,딕셔너리는 키 기반
# 변수={키:값}로 선언함
""" dict_1 = {"name":"펭수","age":20}
print(dict_1)           # 전체출력
print(dict_1["name"])   #특정키의 값 출력 """
#딕셔너리+리스트
""" dict_2={"workmate":[1,2,3,4,5]} #키는 하나지만 값은 여려개인경우 """
""" dict_3={
    "name":"펭수",
    "age" : 20,
    "workmate":[1,2,3,4,5],
    "birth":"남극"
}
print(dict_3["workmate"][2]) """
#키-값추가
#딕셔너리명[새로운키]=새로운값
#특정키의값 제거
""" del dict_3["workmate"]
print(dict_3) """
#딕셔너리 함수
#update()   딕셔너리에 키-값을 추가                   딕셔너리명.update({키:값})으로 사용
#get()      딕셔너리값 반환                          딕셔너리명.get(키)로 사용
#keys()     딕셔너리의 모든키를 반환                    딕셔너리명.keys
#values()   딕셔너리의 모든값을 반환                    딕셔너리명.values
#items()    딕셔너리의 모든 키-값을 튜플로 반환           딕셔너리명.items
#(튜플:리스트와 유사하지만 한번 지정한값 변경 불가) 
#clear()    모든 키-값 삭제                          딕셔너리명.clear()
""" d_m={}
while True:
    k,v=input("키와 값을 입력하세요,종료하려면 0:0입력").split()
    if not k=="0" and not v=="0":
        d_m.update({k:v})
    else:
        break
print(d_m) """
""" cnt={"커피":7,"펜":3,"종이컵":9,"콜라":20,"사이다":9}
key=input("재고를 입력하세요(커치,펜,종이컵,콜라,사이다)")
print("{}의 수량은{}개입니다".format(key,cnt[key])) """
""" i=int(input("등록할 책개수를 입력하세요"))
li={}
for j in range(1,i+1):
    li.update({j:input("책제목을 입력하세요:")})
print(li) """
#문자열 함수
#find(str,n)    문자열에서 특정문자열을 찾아 n번째부터 해당문자의 인덱스 반환 n의 위치는 정할수 있지만 시작되는 인덱스값은 0부터임
#count(str)     문자열에서 특정문자열의 수를 반환
#lower()        영문자를 소문자로 변경후 반환
#upper()        영문자를 대문자로 변경후 반환
#strip()        문자열의 앞뒤공백 제거 lstrip,rstrip로 한쪽만 제거할수도 있음
#replace(a,b)   특정문자열 변경(a를 b로)(a를 위치로 설정해서 변경도가능, 슬라이싱도 가능)
#split(str)     문자열을 특정문자열 기준으로 분리 (기본값=" ")
""" st="It is a fun python class"
st=st.lower()
print(len(st))
print(st.count("a"))
print(st.count("s")) """



#연습문제 (꼭 복습해보기)
'''노가다버전'''
# st ="""김개똥 -2017년 03월 24일
# 홍길동구리 -2015년 04월 02일
# 선우선녀 -2018년 05월 14일
# ㅁ-1234년 03월 12일"""
# # -를 :로, 연도를 모두 1999년으로
# a=st.split("\n")
# ret=""""""
# for i in range(len(a)):
#    # print(a[i])
#     k=a[i].split("년")
#     temp=k[1]
#     temp1=k[0].split("-")
#     temp1=temp1[0]
#     temp="1999년"+temp
#     word=temp1+":"+temp
#     ret+=word+"\n"
#print(ret)
""" 함수 활용 버전 , 슬라이싱 개념/문자열 인덱스 개념 활용시에 이렇게 접근할수있었음"""
# st ="""김개똥 -2017년 03월 24일
# 홍길동구리 -2015년 04월 02일
# 선우선녀 -2018년 05월 14일
# ㅁ-1234년 03월 12일"""
# st=st.replace("-",":")
# a=0
# for i in range(st.count(":")):
#     a=st.find(":",a+1) # 다음루프시에 이전에 찾은값 다음부터 찾을수있음
#     st=st.replace(st[a+1:a+5],1999) #replace함수 슬라이싱으로 활용
# print(st)