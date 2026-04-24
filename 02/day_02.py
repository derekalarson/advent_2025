# Return sum of invalid id's from input.txt
id_sum: int = 0
filename = "input.txt"

with open(filename, 'r') as file:
    for line in file:
        ranges = line.split(',')
        for ea in ranges:
            nums = ea.strip().split('-')
            for num in range(int(nums[0]), int(nums[1])+1):
                num = str(num)
                length = len(num)
                if length % 2 == 0:
                    if num[:length//2] == num[length//2:]:
                        id_sum += int(num)
                        continue

                for i in range(1, length // 2 + 1):
                    if length % i == 0:
                        substring = num[:i]
                        if substring * (length // i) == num:
                            id_sum += int(num)


print(id_sum)