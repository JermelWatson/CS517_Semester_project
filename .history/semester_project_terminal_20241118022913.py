from src import parse_temps
import sys
import numpy as np
from Least_Squares_Approximation import least_squares_approximation
from Linear_Interpolation import compute_line_interpolation
from create_output import save_to_file

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
    
    # Check for command-line argument
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    if file_name == '':
        print("Error: No input file provided.")
        sys.exit(1)

    # Read and parse the input file
    with open(file_name, "r") as file:
        parsed_temps = parse_temps.parse_raw_temps(file)

        # Collect temperature data
        for time_step, temps in parsed_temps:
            times.append(time_step)
            if len(temps) >= 4:  # Ensure sufficient data for all cores
                core_0.append(temps[0])
                core_1.append(temps[1])
                core_2.append(temps[2])
                core_3.append(temps[3])

    # Convert lists to NumPy arrays for efficient computation
    times = np.array(times)
    core_0 = np.array(core_0)
    core_1 = np.array(core_1)
    core_2 = np.array(core_2)
    core_3 = np.array(core_3)

    # Compute the least squares line for core_0
    core_0_ls_slope, core_0_ls_intercept = least_squares_approximation(times=times, temps=core_0)
    print(f"Core 0 Least Squares Line: y = {core_0_ls_slope:.4f}x + {core_0_ls_intercept:.4f}")

    # Compute piecewise linear interpolation for all cores
    core_0_slopes, core_0_intercepts = compute_line_interpolation(times=times, temps=core_0)
    core_1_slopes, core_1_intercepts = compute_line_interpolation(times=times, temps=core_1)
    core_2_slopes, core_2_intercepts = compute_line_interpolation(times=times, temps=core_2)
    core_3_slopes, core_3_intercepts = compute_line_interpolation(times=times, temps=core_3)

    # Save results to files
    save_to_file(core=core_0, slope=core_0_slopes, times=times, core_idx=0)
    save_to_file(core=core_1, slope=core_1_slopes, times=times, core_idx=1)
    save_to_file(core=core_2, slope=core_2_slopes, times=times, core_idx=2)
    save_to_file(core=core_3, slope=core_3_slopes, times=times, core_idx=3)

    print("Process completed. Output files created successfully!")
