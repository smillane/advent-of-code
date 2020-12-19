import math


with open("input.txt", "r") as input_file:
    read_file = [line.strip() for line in input_file]

print(read_file)

seatID_list = []

for input_string in read_file:
    front = 0
    back = 127
    left = 0
    right = 7
    for char in input_string:
        if char == 'F':
            front = front
            back = math.floor(back - ((back - front) / 2))
            front_back_value = front

        if char == 'B':
            front = math.ceil(back - ((back - front) / 2))
            back = back
            front_back_value = back

        if char == 'L':
            left = left
            right = math.floor(right - ((right - left) / 2))
            left_right_value = left

        if char == 'R':
            left = math.ceil(right - ((right - left) / 2))
            right = right
            left_right_value = right


    seatID = front_back_value * 8 + left_right_value
    seatID_list.append(seatID)

seatID_list.sort()
print("Your seat ID is", [seat for seat in range(seatID_list[0], seatID_list[-1] + 1) if seat not in seatID_list])
print()
print("Max seat ID is", max(seatID_list))
