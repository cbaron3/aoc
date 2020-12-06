# Calculate the sum of the yes counts in each group.

tracked = set()
count = 0
with open('Input.txt') as file:
    for line in file:
        if line == '\n':
            # Accumulate count for group and reset tracked characters for next group
            count += len(tracked)
            tracked = set()
        else:
            # Use set to track only unique answers
            customs = line.strip()
            for answer in customs:
                tracked.add(answer)
count += len(tracked)

print(count)
