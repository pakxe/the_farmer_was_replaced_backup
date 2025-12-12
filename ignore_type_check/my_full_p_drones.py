# 한 줄마다 드론을 소환해서 호박을 관리한다. 
#
# 
from my_sq_closure import create_sq
from my_move import move_to_pos

WORLD_WIDTH = get_world_size()

def plant_pumpkin_row(sy, sx):
    move_to_pos(sy, sx)
    pq = create_sq()

    for x in range(WORLD_WIDTH):
        pq['push']((sy, x))

    while True:
        if pq['size']() <= 0:
            print('종료')
            return True
        
        y, x = pq['pop']()
        move_to_pos(y, x)

        if get_ground_type() != Grounds.Soil:
                till()

        if not can_harvest():
            plant(Entities.Pumpkin)
            pq['push']((y, x))
    

def spawn_pumpkin_drones():
    clear()
    
    drones = []
    for i in range(WORLD_WIDTH):
        def wrapper():
            plant_pumpkin_row(i, 0)        

        drone = spawn_drone(wrapper)
        drones.append(drone)

    for i in range(len(drones)):
        drone = drones[i]
        wait_for(drone)
    # print(drones)
    # while True:
    #     is_finished = True
        
    #         if has_finished(drone):
    #             is_finished = False
    #             break

    #     if is_finished:
    #         break
    #     else:
    #         continue

    harvest()

while True:
    spawn_pumpkin_drones()

        