from my_move import move_to_pos

D = [North, West, South, East]

def make_maze(size, pos):
	y, x = pos
	
	substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)
	
def find_wall():
	# 3 * 3
	while True:
		for d in D:
			if not can_move(d):
				return d
			
		move(D[0])
		
DX = [1, 0, -1, 0]
DY = [0, 1, 0, -1]
def escape(pos):
	r = 1
	
	while True:
		if get_entity_type() == Entities.Treasure:
			harvest()
			return
		
		for i in range(len(D)):
			new_direction_index = (r - 1 + i + len(D)) % len(D)
			
			new_direction = D[new_direction_index]
			
			if can_move(new_direction):
				move(new_direction)
				r = new_direction_index
				
				break
			
def spawn_drones():
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

    for y in range(maze_count):
        for x in range(maze_count):
            pos_list.append((y * width_size, x * width_size))

    for i in range(len(pos_list)):
		def wrapper():
			move_to_pos(pos_list[i])
			time = 6
			for i in range(time):
				l = str(time - i) + '초 뒤 출력'
				print(l)
			escape(y, x)
				
        spawn_drones(wrapper)
				
def loop_maze(size, ):
	while True:
		make_maze(size, (0, 0))
		escape(pos)
