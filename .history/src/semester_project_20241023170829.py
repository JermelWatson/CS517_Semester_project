import parse_temps
import sys
import math

def print_greeting():
    print("Hello world")


if __name__ == "__main__":
    print_greeting()
    
    
    result = []
    core_0 = []
    core_1 = []
    core_2 = []
    core_3 = []
    
    file_name = "src/cpu_temps.txt"
    with open(file_name, "r") as file:
        parsed_temps = parse_temps.parse_raw_temps(file)
    
    for x, y in parsed_temps:
        print(x,y)