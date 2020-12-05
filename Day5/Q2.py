with open('Input.txt') as file:
    def to_id(x):
        return (int(x[:7], 2)*8) + int(x[7:10], 2)

    # Convert file into a list of seat IDs
    seatids = [to_id(line.strip().replace("F", "0").replace(
        "B", "1").replace("L", "0").replace("R", "1")) for line in file.readlines()]

    # Create a range from the min to max value of present seat ids
    # Check which id in the range does not exist in the seat ids list
    print([x for x in range(min(seatids), max(seatids)+1)
           if x not in seatids])
