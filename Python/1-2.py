values = [607, 618, 618, 617, 647, 716, 769, 792]
increases = 0

increases = 0
for i in range(3, len(values)):
    if (values[i] > values[i - 3]):
        increases += 1

print(increases)