from src import parse_temps
import sys
import math
import numpy as np
from Least_Squares_Approximation import least_squares_approximation
from L

def print_greeting():
    print("Hello world")

if __name__ == "__main__":
    print_greeting()
    file_name = ''
    times = []
    core_0 = []
    core_1 = []
    core_2 = []
    core_3 = []
    
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    if file_name == '':
        exit()
    with open(file_name, "r") as file:
        parsed_temps = parse_temps.parse_raw_temps(file)

        # Collect temperature data
        for time_step, temps in parsed_temps:
            times.append(time_step)
            if len(temps) >= 4:
                core_0.append(temps[0])
                core_1.append(temps[1])
                core_2.append(temps[2])
                core_3.append(temps[3])

    # Compute the least squares line for core_0
    core_0_ls_slope, core_0_ls_intercept = least_squares_approximation(times=times, temps=core_0)
    print(f"Core 0 Least Squares Line: y = {core_0_ls_slope:.4f}x + {core_0_ls_intercept:.4f}")

    # Compute piecewise linear interpolation for core_0
    core_0_slopes, core_0_intercepts = compute_line_interpolation(times=times, temps=core_0)

    # Print piecewise interpolation results
    for i in range(len(core_0_slopes)):
        t0, t1 = times[i], times[i + 1]
        slope, intercept = core_0_slopes[i], core_0_intercepts[i]
        print(f"{t0:.2f} <= x <= {t1:.2f}; y = {slope:.4f}x + {intercept:.4f}")
