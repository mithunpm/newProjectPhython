def findMaxFromList(numberList):
    print(numberList)
    maximum=0
    for number in numberList:
        if number > maximum:
            maximum=number
    print(f"maximum number is {maximum}")
    return maximum