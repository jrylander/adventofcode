from itertools import islice

with open("dec04-indata.txt") as indata:
    rows = [line.strip() for line in list(indata)]
    createNew = True
    passports = []
    for row in rows:
        if row == '':
            createNew = True
        else:
            if createNew:
                passports.append({})
                createNew = False
            fields = {field.split(':')[0]: field.split(':')[1] for field in row.split(' ')}
            passports[-1] = {**passports[-1], **fields}

    valid = 0
    invalid = 0
    print(valid, invalid)