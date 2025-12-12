class Entities_:
    def __init__(self):
        self.Carrot = 'carrot'
        self.Grass = 'grass'
        self.Bush = 'bush'

Entities = Entities_()

def plant(entities: Entities_):
    return 1

def get_world_size():
    return 1

class Direction_:
    def __init__(self):
        return
    
North: Direction_ = 'north'
South: Direction_ = 'south'
East: Direction_ = 'East'
West: Direction_ = 'West'

def move(direction: Direction_):
    return 1

def can_harvest():
    return True

def harvest():
    return 


def till():
    '''
    밭 교체
    '''
    return

# start

while True:
    for x in range(get_world_size()):
        if can_harvest():
            harvest()
            
        if x == 1:
            is_plantable = plant(Entities.Grass)
            if not is_plantable:
                till()
                plant(Entities.Grass)
        elif x == 2:
            is_plantable = plant(Entities.Carrot)
            if not is_plantable:
                till()
                plant(Entities.Carrot)
        else:
            is_plantable = plant(Entities.Bush)
            if not is_plantable:
                till()
                plant(Entities.Bush)
        move(East)
    move(South)