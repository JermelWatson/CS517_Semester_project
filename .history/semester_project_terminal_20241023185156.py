from src import parse_temps
import sys
import math
import numpy as np

def print_greeting():
    print("Hello world")
    
def compute_line_interpolation(times: list[float], temps: list[float]):
    # Convert input lists to NumPy arrays
    times_np = np.array(times)
    temps_np = np.array(temps)
    
    slopes1 = []
    intercepts = []

    if len(times_np) == len(temps_np) and len(times_np) > 1:
        # Calculate the differences in temps and times
        delta_t = times_np[1:] - times_np[:-1]
        delta_y = temps_np[1:] - temps_np[:-1]

        # Calculate slopes (m = Δy / Δx)
        slopes = delta_y / delta_t
        slopes1.append(slope)

        # Calculate y-intercepts (y_intercept = y - mx)
        y_intercepts = temps_np[:-1] - slopes * times_np[:-1]
        intercepts.append(y_intercepts)

        # Print slopes and intercepts
        #for slope, y_intcpt in zip(slopes, y_intercepts):
        #    print(f"{slope=}, {y_intcpt=}")
        return()

if __name__ == "__main__":
    print_greeting()
    
    times = []
    core_0 = []
    core_1 = []
    core_2 = []
    core_3 = []
    
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
            #print((time_step, temps))
    core_0_slope, core_0_y_incept = compute_line_interpolation(times=times, temps=core_3)
    print(core_0_slope)