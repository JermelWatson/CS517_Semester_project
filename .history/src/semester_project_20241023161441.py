import parse_temps
import sys
import math

def print_greeting():
    print("Hello world")


if __name__ == "__main__":
    print_greeting()
    result = []
    if len(sys.argv) == 2:
        file = sys.argv[1]
    
    