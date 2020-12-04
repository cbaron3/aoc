x_pos = 0
total_trees = 0
with open('Input.txt') as file:
    lines = file.readlines()
    # Start at 1 because you need to check tree AFTER going down
    for line_num in range(1, len(lines)):

        # Determine line index. Include rollover using modulo incase x exceeds line length
        x_pos += 3
        ind = x_pos % len(lines[line_num].strip())

        # Check tree
        if lines[line_num][ind] == '#':
            total_trees += 1

print(total_trees)
