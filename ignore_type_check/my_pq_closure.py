from my_utils import make_floor


def create_pq():
	q = []


	def size():
		global q
		
		return len(q)

	def top():
		global q
		
		if size() <= 0:
			return None

		return q[0]

	def popp():
		global q
		
		s = size()
		if s == 0:
			return None

		v = q[0]
		if s <= 1:
			q = []
			return v
		
		last_v = q.pop()
		ti = 0
		q[ti] = last_v
		while True:
			li = ti * 2 + 1
			ri = ti * 2 + 2

			# 인덱스 초과
			if li >= size():
				break

			if ri >= size():
				if q[li] > q[ti]:
					swap(li, ti)
					ti = li
				
				break

			target_i = None
			if q[ri] > q[li]:
				target_i = ri
			else:
				target_i = li
			
			if q[target_i] > q[ti]:
				swap(target_i, ti)
				ti = target_i
			else:
				break
			
		return v

	# 마지막에 넣고 올린다.
	def push(v):
		global q
		
		s = size()
		q.append(v)

		if s == 0:
			return
		
		ti = s
		while True:
			pi = make_floor((ti - 1) / 2)

			if pi < 0:
				return
			
			# 교환이 필요하다면
			if q[pi] < q[ti]:
				swap(pi, ti)
				ti = pi

			else:
				return

	def swap(i, j):
		global q
		
		q[i], q[j] = q[j], q[i]

	def reset():
		global q
		
		q = []
		
	def show():
		global q
		
		print(q)

	return {
		'push': push,
		'pop': popp,
		'size': size,
		'reset': reset,
		'show': show
	}
	