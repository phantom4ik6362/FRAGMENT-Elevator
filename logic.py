# Logical functions of the elevator

# Function recives 3 arguments. Current floor, list of
# planned floors (pressed buttons) and was last entry
# direction set to up or down
def plan_route(current_floor, plan_bulk, vertical):
    route = []
    temp_route = []
    if vertical == "up":
        for floor in plan_bulk:
            if floor > current_floor:
                route.append(floor)
        route.sort(reverse=False)
        for floor in plan_bulk:
            if floor < current_floor:
                temp_route.append(floor)
        temp_route.sort(reverse=True)
        route += temp_route
    elif vertical == "down":
        for floor in plan_bulk:
            if floor < current_floor:
                route.append(floor)
        route.sort(reverse=True)
        for floor in plan_bulk:
            if floor > current_floor:
                temp_route.append(floor)
        temp_route.sort(reverse=False)
        route += temp_route
    return route


print(plan_route(3, [8, 5, 6, 9, 4, 1, 2], "down"))