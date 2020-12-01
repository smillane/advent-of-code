import itertools


find_sum = 2020

with open("input.txt", "r") as input_file:
    input_list = [int(line) for line in input_file if line.strip()]

print(input_list)

for numbers in itertools.combinations(input_list, 2):
    if sum(numbers) == find_sum:
        print([input_list.index(number) for number in numbers])


#print(input_list)

