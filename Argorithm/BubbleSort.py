#버블정렬 구현테스트
#n번째와 n+1번째의 원소를 비교하면서 순차적으로 정렬을 실행함 
#n + (n-1) + (n-2) ... (n-n-1) for(i=1;i<n;i++)∑i = {(n-1)*n}/2
#최고차항이 N^2이므로
#O(n^2)의 코드복잡도를 가짐
array=[9,8,7,6,5,4,3,2,1,0] #길이는 10

leng=len(array)

def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b
def bubbleSort(array):
    for i in range(0,leng-1):    #뒤의원소와 비교해야하기때문에 총길이 -1
        for j in range(0,leng-1-i): #n바퀴 돌때마다 뒤에서부터 n개까지는 정렬이 완료된다
            if array[j]>array[j+1]:
                array[j],array[j+1]=swap(array[j],array[j+1])
                print(array)        #실험용
        print()                     #실험용2
    print(array)
    #return array