print("Python1")
# 출력 : 개행자동
# 파이썬 주석처리 방식
# 문자열 출력시에는 "" or ''로 문자열 감싸기
print(1)
#숫자출력시에는 그냥 적기
""" i=3
print(f"{i}") """
#파이썬의 f스트링, 따옴표안에 f를 붙이면 중괄호안에 변수를 넣을 수 있다.
"""
여러 데이터 출력시에는 , 사용으로 데이터값 구분
,사용시에는 공백이 자동으로 추가된다
escape sequance 사용시에도 자동공백 생각하기
SyntaxError -> 문법오류코드
띄어쓰기 사용해도 에러남 <- 파이썬은 들여쓰기, 공백개수로 함수를 구분함
"""
print("10 더하기 20은",10+20)
print(1,"\n",1, sep="")
#sep = ,사이에 들어가는 간격 설정 -> 기본은 " "
#end = 끝날때 출력할 문자 -> 기본은 \n(escape sequnce)
str1="=============================================="
print(str1)
print(str1)
print("============ name : Hn =======================")
print("============ call : 010-xxxx-xxxx ============")
print("============ mail : lxnx.kiki@- ==============")
print(str1)
print(str1)
print("=                                            =")
print("=                                            =")
print(str1)
#변수이름 지을때는 다른문자열에 포함되기 힘든이름으로 짓기, 한번에 바꾸다 건드리면 개고생함(한번에 바꿀땐 F2)
#이스케이프시뭔스 \t : 탭 \n : 개행 \뒤에 \?'"붙이면 해당문자 출력