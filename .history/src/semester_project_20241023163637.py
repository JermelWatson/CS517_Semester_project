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
    list = parse_temps.parse_raw_temps(file_name, )
    file = open(file_name, "r")
    for line in file:
        temps = line.split(" ")
        core_0.append(temps[0]) 
        core_1.append(temps[1]) 
        core_2.append(temps[2]) 
        core_3.append(temps[3]) 
        
    print(core_0)