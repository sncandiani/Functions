# for i in range(1, 101):
#     if(i % 5 == 0): 
#         print("Chicken")
#     elif(i % 7== 0):
#         print("Monkey")
#     elif(i % 5 == 0 & i % 7 == 0): 
#         print("ChickenMonkey")
#     else: 
#         print(i)

# Define four Python functions named run, swing, slide, and hide_and_seek.
# Each function should take varying number of children's names as the argument.

def run(*kids):
    for kid in kids: 
        print(f"{kid} ran like a fool") 

def swing(*kids): 
    for kid in kids: 
        print(f"{kid} was swinging like crazy!" )

def slides(*kids): 
    for kid in kids: 
        print(f"{kid} slid away into the ocean...")

def hide_and_seek(*kids): 
    for kid in kids: 
        print(f"{kid} is hiding and nowhere to be found!")

run("Pam", "Sam", "Andrea", "Will")

swing("Marybeth", "Ariel", "Kevin", "Courtney")

slides("Mike", "Jack", "Jennifer", "Earl")

hide_and_seek("Henry", "Heather", "Hayley", "Hugh")