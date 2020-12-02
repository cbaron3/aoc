valid = 0
with open('Input.txt') as file:
    line = file.readline()
    while line:
        # Identify line segments
        segments = line.split(" ")

        # Determine min/max
        min_cnt, max_cnt = segments[0].split("-")

        # Determine valid char
        char = segments[1].split(":")[0]

        # Determine if valid password
        char_count = segments[2].count(char)

        if char_count >= int(min_cnt) and char_count <= int(max_cnt):
            valid += 1

        line = file.readline()

print(valid)
