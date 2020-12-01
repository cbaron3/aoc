# Find the two entries that sum to 2020
# Solution to the problem is those two values multiplied together

# Since a+b = 2020, check if 2020-b exists in set. If not, add b to set
tracked = set()
with open('Input.txt') as file:
    line = file.readline()
    while line:
        # Do stuff with line
        if 2020 - int(line) in tracked:
            print((2020 - int(line))*int(line))
        else:
            tracked.add(int(line))
        line = file.readline()
