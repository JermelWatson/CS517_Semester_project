import parse_temps
import sys
import math

def print_greeting():
    print("Hello world")


if __name__ == "__main__":
    print_greeting()
    result = []
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    
    file_name = "src/cpu_temps.txt"
    file = open(file_name, "r")
    for line in file:
        print(line)
        
    