list=[2,5,3,6,3,5,6,3,4];
duplicate=[]
for i in list:
    if i not in duplicate:
        duplicate.append(i)
print(duplicate)