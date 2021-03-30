

def change_size(self, new_capacity):
    		print(f'  * changing capacity: {self.capacity} --> {new_capacity}') # 이 첫 문장은 수정하지 말 것
		B=[0 for i in range(new_capacity)]# 1. new_capacity의 크기의 리스트 B를 만듬
		for i in range(self.capacity):
			B[i] = A[i]# 2. self.A의 값을 B로 옮김
		del self.A  #3.(A 지움)
		self.A = B
		self.capacity = new_capacity
