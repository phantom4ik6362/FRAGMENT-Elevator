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


# Function recives four arguments. Current floor (to exclude it from the list)
# Lowest floor, to make sure selected floor is not lower than lowest possible, and the same with highest.
# It also removes dublicates.
def validate_plan(current_floor, lowest_floor, highest_floor, plan):
    valid_plan = []
    plan = list(dict.fromkeys(plan))
    for floor in plan:
        if lowest_floor <= floor <= highest_floor and floor != current_floor:
            valid_plan.append(floor)
    return valid_plan