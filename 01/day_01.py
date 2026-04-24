

# Starting values
dial: int = 50
zeros: int = 0

input = "input.txt"

with open(input, 'r') as file:
    for line in file:
        print(f"Dial: {dial}, Line: {line}")

        # number of clicks
        clicks = int(line[1:])

        #number of times we completely loop
        zeros += (clicks // 100)
        # rightward spin, we add
        if line.startswith('R'):
            newdial = (dial + clicks) % 100
            # if the new position is less than the old position, we know we looped zero
            if newdial < dial and newdial != 0:
                zeros += 1
        
        # leftward spin we subtract
        else:
            newdial = (dial - clicks) % 100
            # if the new position is greater than the old position, we looped zero
            if newdial > dial and dial != 0:
                zeros += 1
        dial = newdial
        if dial == 0:
            zeros += 1
        print(f"Newdial: {dial}, Zeros: {zeros}")
print(zeros)

# higher than 5451