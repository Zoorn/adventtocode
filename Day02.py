from typing import List
import re
import os

if __name__ == "__main__":
    patternNumber = r"[^0-9]"
    patternAlpha = r"[^a-z]"
    cubes = {
        "red": 12,
        "green": 13,
        "blue": 14
        }

    endresult = 0
    part2result = 0
    lines = []
    linesok = []
    file = os.path.join(os.path.dirname(__file__),"source/day02/inputfile.txt")

    with open(file) as inputfile:
        lines = [line.rstrip() for line in inputfile if line.strip()]
    
    # part 1
    for line in lines:
        content = line.rstrip()
        id, rightpart = content.split(":")
        id = re.sub(patternNumber, "", id)

        highest = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        sets = rightpart.split(";")

        setOK = True
        for set in sets:
            results = set.split(",")
            for result in results:
                number =  int(re.sub(patternNumber, "", result))
                color = re.sub(patternAlpha, "", result)
                if highest[color] < number:
                    highest[color] = number
                if cubes[color] < number:
                   setOK = False

        # part 1
        if setOK:
            endresult += int(id)
        
        # part 2
        tmpresult = 1
        for entry in highest.values():
            tmpresult *= entry
        part2result += tmpresult
        

    # save result  
    resultfile = os.path.join(os.path.dirname(__file__),"source/day02/result.txt")

    with open(resultfile, "w") as rfile:
        rfile.write(str(endresult) + "\n" + str(part2result))

                    
            



    

