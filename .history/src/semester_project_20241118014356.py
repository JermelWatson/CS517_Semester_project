import parse_temps
import sys
import math
from compute_piecewise_linear_interpolation import compute_piecewise_linear_interpolation
from Least_Squares_Approximation import least_squares_approximation

def print_greeting():
    print("\n****Old Dominion CS517 Computational Methods****")

def save_to_file(core: list[float], slope: list[float], times: list[float], core_idx: int):
    """Summary: [Saves formatted output to new output file]

    Args:
        core (list[float]): list of temperatures for core_idx
        slope (list[float]): list of slopes relating to the core values
        times (list[float]): list of times
        core_idx (int): index value of core e.g 0,1,2,3
    """
    #*I could use mode 'x' or 'w+' to open the file so that the file would not be overwritten
    #* if it already exist, but for now, due to constant testing 'w' is fine.
    core_0_ls_slope, core_0_ls_intercept = least_squares_approximation(times=times, temps=core)
    
    newFile = open("output-core-0" + str(core_idx) + ".txt", "w")
    
    max_slope_length = max(len(f"{slp:.4f}") for slp in slope)  
    
    for i in range(len(slope)):#* Loop over the slopes
        t0 = times[i]        #* Current time
        t1 = times[i + 1]    #* Next time
        curr_slope = slope[i]
        
        #* Format slope and determine if it has a negative sign
        slope_str = f"{curr_slope:.4f}"  #* Format the slope to four decimal places
        
        #*Writes data to file
        newFile.write(f"{t0:>3} <= x <= \t{t1:>10}; y = \t{core[i]:>10.4f} + \t\t\t{slope_str:>{max_slope_length}}{' x ; interpolation' if curr_slope >= 0 else ' x ; interpolation'}\n")
    newFile.write(f"{times[0]:>3} <= x <= \t{times[-1}; y = \t{core_0_ls_intercept:.4f} + {core_0_ls_slope:.4f}x least-squares")
    newFile.close()
    
if __name__ == "__main__":
    print_greeting()
    file_name = ""
    times = []
    core_0 = []
    core_1 = []
    core_2 = []
    core_3 = []
    
    #?Lines for testing
    #* file_name = "src/cpu_temps.txt"
    #* with open(file_name, "r") as file:
    #*     parsed_temps = parse_temps.parse_raw_temps(file)
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    
    #!Exits if file name argument is not provided
    if file_name == '':
        exit()
        
    with open(file_name, "r") as file:
        parsed_temps = parse_temps.parse_raw_temps(file)
        #* Iterate through the parsed temperature data
        for time_step, temps in parsed_temps:
            times.append(time_step)
            #* Make sure there are exactly four temperatures
            if len(temps) >= 4:
                core_0.append(temps[0])
                core_1.append(temps[1])
                core_2.append(temps[2])
                core_3.append(temps[3])

    #* Compute the slope and y- linear interpolation for core_3
    core_0_slope, core_0_y_intercept = compute_piecewise_linear_interpolation(times=times, temps=core_0)
    core_1_slope, core_1_y_intercept = compute_piecewise_linear_interpolation(times=times, temps=core_1)
    core_2_slope, core_2_y_intercept = compute_piecewise_linear_interpolation(times=times, temps=core_2)
    core_3_slope, core_3_y_intercept = compute_piecewise_linear_interpolation(times=times, temps=core_3)
    
    #* Print slopes and corresponding time ranges
    #* First, determine the maximum length of the slope string with a sign
    save_to_file(core=core_0, slope=core_0_slope, times=times, core_idx=0)
    save_to_file(core=core_1, slope=core_1_slope, times=times, core_idx=1)
    save_to_file(core=core_2, slope=core_2_slope, times=times, core_idx=2)
    save_to_file(core=core_3, slope=core_3_slope, times=times, core_idx=3)
    print("Process completed.\nOutput files created successfully!!")
    
    