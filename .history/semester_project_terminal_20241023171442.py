from src import parse_temps
import sys
import math

def print_greeting():
    print("Hello world")


if __name__ == "__main__":
    print_greeting()
    result = []
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    
    with open(file_name, "r") as file:
        parsed_temps = parse_temps.parse_raw_temps(file)

        # Iterate through the parsed temperature data
        for time_step, temps in parsed_temps:
            times.append(time_step)
            # Make sure there are exactly four temperatures
            if len(temps) >= 4:
                core_0.append(temps[0])
                core_1.append(temps[1])
                core_2.append(temps[2])
                core_3.append(temps[3])

            # Print the time step and temperatures
            print((time_step, temps))
    print(times)