from itertools import islice

REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
OPTIONAL_FIELDS = ['cid']

with open("dec04-indata.txt") as indata:
    rows = [line.strip() for line in list(indata)]

    valid = 0
    invalid = 0

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
            passports[-1] = passports[-1] | fields
    
    for passport in passports:
        if all(passport.get(key) for key in REQUIRED_FIELDS):
            valid += 1
        else:
            invalid += 1

    print(valid, invalid)