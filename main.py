from logic import plan_route
from logic import validate_plan

# ELEVATOR.OS By FRAGMENT
version = "0.1"

# Set highest, lowest floors of the building
# And a starting floor
lowest_floor = 1
highest_floor = 8
start_floor = 4

def main():
    print(f"Booting ELEVATOR.OS v{version}\n")
    print(f"CONTEXT: {highest_floor}-story building\nCurrently on {start_floor} floor\n")

    time_to_stop = False # Argument responsible for state of the cycle.
    current_floor = start_floor

    while not time_to_stop:
        cmd = input("%/: ").strip().lower()
        if cmd == "exit":
            print("Shutting down...")
            time_to_stop = True
        elif cmd == "help":
            print()
        else:
            cmd_list = cmd.split()
            if cmd_list[0] == "go":
                plan = []
                if len(cmd_list) < 3:
                    print("Error. Command is incomplete.")
                    continue
                if cmd_list[-1] != "up" and cmd_list[-1] != "down":
                    print(f"Error. (up/down) argument missing")
                    continue
                vertical = cmd_list[-1]
                cmd_list.pop(0)
                cmd_list.pop(-1)
                for el in cmd_list:
                    try:
                        el = int(el)
                        plan.append(el)
                    except ValueError:
                        print(f"Error. [{el}] is not a valid number.")
                        break
                verified_plan = validate_plan(current_floor, lowest_floor, highest_floor, plan)

                route = plan_route(current_floor, verified_plan, vertical)
                print(route)
                
            else:
                print("Error. Command unidenified. try help for help")

                
            

if __name__ == "__main__":
    main()