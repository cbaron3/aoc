from collections import defaultdict
import time


tracked = defaultdict(int)
count = 0
group_size = 0
mult = 100

# Add additional new line to EOF so I dont need to check the last groups tracked answers outside for loop
with open('Input.txt', 'a') as file:
    file.write("\n\n")

start_time = time.time()

with open('Input.txt') as file:
    lines = []
    for line in file:
        # When we encounter a new line, update the count of the current groups answers and reset in prep for counting next groups answers
        if line == '\n':
            ll = len(lines)
            for c in ''.join(lines):
                # if c != '\n':
                tracked[c] += 1

                if tracked[c] == ll:
                    count += 1

            # Reset group size and tracked customs answers
            lines = []
            tracked = defaultdict(int)
        else:
            # Another set of answers therefore increment group size
            lines += [line[:-1]*mult]
            group_size += 1*mult

print(count)
print(time.time() - start_time)
