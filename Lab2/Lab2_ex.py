#Lab 2
#%%
#Exercise 1 - Greeting
print("Computer: Hi!")
while True:
    userInput = input("You: ")
    if userInput == "How are you?":
        print("Computer: Fine, and you?")
    elif userInput == "How do you do.":
        print("Computer: How do you do.")
    elif userInput == "Good to see you.":
        print("Computer: Me too.")
    elif userInput == "Bye.":
        print("Computer: Bye!")
        break
    else:
        print("Computer: ...")
        
#%%
#Exercise 2 - Summation
result = 0
while True:
    n = input("Input an integer: ")
    
    if n.isdigit() == False:
        break
    
    result += int(n)

print(result)

#%%
#Exercise 3 - Maximun Value
maximun = 0
for i in range(5):
    n = input("Input a number: ")
    n = int(n)
    if n &gt; maximun:
        maximun = n

print("Maximun is ", maximun)