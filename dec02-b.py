from itertools import islice
import re

passpatt = re.compile(r'(\d+)-(\d+) (.): (.+)')

with open("dec02-indata.txt") as indata:
    lines = list(indata)
    numbers = list()
    okPwds = 0
    for line in lines:
        match = passpatt.match(line)
        if match:
            (firstPos, secondPos, charToCheck, password) = (int(match.group(1)), int(match.group(2)), match.group(3), match.group(4))
            (first, second) = (password[firstPos-1], password[secondPos-1])
            if first != second and (first == charToCheck or second == charToCheck):
                okPwds += 1
    print(okPwds)
