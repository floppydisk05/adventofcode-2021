from collections import Counter

input = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
ox_gen = input
col = 0
while len(ox_gen) > 1:
    out = Counter([line[col] for line in ox_gen])
    if out["1"] >= out["0"]:
        most = "1"
    else:
        most = "0"

    ox_gen = [line for line in ox_gen if line[col] == most]
    col += 1

co2_scrubber = input
col = 0
while len(co2_scrubber) > 1:
    out = Counter([line[col] for line in co2_scrubber])
    if out["1"] < out["0"]:
        least = "1"
    else:
        least = "0"
    co2_scrubber = [line for line in co2_scrubber if line[col] == least]
    col += 1

print(int(ox_gen[0], 2) * int(co2_scrubber[0], 2))