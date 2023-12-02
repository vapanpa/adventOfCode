#part 1

infile = open("day1_input.txt", "r")

runningSum = 0

for line in infile:
    currentNumber = ""
    newLine = [x for x in line]
    print(newLine)
    for i in newLine:
        if i.isnumeric():
            currentNumber = currentNumber + i
    print(currentNumber, "length: " + f"{len(currentNumber)}")
    if len(currentNumber) > 2:
        currentNumber = currentNumber[0] + currentNumber[-1]
    elif len(currentNumber) == 1:
        currentNumber = currentNumber[0] + currentNumber[0]
    elif len(currentNumber) == 2:
        currentNumber = currentNumber[0] + currentNumber[1]
    else:
        currentNumber = 0
    print("final digit from line: " + f'{currentNumber}')
    currentNumber = int(currentNumber)

    runningSum = runningSum + currentNumber
    print("running sum: " + f'{runningSum}')

print(runningSum)

#part 2