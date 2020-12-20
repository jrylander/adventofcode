from itertools import islice

with open("dec01-indata.txt") as indata:
    lines = list(indata)
    numbers = [int(i) for i in lines]

    for firstIdx, firstNumber in enumerate(numbers):
        for secondIdx, secondNumber in enumerate(islice(numbers, firstIdx+1)):
            sumOfTheNumbers = firstNumber + secondNumber
            if (sumOfTheNumbers == 2020):
                print(f"{firstNumber} at {firstNumber} and {secondNumber} at {secondIdx} equals {firstNumber * secondNumber}")
