from itertools import islice
import re

passpatt = re.compile(r'(\d+)-(\d+) (.): (.+)')

with open("indata-dec02.txt") as indata:
    lines = list(indata)
    numbers = list()
    okPwds = 0
    for line in lines:
        match = passpatt.match(line)
        if match:
            (minOccurs, maxOccurs, charToCheck, password) = (int(match.group(1)), int(match.group(2)), match.group(3), match.group(4))
            charOccurences = len([char for char in password if char == charToCheck])
            if charOccurences >= minOccurs and charOccurences <= maxOccurs:
                okPwds += 1
    print(okPwds)
