carStarus=False
while True:
    inputIst = input('please eter the option');
    if inputIst.upper() == "Start".upper():
        if carStarus:
            print("car started already")
        else:
            carStarus = True;
            print("car started")
    elif inputIst.upper() == "stop".upper():
        if(carStarus):
            carStarus=False;
            print("car stoped ")
        else:
            print("car already stoped")
    elif inputIst.upper() == "help".upper():
        print("""
start -- to start car
stop --- to stop car
quit --- to quit from menu
         
         """ )
    elif inputIst.upper() == "quit".upper():
        print("quit from menu")
        break
    else:
        print("i dont under stand the function")
        break
