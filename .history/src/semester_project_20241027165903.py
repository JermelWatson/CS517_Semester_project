import parse_temps

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

def evaluate_interpolation(times: list[float], slope: list[float], y_intercept: list[float], query_time: float):
    # Find the appropriate interval for the given query time
    for i, (t0, t1) in enumerate(zip(times[:-1], times[1:])):
        if t0 <= query_time <= t1:
            # Calculate the interpolated temperature using the slope and y-intercept
            return slope[i] * query_time + y_intercept[i]
    raise ValueError("Query time is out of the interpolation range.")

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
    core_3_slope, core_3_y_intercept = compute_piecewise_linear_interpolation(times=times, temps=core_3)

    # Example: Evaluate the interpolation at a specific query time
    query_time = 
    try:
        interpolated_temp = evaluate_interpolation(times, core_3_slope, core_3_y_intercept, query_time)
        print(f"The interpolated temperature at time {query_time} is {interpolated_temp:.2f}")
    except ValueError as e:
        print(e)
