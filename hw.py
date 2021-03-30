class myList():
    def __init__(self):
	    self.capacity = 2	  # myList의 용량 (저장할 수 있는 원소 개수)
	    self.n = 0          # 실제 저장된 값의 개수
	    self.A = [None] * self.capacity # 실제 저장 자료구조 (python의 리스트 사용) 

    def __len__(self):
	    return self.n
	
    def __str__(self):
	    return f'  ({self.n}/{self.capacity}): ' + '[' + ', '.join([str(self.A[i]) for i in range(self.n)]) + ']'

    def __getitem__(self, k): # k번째 칸에 저장된 값 리턴
		#try:
	    return self.A[k]
		#except:
	# k가 음수일 수도 있음
		# k가 올바른 인덱스 범위를 벗어나면 IndexError 발생시킴

    def __setitem__(self, k, x): # k번째 칸에 값 x 저장
	    self.A[k] = x
		# k가 음수일 수도 있음
		# k가 올바른 인덱스 범위를 벗어나면 IndexError 발생시킴

    def change_size(self, new_capacity):
        
	    print(f'  * changing capacity: {self.capacity} --> {new_capacity}') # 이 첫 문장은 수정하지 말 것
	    # 1. new_capacity의 크기의 리스트 B를 만듬
	    B = [0 for i in range(new_capacity)]
	    for i in range(self.capacity):
		    B[i] = self.A[i]
	    del self.A  #3.(A 지움)
	    self.A = B
	    self.capacity = new_capacity

	
    def append(self, x):
	    if self.n == self.capacity: # 더 이상 빈 칸이 없으니 capacity 2배로 doubling
	        self.change_size(self.capacity*2)
	    self.A[self.n] = x     # 맨 뒤에 삽입
	    self.n += 1            # n 값 1 증가
L = myList()
while True:
    cmd = input().strip().split()
    if cmd[0] == 'append':
        L.append(int(cmd[1]))
        print(f"  + {cmd[1]} is appended.")
    elif cmd[0] == 'print':
        print(L)
    else:
        print(" ? invalid command! Try again.")
