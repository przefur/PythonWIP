with open("input4.txt", 'r') as f:
    input_string = f.readlines()

def passportGetter(input_string):
    passport = {}
    listofpassports = []
    for line in input_string:
        if line != "\n":
            line = line.rstrip().split(" ")
            line = [field.split(":") for field in line]
            for field in line:
                passport[field[0]] = field[1]
        else:
            listofpassports.append(passport)
            passport = {}
    listofpassports.append(passport)
    return listofpassports

def answer1(listofpassports):
    count = 0
    for passport in listofpassports:
        if len(passport) == 8 and 'cid' in passport or len(passport) == 7 and 'cid' not in passport:
            count += 1
    return count
    
def answer2(listofpassports):
    count = 0
    for passport in listofpassports:
        checks = 0
        if len(passport) == 8 and 'cid' in passport or len(passport) == 7 and 'cid' not in passport:
            if 1920 <= int(passport.get('byr')) <= 2002:
                checks += 1
            if 2010 <= int(passport.get('iyr')) <= 2020:
                checks += 1
            if 2020 <= int(passport.get('eyr')) <= 2030:
                checks += 1
            if (passport.get('hgt')[-2:] == 'cm' and 150 <= int(passport.get('hgt')[:-2]) <= 193) or (passport.get('hgt')[-2:] == 'in' and 59 <= int(passport.get('hgt')[:-2]) <= 76):
                checks += 1
            if passport.get('hcl')[0] == '#' and passport.get('hcl')[1:].isalnum():
                checks += 1
            if passport.get('ecl') in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                checks += 1
            if len(passport.get('pid')) == 9:
                checks += 1
            if checks == 7:
                count += 1
    return count
                
print(answer1(passportGetter(input_string)))
print(answer2(passportGetter(input_string)))
