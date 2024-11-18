from Least_Squares_Approximation import least_squares_approximation

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
    newFile.write(f"{times[0]:>3} <= x <= \t{times[-1]:>10}; y = \t\t {core_0_ls_intercept:.4f} + \t\t   {core_0_ls_slope:.4f} x least-squares")
    newFile.close()
