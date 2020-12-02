import itertools
from functools import reduce


find_sum = 2020

with open("input.txt", "r") as input_file:
    input_list = [int(line) for line in input_file if line.strip()]

print(input_list)

for numbers in itertools.combinations(input_list, 2):
    if sum(numbers) == find_sum:
        number_position = ([input_list.index(number) for number in numbers])

number_sum = input_list[number_position[0]] * input_list[number_position[1]]

for numbers in itertools.combinations(input_list, 3):
    if sum(numbers) == find_sum:
        number_position_part2 = ([input_list.index(number) for number in numbers])

number_sum_part2 = input_list[number_position_part2[0]] * input_list[number_position_part2[1]] * input_list[number_position_part2[2]]

print(input_list[number_position[0]])
print(input_list[number_position[1]])
print(number_sum)

print(input_list[number_position_part2[0]])
print(input_list[number_position_part2[1]])
print(input_list[number_position_part2[2]])
print(number_sum_part2)
