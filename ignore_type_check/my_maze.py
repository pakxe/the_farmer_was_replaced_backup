from my_move import move_to_pos

D = [North, West, South, East]

def make_full_maze(size):
	move_to_pos(0, 0)
	plant(Entities.Bush)
	
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
def escape():
	r = 1
	
	while True:
		if get_entity_type() == Entities.Treasure:
			harvest()
			return
		
		for i in range(len(D)):
			# 0 -> 3, 0 - 1 + 1 + 4 4 % 4 = 0
			new_direction_index = (r - 1 + i + len(D)) % len(D)
			
			new_direction = D[new_direction_index]
			
			if can_move(new_direction):
				move(new_direction)
				r = new_direction_index
				
				break
				
def loop_maze(size):
	while True:
		make_full_maze(size)
		escape()
