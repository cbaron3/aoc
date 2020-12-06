from collections import defaultdict

tracked = defaultdict(int)
count = 0
group_size = 0

# Add additional new line to EOF so I dont need to check the last groups tracked answers outside for loop
with open('Input.txt', 'a') as file:
    file.write("\n\n")

with open('Input.txt') as file:
    for line in file:
        # When we encounter a new line, update the count of the current groups answers and reset in prep for counting next groups answers
        if line == '\n':
            keys = tracked.keys()

            # Check to see how many keys in the dict have a value == group_size
            for key in keys:
                if tracked[key] == group_size:
                    count += 1
            
            # Reset group size and tracked customs answers
            group_size = 0
            tracked = defaultdict(int)
        else:
            # Another set of answers therefore increment group size
            group_size += 1

            # Use default dict to track frequeny of answer
            customs = line.strip()
            for answer in customs:
                tracked[answer] += 1

print(count)
