def make_tea(tea_bag:str, water:str, quantity_milk:int, quantity_sugar:int):
    transition_state:list = ['black', 'brown-ish', 'clear']
    if water == 'hot':
        print("Pouring into a cup")
    else:
        print("Preparing a hot water...")
    print(f"{tea_bag} inserted into cup")
    while transition_state:
        print(f"state {transition_state.pop()}")
    print("Taking the bag out")
    print(f"Adding {quantity_milk} tea-spoons of milk into tea")
    print(f"Adding {quantity_sugar} tea-spoons of sugar into tea")


def make_tea(tea_bag:str, water:str, milk:bool, sugar:bool):
    transition_state:list = ['black', 'brown-ish', 'clear']
    if water == 'hot':
        print("Pouring into a cup")
    else:
        print("Preparing a hot water...")
    print(f"{tea_bag} inserted into cup")
    while transition_state:
        print(f"state {transition_state.pop()}")
    print("Taking the bag out")
    print(f"Adding  of milk to tea" if milk == True else "No milk then")
    print(f"Adding  sugar to tea" if sugar == True else "No sugar then")
        
make_tea('black tea', 'hot', False, True)