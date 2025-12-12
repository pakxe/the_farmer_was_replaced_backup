from my_move import move_to_pos

def plant_entity(entity):
	is_planted = plant(entity)
	
	if not is_planted:
		till()
		plant(entity)
	

def mix_plant(y, x, main_entity):
	while True:
		move_to_pos(y, x)
		
		if can_harvest():
			use_item(Items.Weird_Substance)
			harvest()
		else:
			use_item(Items.Fertilizer)
			use_item(Items.Fertilizer)
			
			if num_items(Items.Water) > 0:
				use_item(Items.Water)
			continue
		
		# main 심기
		is_planted = plant(main_entity)
		if not is_planted:
			till()
			plant(main_entity)
		use_item(Items.Fertilizer)
		
	
		# 하인 심기
		plant_type, (tx, ty) = get_companion()
		move_to_pos(ty, tx)
		harvest()
		plant_entity(plant_type)
		move_to_pos(ty+1, tx)
		plant_entity(Entities.Sunflower)
		
		
		
		
clear()
mix_plant(3, 3, Entities.Grass)