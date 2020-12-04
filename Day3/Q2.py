x_pos = 0
path_tree_cnt = 0
total_trees = 1
with open('Input.txt') as file:
    lines = file.readlines()
    for right, down in [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]:
        # Count DOWN steps per loop iteration
        for line_num in range(down, len(lines), down):

            # Determine line index. Include rollover using modulo incase x exceeds line length
            x_pos += right
            ind = x_pos % len(lines[line_num].strip())

            # Check if tree
            if lines[line_num][ind] == '#':
                path_tree_cnt += 1

        # Accumulate trees and reset counters for next path
        total_trees *= path_tree_cnt
        path_tree_cnt = 0
        x_pos = 0

print(total_trees)
