# plant_cactus

# 오른쪽 상단과 같거나 크고, 왼쪽 하단과 작거나 같다면 선인장은 정렬되었다고 판단.
# 모든 선인장이 다 자랐고, 정렬되어있으며, 사각형인 경우 한번에 수확. 
# 정렬 안됐으면 선인장은 갈색, 정렬됐으면 녹색
# 수확 ** 2로 받는다. 
# 크기는 measure()로 확인한다. 0~9까지. measure(direction)도 가능. 
# swap(direction)으로 드론 아래 <-> direction 개체를 교환 할 수 있음.
from my_move import move_to_pos
from my_drone import my_spawn_drone

WORLD_SIZE = get_world_size()
def plant_and_sort_cts_row(y):
    # 1. 행에 선인장 심기
    for x in range(WORLD_SIZE):
        move_to_pos(y, x)

        if get_ground_type() != Grounds.Soil:
            till()

        plant(Entities.Cactus)

    # 2. 행을 정렬하기 
    for i in range(WORLD_SIZE):
        for j in range(0, WORLD_SIZE - i - 1):
            left_x = j
            right_x = j + 1

            move_to_pos(y, left_x)
            left_v = measure()

            move_to_pos(y, right_x)
            right_v = measure()

            if left_v > right_v:
                swap(West)
    
    return 

def sort_col_cts(x):
    # 1. 열을 정렬하기
    for i in range(WORLD_SIZE):
        for j in range(0, WORLD_SIZE - i - 1):
            bottom_y = j
            top_y = j + 1

            move_to_pos(bottom_y, x)
            bottom_v = measure()

            move_to_pos(top_y, x)
            top_v = measure()

            if bottom_y > top_v:
                swap(South)

    return

def spawn_drones_row():
    drone_handlers = []
    for y in range(WORLD_SIZE):
        move_to_pos(y, 0)    
        drone = my_spawn_drone(plant_and_sort_cts_row, y)
        drone_handlers.append(drone)

    return drone_handlers

def spawn_drones_col():
    drone_handlers = []
    for x in range(WORLD_SIZE):
        move_to_pos(x, 0)    
        drone = my_spawn_drone(sort_col_cts, x)
        drone_handlers.append(drone)
    
    return drone_handlers


def main():
    # 행
    drone_handlers = spawn_drones_row()
    print(drone_handlers)
    for i in range(len(drone_handlers)):
        drone_handler = drone_handlers[i]
        wait_for(drone_handler)

    # 열
    drone_handlers = spawn_drones_col()
    for i in range(len(drone_handlers)):
        drone_handler = drone_handlers[i]
        wait_for(drone_handler)

    # 끝
    harvest()

while True:
    main()
