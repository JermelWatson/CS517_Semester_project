def compute_piecewise_linear_interpolation(times: list[float], temps: list[float]):
    """Summary: [The compute_piecewise_linear_interpolation function calculates the slope and y-intercept and 
    returns those values.]

    Args:
        times (list[float]): List of times 30 seconds apart per temperature reading
        temps (list[float]): List of core temperatures extracted from file

    Raises:
        ValueError: captures a value error

    Returns:
        Tuple: return tuple containing to lists
    """
    if len(times) == len(temps) and len(times) > 1:
        #* Calculate the slope and y-intercept for each interval
        slope = []
        y_intercept = []

        for i, (t0, t1) in enumerate(zip(times[:-1], times[1:])):
            y0, y1 = temps[i], temps[i + 1]
            slope_value = (y1 - y0) / (t1 - t0)  # Calculate slope
            slope.append(slope_value)

            y_intcpt = y0 - (slope_value * t0)  # Calculate y-intercept
            y_intercept.append(y_intcpt)
        
        #* Return both the slopes and y-intercepts for each segment
        return slope, y_intercept
    else:
        #! Error: Mismatch list indices
        raise ValueError("The number of time and temperature values must be the same and greater than one.")
