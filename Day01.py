import os
import re

pattern = r"[^0-9]"

result = 0

def getTwodigits(string: str):
    onlyNumber = re.sub(pattern, "", string)
    return onlyNumber[0] + onlyNumber[-1]

if __name__ == "__main__":
    with open("source/day01/inputfile.txt") as inputfile:
        for line in inputfile:
            twodigits = int(getTwodigits(line.rstrip()))
            result += twodigits
        
    with open("source/day01/result.txt", "w") as resultfile:
        resultfile.write(str(result))

    