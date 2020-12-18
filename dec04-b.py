import re

REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

VALIDATORS = {
    'byr': lambda value : re.match(r'\d\d\d\d', value),
    'iyr': lambda value : re.match(r'\d\d\d\d', value),
    'eyr': lambda value : re.match(r'\d\d\d\d', value),
    'hgt': lambda value : re.match(r'\d\d\d?\w\w', value),
    'hcl': lambda value : re.match(r'#[0-9a-f]{6}', value),
    'ecl': lambda value : re.match(r'amb|blu|brn|gry|grn|hzl|oth', value),
    'pid': lambda value : re.match(r'\d{9}', value)
}

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
        if ( all(passport.get(key) for key in REQUIRED_FIELDS) and
             all(not VALIDATORS.get(key) or VALIDATORS[key](passport[key]) for key in passport.keys()) ):
            valid += 1
        else:
            invalid += 1

    print(valid, invalid)