numbers=[5,2,5,2,2]
j=0
for i in numbers:
    output=''
    for j in range(i):
        output=output.__add__('X')
    print(output)

