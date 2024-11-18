import numpy as np
from Least_Squares_Approximation import least_squares_approximation

def save_to_file(core: np.ndarray, slope: np.ndarray, times: np.ndarray, core_idx: int):
    """
    Saves formatted output to a new output file.

    Args:
        core (np.ndarray): Array of temperatures for core_idx.
        slope (np.ndarray): Array of slopes relating to the core values.
        times (np.ndarray): Array of times.
        core_idx (int): Index value of core (e.g., 0, 1, 2, 3).
    """
    # Compute least squares approximation for the current core
    core_ls_slope, core_ls_intercept = least_squares_approximation(times=times, temps=core)

    # Open the output file
    output_file = f"output-core-{core_idx}.txt"
    with open(output_file, "w") as newFile:
        max_slope_length = max(len(f"{slp:.4f}") for slp in slope)

        # Write piecewise interpolation results
        for i in range(len(slope)):  # Loop over the slopes
            t0 = times[i]        # Current time
            t1 = times[i + 1]    # Next time
            curr_slope = slope[i]

            # Format and write to the file
            slope_str = f"{curr_slope:.4f}"
            newFile.write(
                f"{t0:>3} <= x <= \t{t1:.2f}; y = {core[i]:.4f} + {slope_str:>{max_slope_length}} x\n"
            )

        # Write least squares line at the end
        newFile.write(f"{times[0]:>3} <= x <= \t{times[-1]:>10}; y = \t\t {core_ls_intercept:.4f} + \t\t   {core_ls_slope:.4f} x least-squares")
    

    print(f"Core {core_idx}: Data written to {output_file}")
