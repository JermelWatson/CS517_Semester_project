import parse_temps
import sys
import math

def print_greeting():
    print("Old Dominion CS517 Computational Methods")

def compute_piecewise_linear_interpolation(times: list[float], temps: list[float]):
    if len(times) == len(temps) and len(times) > 1:
        # Calculate the slope and y-intercept for each interval
        slope = []
        y_intercept = []

        for i, (t0, t1) in enumerate(zip(times[:-1], times[1:])):
            y0, y1 = temps[i], temps[i + 1]
            slope_value = (y1 - y0) / (t1 - t0)  # Calculate slope
            slope.append(slope_value)

            y_intcpt = y0 - (slope_value * t0)  # Calculate y-intercept
            y_intercept.append(y_intcpt)
        
        # Return both the slopes and y-intercepts for each segment
        return slope, y_intercept
    else:
        raise ValueError("The number of time and temperature values must be the same and greater than one.")

def save_to_file(core: list[float], slope: list[float], times: list[float] )
if __name__ == "__main__":
    print_greeting()
    
    times = []
    core_0 = []
    core_1 = []
    core_2 = []
    core_3 = []
    
    file_name = "src/cpu_temps.txt"
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
    core_0_slope, core_0_y_intercept = compute_piecewise_linear_interpolation(times=times, temps=core_0)
    core_1_slope, core_1_y_intercept = compute_piecewise_linear_interpolation(times=times, temps=core_1)
    core_2_slope, core_2_y_intercept = compute_piecewise_linear_interpolation(times=times, temps=core_2)
    core_3_slope, core_3_y_intercept = compute_piecewise_linear_interpolation(times=times, temps=core_3)
    
    # Print slopes and corresponding time ranges
    # First, determine the maximum length of the slope string with a sign
newFile = open("test_input_core-00.txt", "x")

max_slope_length = max(len(f"{slope:.4f}") for slope in core_0_slope)  # Including the negative sign

for i in range(4):
    newFile = open("test_input_core-0" + str(i) + ".txt", "x")
    for i in range(min(len(core_0_slope), 1000)):  # Loop over the slopes, up to 1000
        t0 = times[i]        # Current time
        t1 = times[i + 1]    # Next time
        slope = core_0_slope[i]
        
        # Format slope and determine if it has a negative sign
        slope_str = f"{slope:.4f}"  # Format the slope to four decimal places
        slope_display = slope_str.lstrip('-')  # Remove the negative sign for display alignment
        
        # Print with specified width for alignment
        #print(f"{t0:>3} <= x <= \t{t1:>10}; y = \t{core_0[i]:>10.4f} + \t{slope_str:>{max_slope_length}}{' x ; interpolation' if slope >= 0 else ' x ; interpolation'}")
        newFile.write(f"{t0:>3} <= x <= \t{t1:>10}; y = \t{core_0[i]:>10.4f} + \t\t\t{slope_str:>{max_slope_length}}{' x ; interpolation' if slope >= 0 else ' x ; interpolation'}\n")
        #Send data to file
    newFile.close()