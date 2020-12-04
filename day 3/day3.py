with open("input.txt", "r") as input_file:
    read_file = [line.strip() for line in input_file]

file2 = read_file
tree_count_skip = 0
column_count_skip = 0
row_counter = 1
width = (len(read_file[0])) - 1

for item2 in file2:
    if row_counter % 2 != 0:
        row_counter += 1
        if item2[column_count_skip] == '#':
            tree_count_skip += 1
            column_count_skip += 1
            if column_count_skip > width:
                column_count_skip = 0
        else:
            column_count_skip += 1
            if column_count_skip > width:
                column_count_skip = 0
    else:
        row_counter += 1

read_file.pop(0)
tree_count = 0
tree_count_array = []
column_count = [1, 3, 5, 7]

for right in column_count:
    perm_right = right
    tree_count = 0
    for item in read_file:
        if item[right] == '#':
            tree_count += 1
            if width == right:
                right = perm_right - 1
            else:
                right += perm_right
                if width < right:
                    right = (right % width) - 1
        else:
            if width == right:
                right = perm_right - 1
            else:
                right += perm_right
                if width < right:
                    right = (right % width) - 1
    tree_count_array.append(tree_count)

print(tree_count_skip)
print(tree_count_array)
