from src import parse_temps
import sys
import math
import numpy as np

def print_greeting():
    print("Hello world")

def compute_line_interpolation(times: list[float], temps: list[float]):
    """
    Compute piecewise linear interpolation between consecutive points.
    
    Args:
        times (list[float]): List of time values.
        temps (list[float]): List of temperature values.
    
    Returns:
        tuple: List of slopes and intercepts for each segment.
    """
    times_np = np.array(times)
    temps_np = np.array(temps)
    
    slopes = []
    intercepts = []

    if len(times_np) == len(temps_np) and len(times_np) > 1:
        # Calculate the differences in temps and times
        delta_t = times_np[1:] - times_np[:-1]
        delta_y = temps_np[1:] - temps_np[:-1]

        # Calculate slopes (m = Δy / Δx)
        slopes = delta_y / delta_t

        # Calculate y-intercepts (y_intercept = y - mx)
        intercepts = temps_np[:-1] - slopes * times_np[:-1]

    return slopes, intercepts

def least_squares_approximation(times: list[float], temps: list[float]):
    """
    Compute the least squares approximation for a linear relationship
    between times and temps using the (X^T X)^-1 X^T Y method.

    Args:
        times (list[float]): List of time values (independent variable).
        temps (list[float]): List of temperature values (dependent variable).

    Returns:
        tuple: Coefficients (slope, intercept) of the least squares line.
    """
    times_np = np.array(times)
    temps_np = np.array(temps)
    
    if len(times_np) != len(temps_np) or len(times_np) < 2:
        raise ValueError("Input lists must have the same length and contain at least two points.")
    
    # Construct the design matrix X
    X = np.vstack([times_np, np.ones(len(times_np))]).T
    
    # Compute the least squares solution
    coefficients = np.linalg.inv(X.T @ X) @ X.T @ temps_np
    
    return coefficients[0], coefficients[1]  # slope, intercept

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
