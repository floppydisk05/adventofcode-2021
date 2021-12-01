values = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
increases = 0
for i in range(len(values)):
    if (i != 0) and (values[i] > values[i-1]):
        increases += 1

print(increases)