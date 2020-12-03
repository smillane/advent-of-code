import re

input_list = []
with open("input.txt", "r") as input_file:
    input_list = [line for line in input_file if line.strip()]

master_list = []

for item in input_list:
    min_max = re.findall('\d+', item)
    min_max_int = list(map(int, min_max))
    removing_semi_colon = item.replace(':', '')
    final_list = removing_semi_colon.split()
    final_list.pop(0)
    final_list.append(min_max_int[0])
    final_list.append(min_max_int[1])
    master_list.append(final_list)

rep_list = []
pass_count = 0

for item in master_list:
    rep_amount = len(re.findall(item[0], item[1]))
    rep_list.append(rep_amount)
    if rep_amount >= item[2] and rep_amount <= item[3]:
        pass_count += 1

print(pass_count, "passwords are valid per part 1.")
p2_pass_count = 0
p3_pass_count = 0

for item in master_list:
    str1 = item[2] - 1
    str2 = item[3] - 1
    pw_string = str(item[1])
    if pw_string[str1] == item[0]:
        if pw_string[str2] == item[0]:
            continue
        else:
            p2_pass_count += 1
    if pw_string[str2] == item[0]:
        p2_pass_count += 1

print(p2_pass_count, "passwords are valid per part 2.")
