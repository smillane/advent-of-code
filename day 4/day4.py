import re

pp_dict = dict()
pp_list = []

with open("input.txt", "r") as file:
    reader = [x for x in file.read().strip().split("\n\n")]
    for x in reader:
        temp_split = re.split(r"\s", x)
        for y in temp_split:
            tempkey = y[:3]
            tempvalue = y[4:]
            pp_dict[tempkey] = tempvalue
        pp_list.append(pp_dict)
        pp_dict = {}

counter = 0
valid_pp_list = []
valid_pp_dict = {}

keylist = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

for pp in pp_list:
    if set(keylist).issubset(pp):
        counter += 1
        valid_pp_list.append(pp)

ecl_check = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
counter2 = -1
counter3 = 0

for pp in valid_pp_list:
    counter2 += 1
    #   BYR CHECK
    if int(pp['byr']) >= 1920:
        if int(pp['byr']) <= 2002:
            pass
        else:
            del valid_pp_list[counter2]
            continue
    else:
        del valid_pp_list[counter2]
        continue

    #   IYR CHECK
    if int(pp['iyr']) >= 2010:
        if int(pp['iyr']) <= 2020:
            pass
        else:
            del valid_pp_list[counter2]
            continue
    else:
        del valid_pp_list[counter2]
        continue

    #   EYR CHECK
    if int(pp['eyr']) >= 2020:
        if int(pp['eyr']) <= 2030:
            pass
        else:
            del valid_pp_list[counter2]
            continue
    else:
        del valid_pp_list[counter2]
        continue

    #   HGT CHECK
    if re.search('cm', pp['hgt']):
        if re.search('(?!cm).*', pp['hgt']):
            temp_value = pp['hgt'].split('c')[0]
            if int(temp_value) >= 150:
                if int(temp_value) <= 193:
                    pass
                else:
                    del valid_pp_list[counter2]
                    continue
            else:
                del valid_pp_list[counter2]
                continue
        else:
            del valid_pp_list[counter2]
            continue

    if re.search('in', pp['hgt']):
        if re.search('(?!in).*', pp['hgt']):
            temp_value = pp['hgt'].split('i')[0]
            if int(temp_value) >= 59:
                if int(temp_value) <= 76:
                    pass
                else:
                    del valid_pp_list[counter2]
                    continue
            else:
                del valid_pp_list[counter2]
                continue
        else:
            del valid_pp_list[counter2]
            continue

    if not re.search('(in|cm)', pp['hgt']):
        del valid_pp_list[counter2]
        continue

    #   HCL CHECK
    if len(pp['hcl']) == 7:
        if re.search('(?<=#)[a-f0-9]+', pp['hcl']):
            pass
        else:
            del valid_pp_list[counter2]
            continue
    else:
        del valid_pp_list[counter2]
        continue

    #   ECL CHECK
    if any(value in pp['ecl'] for value in ecl_check):
        pass
    else:
        del valid_pp_list[counter2]
        continue

    #   PID CHECK
    if len(pp['pid']) == 9:
        if re.search('[0-9]', pp['pid']):
            print(pp['pid'])
            pass
        else:
            del valid_pp_list[counter2]
            continue
    else:
        del valid_pp_list[counter2]
        continue

    counter3 += 1



print()
print(counter)
print(len(valid_pp_list))
print()
print(counter3)
print()
#for row in valid_pp_list:
#    print(row)