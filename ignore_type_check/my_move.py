from my_utils import make_abs

# 인자 이름 명확화 (get_current_pos -> current_pos)
def custom_move(current_pos, target_pos, toward, backward):
	# 변수명을 직관적으로 변경 (y -> current_pos)
	row = get_world_size()
	
	if target_pos == current_pos:
		return
	
	diff = make_abs(target_pos - current_pos)
	
	# 1. 목표 지점의 좌표가 더 클 때 (예: 현재 1 -> 목표 3)
	#    기본적으로 toward(정방향, +)로 가야 함
	if target_pos > current_pos:
		# 반대편으로 돌아가는 게 더 빠를 때 (World Wrap)
		if diff > (row / 2):
			move_count = row - diff
			for _ in range(move_count):
				move(backward) # 뒤로 돌아가기
		# 바로 가는 게 빠를 때
		else:
			for _ in range(diff):
				move(toward)   # 앞으로 가기

	# 2. 목표 지점의 좌표가 더 작을 때 (예: 현재 3 -> 목표 1)
	#    기본적으로 backward(역방향, -)로 가야 함
	else:
		# 반대편으로 돌아가는 게 더 빠를 때 (World Wrap)
		if diff > (row / 2):
			move_count = row - diff
			for _ in range(move_count):
				move(toward)   # [수정] 하드코딩된 North 제거 -> toward(앞으로 돌아가기)
		# 바로 가는 게 빠를 때
		else:
			for _ in range(diff):
				move(backward) # 뒤로 가기

def move_to_pos(y, x):
	# y축 이동
	# [수정] 보통 좌표계는 북쪽이 +(증가) 방향이므로 North가 toward(정방향)가 되어야 합니다.
	# 만약 (0,0)이 좌상단인 좌표계라면 원본 순서(South, North)를 유지하세요.
	custom_move(get_pos_y(), y, North, South) 
	
	# x축 이동
	# 동쪽이 +(증가) 방향이므로 East가 toward, West가 backward
	custom_move(get_pos_x(), x, East, West)