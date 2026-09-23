filename = 'input.txt'

ranges = []
items = []

with open(filename, 'r') as f:
    content = f.read()
    parts = content.split("\n\n", 1)

    ranges = parts[0].splitlines()
    items = parts[1].splitlines()

def between(item: str, line: str):
    nums = line.split("-")
    low, high = int(nums[0]), int(nums[1])
    if int(item) >= low and int(item) <= high:
        return True
    return False

def check_freshness(item: str):
    for range in ranges:
        if between(item.strip(), range.strip()):
            return True
    return False

sum_fresh: int = 0

for item in items:
    if check_freshness(item):
        sum_fresh += 1

print(sum_fresh)

# part 2
good_ranges = []
ranges = [tuple(map(int, r.split("-"))) for r in ranges]
ranges.sort(key=lambda rng: rng[0])

i = 0
j = 1

while j < len(ranges):
    if ranges[i][1] >= ranges[j][0]:
        ranges[i] = (ranges[i][0], max(ranges[i][1], ranges[j][1]))
        j += 1
    else:
        good_ranges.append(ranges[i])
        i = j
        j += 1

good_ranges.append(ranges[i])

print(len(good_ranges))

dumb_sum = 0
for rng in good_ranges:
    dumb_sum += rng[1] - rng[0] + 1


print(dumb_sum)