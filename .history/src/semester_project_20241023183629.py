import parse_temps
import sys
import math

def print_greeting():
    print("Old Dominion CS517 Computational Methods")
    
    
def compute_line_interpolation(times: list[float], temps: list[float]):
    if len(times) == len(temps) and len(times) > 1:
        # Calculate the slope of the line
        slope = []
        y_intercept = []

        for i, (t0, t1) in enumerate(zip(times[:-1], times[1:])):
            y0, y1 = temps[i], temps[i + 1]
            slope_value = (y1 - y0) / (t1 - t0)  # Calculate slope
            slope.append(slope_value)

            y_intcpt = y0 - (slope_value * t0)  # Calculate y-intercept
            y_intercept.append(y_intcpt)
            print(f"{slope_value=}, {y_intcpt=}")
            return(slope, y_intercept)


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

            # Print the time step and temperatures
            print((time_step, temps))
    core_0_slope, core_0_compute_line_interpolation(times=times, temps=core_0)