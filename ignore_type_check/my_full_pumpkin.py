from my_ground import change_ground
import my_sq 
from my_move import move_to_pos
from all_plant import plant_name

clear()
change_ground(Grounds.Soil)

move_to_pos(0, 0)

def grow_pumpkin():
	s = get_world_size()
	
	for y in range(s):
		for x in range(s):
			my_sq.push((y, x))
			
	while True:
		if my_sq.size() <= 0:
			harvest()
			break
			
		y, x = my_sq.pop()
		move_to_pos(y, x)
		
		if not can_harvest():
			# if num_items(Items.Water) > 2:
			# 	use_item(Items.Water)
			# 	use_item(Items.Water)
		
			if num_items(Items.Carrot) == 0:
				return False
				
			plant(Entities.Pumpkin)
			my_sq.push((y, x))
						
	return True

while True:
	is_finished = grow_pumpkin()
	
	if is_finished:
		continue
	else:
		is_finished = plant_name('carrot')
		if is_finished:
			continue
		else:
			is_finished = plant_name('tree')
			if is_finished:
				plant_name('grass')
			
		