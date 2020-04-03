inputNumber=input('Enter the input number !')
mapNumber={
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    0 : "😢"
}
stringTemp=""
for int1 in inputNumber:
    tempInt=int(int1)
    stringTemp = stringTemp +" " +mapNumber.get(tempInt)
print(stringTemp)


