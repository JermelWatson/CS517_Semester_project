import parse_temps
import sys
import math

def print_greeting():
    print("Hello world")


if __name__ == "__main__":
    print_greeting()
    result = []
    if len(sys.argv) :
        for i in range(2, len(sys.argv)):
            result.append(dec_to_any(int(sys.argv[1]), float(sys.argv[i]), MAX_DIGITS))