# 그 외 공간에 선플라워를 심고 계속 수확한다.

# from my_maze import loop_maze
from maze import loop_maze
from my_move import move_to_pos
from my_utils import make_floor
import my_priority_queue

# flower 심을 edge_width를 정한다.
EDGE_WIDTH = 1

def plant_sunflower_to_top(start_pos, pq):
	y, x = start_pos
	move_to_pos(y, x)
	
	row = get_world_size()

	# # 위쪽 엣지 채우기
	for y in range(y, y - EDGE_WIDTH, -1):
		for x in range(row):
			move_to_pos(y, x)
			if get_ground_type() != Grounds.Soil:
                till()
		
			plant(Entities.Sunflower)
			pq.push((measure(), y, x))

def plant_sunflower_to_right(start_pos, pq):
	y, x = start_pos
	move_to_pos(y, x)

	row = get_world_size()

	for x in range(x, x - EDGE_WIDTH, -1):
		for y in range(0, row - 1):
			move_to_pos(y, x)
			if get_ground_type() != Grounds.Soil:
                till()
		
			plant(Entities.Sunflower)
			pq.push((measure(), y, x))
	
def harvest_sunflower(pq):
	while True:
		if pq.size() == 0:
			return

		leaf_count, y, x = pq.popp()
		move_to_pos(y, x)
		
		while True:
			if can_harvest():
				harvest()
				break
			
			if num_items(Items.Water) > 0:
				use_item(Items.Water)
	

def loop_sunflower():
	# top, right edge
	row = get_world_size()
	start_pos = (row - 1, 0)
	pq = my_priority_queue
	while True:
		plant_sunflower_to_top(start_pos, pq)
		harvest_sunflower(pq)
		pq.reset()

def loop_sunflower_to_right():
	l = get_world_size()
	start_pos = (l - 1, l - 1)
	pq = my_priority_queue
	while True:
		plant_sunflower_to_right(start_pos, pq)
		harvest_sunflower(pq)
		pq.reset()

clear()
spawn_drone(loop_sunflower)
spawn_drone(loop_sunflower_to_right)

drone_count = max_drones() - 2
rest_world_size = get_world_size() - EDGE_WIDTH

# 한 변에 몇 개의 maze 가능?
maze_count = 1
# 최대 미로 개수 찾기
for i in range(1, get_world_size() - 1):
	if i ** 2 > drone_count:
		maze_count = i - 1
		break

# maze_count로 좌표 찾기
pos_list = []
width_size = make_floor(rest_world_size / maze_count)

half = make_floor(width_size / 2)
for y in range(maze_count):
	for x in range(maze_count):
		pos_list.append((y * width_size + half , x * width_size + half))

def maze_drone(pos):
	y, x = pos
	move_to_pos(y, x)
	time = 6
	for i in range(time):
		l = str(time - i) + '초 뒤 시작'
		print(l)
	
	loop_maze(width_size, pos)

while True:
	for i in range(len(pos_list)):
		def wrapper():
			maze_drone(pos_list[i])
		
		spawn_drone(wrapper)