inputName =input("Enter the namer want to validate")
if len(inputName) < 3:
    print("name should be 3 char long")
elif len(inputName) > 10:
    print("name not loger than 10 char")
else:
    print("name sounds good")

print(f"end of validation[{inputName}] ")

