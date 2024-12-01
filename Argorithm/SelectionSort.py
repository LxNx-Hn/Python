#선택정렬 알고리즘
#끝까지 반복한후 최소값을 인덱스 0에 넣음
#여기서는 최대값을 마지막인덱스에 넣고 -1번 순회하는 형식으로 구현할 예정
array=[9,8,7,6,5,4,3,2,1,0] #길이는 10

def selection_sort(array):
	n = len(array)
	for i in range(n):
		min_index = i
		for j in range(i + 1, n):
			if array[j] < array[min_index]:
				min_index = j
		array[i], array[min_index] =  array[min_index], array[i]
		print(array[:i+1])

print("before: ",array)
selection_sort(array)
print("after:", array)