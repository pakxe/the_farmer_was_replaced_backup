# 0,0에 맵 사이즈 -1의 미로를 만들고
# 그 외 공간에 선플라워를 심고 계속 수확한다.

from my_maze import loop_maze
from my_move import move_to_pos
import my_priority_queue

# flower 심을 edge_width를 정한다.
EDGE_WIDTH = 1

def plant_sunflower(start_pos, pq):
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

	# 오른쪽 엣지 채우기
	# start_y = y - EDGE_WIDTH
	# start_x = row - EDGE_WIDTH
	# for y in range(start_y, -1, -1):
	# 	for x in range(start_x, row):
	# 		move_to_pos(y, x)
	# 		if get_ground_type() != Grounds.Soil:
    #             till()
		
	# 		plant(Entities.Sunflower)
	# 		pq.push((measure(), y, x))
	
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
		plant_sunflower(start_pos, pq)
		harvest_sunflower(pq)
		pq.reset()

clear()
spawn_drone(loop_sunflower)

while True:
	move_to_pos(0, 0)

	maze_width = get_world_size() - EDGE_WIDTH

	loop_maze(maze_width)