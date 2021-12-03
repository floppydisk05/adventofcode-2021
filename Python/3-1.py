input = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
gammaRate = []
epsilonRate = []
ones = 0
zeroes = 0

def BinToDec(binNum):
    decimal = 0
    binNum = str(binNum)
    for digit in binNum:
        decimal = decimal*2 + int(digit)
    return decimal

for x in range(len(input[0])):
    zeroes = 0
    ones = 0
    for i in range(len(input)):
        if input[i][x] == "0":
            zeroes += 1
        else:
            ones += 1
    if ones > zeroes:
        gammaRate.append("1")
        epsilonRate.append("0")
    else:
        gammaRate.append("0")
        epsilonRate.append("1")
     
gammaRate = BinToDec(int(''.join(gammaRate)))
epsilonRate = BinToDec(int(''.join(epsilonRate)))
answer = gammaRate * epsilonRate
print(answer)

