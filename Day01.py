import os
import re

pattern = r"[^0-9]"

result = 0

numbers = [
    {r"(?<=o)n(?=e)": "1"},
    {r"(?<=t)w(?=o)": "2"},
    {r"(?<=t)hre(?=e)": "3"},
    {r"(?<=f)ou(?=r)": "4"},
    {r"(?<=f)iv(?=e)": "5"},
    {r"(?<=s)i(?=x)": "6"},
    {r"(?<=s)eve(?=n)": "7"},
    {r"(?<=e)igh(?=t)": "8"},
    {r"(?<=n)in(?=e)": "9"}
]


def changeNumber(line: str):
    for number in numbers:
        for key, value in number.items():
            line = re.sub(key, value, line)
    return line


def getTwodigits(string: str):
    onlyNumber = re.sub(pattern, "", string)
    return onlyNumber[0] + onlyNumber[-1]

if __name__ == "__main__":
    lines = []
    result = 0
    resulttwo = 0
    with open("source/day01/inputfile.txt") as inputfile:
        for line in inputfile:
            lines.append(line)

    for line in lines:
        # part 1
        twodigits = int(getTwodigits(line.rstrip()))
        result += twodigits

        #part 2
        twodigits = int(getTwodigits(changeNumber(line.rstrip())))
        resulttwo += twodigits

    with open("source/day01/result.txt", "w") as resultfile:
        resultfile.write(str(result) + "\n" + str(resulttwo))

    