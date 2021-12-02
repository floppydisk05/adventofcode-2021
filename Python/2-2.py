input = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']
hpos = 0
depth = 0
aim = 0
for i in range(len(input)):
    direction = input[i].split()[0]
    distance = int(input[i].split()[1])
    if direction == 'up':
        aim -= distance
    elif direction == 'down':
        aim += distance
    elif direction == 'forward':
        hpos += distance
        depth += (aim * distance)
solution = hpos * depth
print(solution)
