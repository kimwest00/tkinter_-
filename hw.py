
A = [1,2,3,4,5,6]
capacity = 6
def change_size(A , capacity, new_capacity):
    print(f'  * changing capacity: {capacity} --> {new_capacity}') # 이 첫 문장은 수정하지 말 것
	B = [0 for i in range(new_capacity)]
	for i in range(capacity):
		B[i] = A[i]
	del A  #3.(A 지움)
	A = B
	capacity = new_capacity
