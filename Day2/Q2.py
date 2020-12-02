valid = 0
with open('Input.txt') as file:
    line = file.readline()
    while line:
        # Identify line segments
        segments = line.split(" ")

        # Determine expected char location
        first_pos, second_pos = segments[0].split("-")

        # Determine valid char
        char = segments[1].split(":")[0]

        # Determine if valid password using exclusive or to ensure that if both positions match, the if doesnt execute
        if (segments[2][int(first_pos)-1] == char) ^ (segments[2][int(second_pos)-1] == char):
            valid += 1

        line = file.readline()

print(valid)
