for i in range(1, 101):
    if(i % 5 == 0): 
        print("Chicken")
    elif(i % 7== 0):
        print("Monkey")
    elif(i % 5 == 0 & i % 7 == 0): 
        print("ChickenMonkey")
    else: 
        print(i)