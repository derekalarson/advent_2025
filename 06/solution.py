filename = 'input.txt'

rows = []
sum_tot = 0

with open(filename, 'r') as f:
    content = f.read()
    for line in content.split('\n'):
        rows.append(line.split())


for i in range(len(rows[0])):
    if rows[4][i] == '*':
        sum_tot += int(rows[0][i]) * int(rows[1][i]) * int(rows[2][i]) * int(rows[3][i])
    else:
        sum_tot += int(rows[0][i]) + int(rows[1][i]) + int(rows[2][i]) + int(rows[3][i])

print(sum_tot)

# part 2

sum_tot2 = 0

cols = []

with open(filename, 'r') as f:
    content = f.read()
    rows = content.split('\n')
    print(len(rows[0]))
    for i in range(len(rows[0])):
        col = ""
        for row in rows:
            col = col + row[i]
        cols.append(col)
cols.append('     ')
batch = []
multiply = False

for i in range(len(cols)):
    if cols[i][-1] == '*':
        batch.append(int(cols[i][:-1]))
        multiply = True

    elif cols[i][-1] == '+':
        batch.append(int(cols[i][:-1]))
        multiply = False

    elif cols[i] == '     ':
        if multiply:
            temp_total = 1
            for num in batch:
                temp_total *= num
            sum_tot2 += temp_total
            batch = []
        else:
            temp_total = 0
            for num in batch:
                temp_total += num
            sum_tot2 += temp_total
            batch = []
    else:
        batch.append(int(cols[i]))


print(sum_tot2)

# print(cols[0])
# print(cols[1])
# print(cols[2])
# print(cols[3])