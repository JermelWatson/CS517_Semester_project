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
        slopes1.append(slopes)

        # Calculate y-intercepts (y_intercept = y - mx)
        y_intercepts = temps_np[:-1] - slopes * times_np[:-1]
        intercepts.append(y_intercepts)

        # Print slopes and intercepts
        #for slope, y_intcpt in zip(slopes, y_intercepts):
        #    print(f"{slope=}, {y_intcpt=}")
        return(slopes1, intercepts)

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

        # Compute the piecewise linear interpolation for core_3
    core_0_slope, core_0_y_intercept = compute_line_interpolation(times=times, temps=core_0)
    core_1_slope, core_1_y_intercept = compute_line_interpolation(times=times, temps=core_1)
    core_2_slope, core_2_y_intercept = compute_line_interpolation(times=times, temps=core_2)
    core_3_slope, core_3_y_intercept = compute_line_interpolation(times=times, temps=core_3)
    
    # Print slopes and corresponding time ranges
    # First, determine the maximum length of the slope string with a sign
    max_slope_length = max(len(f"{slope:.4f}") for slope in core_0_slope.flatten())  # Including the negative sign

    for i in range(min(len(core_0_slope), 1000)):  # Loop over the slopes, up to 1000
        t0 = times[i]        # Current time
        t1 = times[i + 1]    # Next time
        slope = core_0_slope[i]
        
        # Format slope and determine if it has a negative sign
        slope_str = f"{slope:.4f}"  # Format the slope to four decimal places
        slope_display = slope_str.lstrip('-')  # Remove the negative sign for display alignment
        
        # Print with specified width for alignment
        print(f"{t0:>3} <= x <= \t{t1:>10}; y = \t{core_0[i]:>10.4f} + \t{slope_display:>{max_slope_length}}{' x ; interpolation' if slope >= 0 else ' x ; interpolation'}")