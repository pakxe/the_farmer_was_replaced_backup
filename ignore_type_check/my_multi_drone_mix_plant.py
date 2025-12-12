# 1 현재 땅을 가지고 혼합 심을 수 있는 위치 구하기
# 위치마다 다른 식물을 심고 싶다면 dict 배열을 사용한다. 
# 한놈이 이동하면서 1로 구한 위치에 드론 spawn하기 
# 소환된 드론들은 mix_plant함수를 사용한다. 
from my_move import move_to_pos
from my_utils import make_arr

PLANTS = [{
	'entity': Entities.Grass,
	'ground': Grounds.Grassland
}, {
	'entity': Entities.Tree,
	'ground': Grounds.Soil,
}, {
	'entity':Entities.Carrot,
	'ground': Grounds.Soil
}]
WORLD_WIDTH = get_world_size()

# 1. 현재 땅을 가지고 혼합 심을 수 있는 위치 구하기
# 사이사이 끼우면 될 것 같다.
WIDTH = 3
def get_mix_plant_locations():
	locations = []

	# rect
	RECT_Y_UNIT = WIDTH * 2 + 1
	RECT_Y_START = WIDTH

	RECT_X_UNIT = WIDTH * 2 + 2
	RECT_X_START = WIDTH

	for y in range(RECT_Y_START, WORLD_WIDTH - WIDTH, RECT_Y_UNIT):
		for x in range(RECT_X_START, WORLD_WIDTH - WIDTH, RECT_X_UNIT):
			locations.append((y, x))

	# interval
	INTERVAL_Y_UNIT = WIDTH * 2 + 1
	INTERVAL_Y_START = WIDTH * 2

	INTERVAL_X_UNIT = WIDTH * 2 + 2
	INTERVAL_X_START = WIDTH * 2 + 1

	for y in range(INTERVAL_Y_START, WORLD_WIDTH - WIDTH, INTERVAL_Y_UNIT):
		for x in range(INTERVAL_X_START, WORLD_WIDTH - WIDTH, INTERVAL_X_UNIT):
			locations.append((y, x))

	return locations

def plant_entity(plant_info):
	if get_ground_type() != plant_info['ground']:
		till()

	plant(plant_info['entity'])

def mix_plant(y, x, plant_info):
	while True:
		move_to_pos(y, x)

		if can_harvest():
			use_item(Items.Weird_Substance)
			harvest()
		else:
			if get_water() < 0.5 and num_items(Items.Water) > 1:
				use_item(Items.Water)
			
			if num_items(Items.Fertilizer) > 2:
				use_item(Items.Fertilizer)
				use_item(Items.Fertilizer)
			
			
			continue

		# main 심기
		plant_entity(plant_info)
		if get_water() < 0.5 and num_items(Items.Water) > 1:
			use_item(Items.Water)
			
		if num_items(Items.Fertilizer) > 1:
			use_item(Items.Fertilizer)
	
		sub_entity, (tx, ty) = get_companion()

		for i in range(len(PLANTS)):
			if PLANTS[i]['entity'] == sub_entity:
				move_to_pos(ty, tx)
				plant_entity(PLANTS[i])

def harvest_row(sy):
	move_to_pos(sy, 0)
	while True:
		if can_harvest():
			harvest()
			
		move(East)
		
def patrol(location_set):
	while True:
		for y in range(WORLD_WIDTH):
			for x in range(WORLD_WIDTH):
				move_to_pos(y, x)

				key = str(y) + str(x)
				if key in location_set:
					continue

				if can_harvest():
					harvest()

				else:
					if get_entity_type() == Entities.Tree:
						if num_items(Items.Water) > 0:
							use_item(Items.Water)

def command_drones_to_work():
	clear()

	locations = get_mix_plant_locations()

	visited = make_arr(False, WORLD_WIDTH)

	for i in range(len(locations)):
		y, x = locations[i]
		visited[y] = True

		plant_info_index = i % len(PLANTS)
		def wrapper():
			mix_plant(y, x, PLANTS[plant_info_index])

		spawn_drone(wrapper)
		
	cur_drone_count = num_drones()
	left_drone_count = max_drones() - cur_drone_count


	location_set = set()
	for i in range(len(locations)):
		y, x = locations[i]

		key = str(y) + str(x)
		location_set.add(key)
	
	
	if left_drone_count > 0:
		def wrapper():
			patrol(location_set)

		for i in range(left_drone_count):
			spawn_drone(wrapper)
			for i in range(10):
				s = ''
				s += str(10 - i)
				s += '초 뒤 패트롤'
				print(s)
		
	# for i in range(len(visited)):
	#     if visited[i]:
	#         continue
	#     else:
	#         def wrapper():
	#             harvest_row(i)
			
	#         spawn_drone(wrapper)
command_drones_to_work()