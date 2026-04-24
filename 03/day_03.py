filename = 'input.txt'
jolt_sum: int = 0


# Scan left to right for a 9, 9 wins
# if 9 is in pos line[-1] (last), start over
# once best 10^1 slot is found, find best 10^0 slot right of index pos


def find_best_ten(slice):
    # first char is highest obviously
    high_char = slice[0]
    high_pos = 0
    for i in range(1, len(slice)-1):
        if int(slice[i]) > int(high_char):
            high_char = slice[i]
            high_pos = i
            if high_char == '9':
                return high_pos
    return high_pos

def find_best_one(slice):
    high_char = slice[0]
    high_pos = 0
    if len(slice) == 1:
        return high_pos
    for i in range(1, len(slice)):
        if int(slice[i]) > int(high_char):
            high_char = slice[i]
            high_pos = i
            if high_char == '9':
                return high_pos
    return high_pos


with open(filename, 'r') as file:
    for line in file:
        line = line.strip()
        tens = find_best_ten(line)
        ones = find_best_one(line[tens+1:]) #go right from the best ten
        # print(line)
        # print(f"{line[tens]}, {line[tens+1+ones]}")
        jolt_sum += int(line[tens])*10 + int(line[tens+1+ones])

print("Part1 solution: ", jolt_sum)

def find_digits(line, stop):
    if stop < 0: return ""
    high_ = line[0]
    high_pos = 0
    for i in range(1, len(line)-stop):
        if int(line[i]) > int(high_):
            high_ = line[i]
            high_pos = i
    # print(line)
    return high_ + find_digits(line[high_pos+1:], stop-1)
        


with open(filename, 'r') as file:
    joltage:int = 0
    for line in file:
        line = line.strip()
        battery = int(find_digits(line, 11))
        # print(battery)
        joltage += battery
        # break
    print("Part2 solution: ", joltage)

# too high: 172134777040773
#           1735134777039210
#           173513477703921
#           171518260283767