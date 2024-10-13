print('직각삼각형 그리기\n')
leg = int(input('변의 길이: '))
 #이거 혹시 int leg = input("~") 로 해도 되는건가..
for i in range(leg):
    print('* ' * (i + 1))

area = (leg ** 2) / 2
print('넓이:', area)