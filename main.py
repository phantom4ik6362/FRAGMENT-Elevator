from logic import plan_route
from logic import validate_plan

# ELEVATOR.OS By FRAGMENT
version = "0.1"

# Set highest, lowest floors of the building
# And a starting floor
lowest_floor = 1
highest_floor = 8
start_floor = 4

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
                if len(cmd_list) < 3: # command length test
                    print("Error. Command is incomplete.")
                    continue
                if cmd_list[-1] != "up" and cmd_list[-1] != "down": # argument checks
                    print(f"Error. (up/down) argument missing")
                    continue
                vertical = cmd_list[-1]
                cmd_list.pop(0)
                cmd_list.pop(-1)
                error = False
                for el in cmd_list: # remaining numbers are being appended to plan
                    try:
                        el = int(el)
                        plan.append(el)
                    except ValueError:
                        print(f"Error. [{el}] is not a valid number.")
                        error = True
                        break
                if error: # variable to transfer error out of the cycle
                    continue
                verified_plan = validate_plan(current_floor, lowest_floor, highest_floor, plan) # function validates data
                route = plan_route(current_floor, verified_plan, vertical) # function builds correct route
                print(f"Success! Current route: {route}") 
                while route:    
                    print(f"Elevator moved from {current_floor} to {route[0]}")
                    current_floor = route[0]
                    route.pop(0)
                    selected_buttons, time_to_stop = request_buttoninput()
                    if time_to_stop:
                        break
                    verified_selectedbuttons = validate_plan(current_floor, lowest_floor, highest_floor, selected_buttons)
                    new_route = route + verified_selectedbuttons
                    route = plan_route(current_floor, new_route, vertical)
            else:
                print("Error. Command unidenified. try help for help")


if __name__ == "__main__":
    main() # Starts main loop in case of a correct entry point