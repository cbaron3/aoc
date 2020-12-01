# Same as Q2 but with three elements instead of two
# A lot trickier, can use three pointer technique
# Need sorted list
# First pointer is at i, index of iterating the list
# Second pointer is i+1, the left pointer
# Third pointer is at the end of the list, the right pointer
# If the sum is to large, decrement the right pointer
# If the sum is to small, incremene the left pointer
# If the left pointer passes the right pointer, increment i and restart the process
with open('Input.txt') as file:
    lines = [int(line.strip()) for line in file]

lines.sort()

for i in range(0, len(lines)-2):
    left = i + 1
    right = len(lines) - 1

    while left < right:
        if(lines[i] + lines[left] + lines[right] > 2020):
            right -= 1
        elif (lines[i] + lines[left] + lines[right] < 2020):
            left += 1
        else:
            print(lines[i]*lines[left]*lines[right])
            break
