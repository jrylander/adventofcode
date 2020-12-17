from itertools import islice

with open("indata-dec01.txt") as indata:
    lines = list(indata)
    numbers = [int(i) for i in lines]

    for firstIdx, firstNumber in enumerate(numbers):
        for secondIdx, secondNumber in enumerate(islice(numbers, firstIdx+1)):
            for thirdIdx, thirdNumber in enumerate(islice(numbers, secondIdx+1)):
                sumOfTheNumbers = firstNumber + secondNumber + thirdNumber
                if (sumOfTheNumbers == 2020):
                    print(f"{firstNumber}, {secondNumber} and {thirdNumber} equals {firstNumber * secondNumber * thirdNumber}")
