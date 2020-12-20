import re

REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

VALIDATORS = {
    'byr': lambda value : re.match(r'\d\d\d\d', value) and int(value) >= 1920 and int(value) <= 2002,
    'iyr': lambda value : re.match(r'\d\d\d\d', value) and int(value) >= 2010 and int(value) <= 2020,
    'eyr': lambda value : re.match(r'\d\d\d\d', value) and int(value) >= 2020 and int(value) <= 2030,
    'hgt': lambda value : heightIsOk(value),
    'hcl': lambda value : re.match(r'#[0-9a-f]{6}', value),
    'ecl': lambda value : re.match(r'amb|blu|brn|gry|grn|hzl|oth', value),
    'pid': lambda value : re.match(r'\d{9}', value)
}

def heightIsOk(value):
    if (match := re.match(r'(\d\d\d?)(\w\w)', value)):
        amount = int(match.group(1))
        unit = match.group(2)
        return (
            (unit == 'cm' and amount >= 150 and amount <= 193) or
            (unit == 'in' and amount >= 59 and amount <= 76)
        )
    return False

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

    print(f'{valid} valid out of {len(passports)}')