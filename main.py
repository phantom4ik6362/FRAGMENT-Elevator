from logic import plan_route
from logic import validate_plan

# ELEVATOR.OS By FRAGMENT
version = "0.1"

# Set highest, lowest floors of the building
# And a starting floor
lowest_floor = 1
highest_floor = 8
start_floor = 1

def request_buttoninput():
    cyclecontrol_variable = False
    time_to_stop = False
    selected_buttons = []
    while not cyclecontrol_variable:   
        inelevator_button = input("Elevator doors have opened...\n---\nElevator door have closed...\n\nAny more floors selected?(yes 1 2 3/no): ").lower().strip()
        if inelevator_button == "no":
            cyclecontrol_variable = True
        elif inelevator_button == "exit":
            print("Shutting down...")
            time_to_stop = True
            cyclecontrol_variable = True
        else:
            inelevator_button = inelevator_button.split()
            if len(inelevator_button) < 2:
                print("Error. Try again (no/yes 4 5 6)")
                continue
            else:
                if inelevator_button[0] == "yes":
                    inelevator_button.pop(0)
                    try:
                        inelevator_button = list(map(int, inelevator_button))
                    except ValueError:
                        print("Error. Try again (no/yes 4 5 6)")
                        continue
                    selected_buttons = inelevator_button
                    cyclecontrol_variable = True                                        
                else:
                    print("Error. Try again (no/yes 4 5 6)")
    return selected_buttons, time_to_stop

def has_out_of_range(lowest_floor, highest_floor, plan):
    outofrange = False
    for el in plan:
        if el <= highest_floor and el >= lowest_floor:
            continue
        else:
            outofrange = True
            break
    return outofrange


def main():
    print(f"Booting ELEVATOR.OS v{version}\n")
    print(f"CONTEXT: {highest_floor}-story building\nCurrently on {start_floor} floor\n")

    time_to_stop = False # Flag-variable responsible for state of the cycle.
    current_floor = start_floor

    while not time_to_stop: # Main cycle
        cmd = input("%/: ").strip().lower() # user input (string)
        if cmd == "":
            print("Error. Command is incomplete.")
            continue
        if cmd == "exit":
            print("Shutting down...")
            time_to_stop = True
        elif cmd == "help":
            print()
        else:
            cmd_list = cmd.split() # user's input transforms into a list
            if cmd_list[0] == "go": # cmd "go" is spotted
                plan = [] # unverified list of potential floors
                if len(cmd_list) != 3: # command length test
                    print("Error. Command is incomplete.")
                    continue
                if cmd_list[-1] != "up" and cmd_list[-1] != "down": # argument checks
                    print("Error. (up/down) argument missing")
                    continue
                vertical = cmd_list[-1]
                cmd_list.pop(0)
                cmd_list.pop(-1)
                try:
                    cmd_list[0] = int(cmd_list[0])
                except ValueError:
                    print("Error. The floor elevator was called from must be a number.")
                    continue
                if cmd_list[0] == highest_floor and vertical == "up":
                    print("Error. You can't go up from the top floor.")
                    continue
                elif cmd_list[0] == lowest_floor and vertical == "down":
                    print("Error. You can't go down from the lowest floor.")
                    continue
                if cmd_list[0] < lowest_floor or cmd_list[0] > highest_floor:
                    print("Error. The floor elevator was called is not in range.")
                    continue
                awaiting_input = True
                while awaiting_input:
                    current_floor = cmd_list[0]
                    plan = input(f"Elevator arrived to {cmd_list[0]} floor. Please insert what buttons were pressed: ").lower().strip()
                    if plan == "exit":
                        print("Shutting down...")
                        awaiting_input = False
                        time_to_stop = True
                        continue
                    elif len(plan) == 0:
                        print("Error. Try again.")
                        continue
                    plan = plan.split()
                    try:
                        plan = list(map(int, plan))
                    except ValueError:
                        print("Error. Try again.")
                        continue
                    if has_out_of_range(lowest_floor, highest_floor, plan):
                        print("Selected floor (floors) out of range.")
                        continue
                    verified_plan = validate_plan(current_floor, lowest_floor, highest_floor, plan) # function validates data
                    route = plan_route(current_floor, verified_plan, vertical) # function builds correct route
                    awaiting_input = False
                    print(f"Success! Current route: {route}") 
                    while route:    
                        print(f"Elevator moved from {current_floor} to {route[0]}")
                        current_floor = route[0]
                        route.pop(0)
                        selected_buttons, time_to_stop = request_buttoninput()
                        if time_to_stop:
                            awaiting_input = False
                            break
                        verified_selectedbuttons = validate_plan(current_floor, lowest_floor, highest_floor, selected_buttons)
                        new_route = route + verified_selectedbuttons
                        route = plan_route(current_floor, new_route, vertical)
                    if time_to_stop:
                        break
                    print("Route completed. use GO for next one or exit to quit\n")
            else:
                print("Error. Command unidenified. try help for help")

if __name__ == "__main__":
    main() # Starts main loop in case of a correct entry point