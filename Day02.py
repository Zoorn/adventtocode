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
    lines = []
    file = os.path.join(os.path.dirname(__file__),"source/day02/inputfile.txt")

    with open(file) as inputfile:
        lines = [line.rstrip() for line in inputfile if line.strip()]
    
    for line in lines:
        content = line.rstrip()
        id, rightpart = content.split(":")
        id = re.sub(patternNumber, "", id)


        sets = rightpart.split(";")

        setOK = True
        for set in sets:
            results = set.split(",")
            for result in results:
                number =  re.sub(patternNumber, "", result)
                color = re.sub(patternAlpha, "", result)
                if cubes[color] < int(number):
                   setOK = False
                   break
            if not setOK:
                break
        if setOK:
            endresult += int(id)
        
    resultfile = os.path.join(os.path.dirname(__file__),"source/day02/result.txt")

    with open(resultfile, "w") as rfile:
        rfile.write(str(endresult))

                    
            



    

