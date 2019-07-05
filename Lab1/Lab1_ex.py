#Lab 1A
#%%
#Trial-and-Error Exercise 1.1
def hello():
    print("Hello, Python!")
hello
hello()

#%%
#Trial-and-Error Exercise 1.2
def hello():
    print("Hello, Python!")
   print("again")
hello
hello()

#%%
#Trial-and-Error Exercise 1.3
def inputName():
    name = input("What's your name?")
    print("name")
    
inputName()

#%%
#Trial-and-Error Exercise 2.1
type(true)

#%%
#Trial-and-Error Exercise 2.2
tuple_item = (0, "string", 3.14, False)
type(tuple_item)
print(tuple_item)
tuple_student = ("17991234", "CHAN TAI MAN", "Male", "2001-01-01")
print(tuple_student[0])
print(tuple_student[1])
print(tuple_student[2])
print(tuple_student[3])
print(tuple_student[4])

#%%
#Trial-and-Error Exercise 2.3
list_item = [0, "string", 3.14, False]
type(list_item)
print(list_item)
list_student = ["17991234", "CHAN TAI MAN", "Male", "2001-01-01"]
print(list_student)
print(list_student[0])
print(list_student[1])
print(list_student[2])
print(list_student[3])
list_student[3] = "2001-12-31"
print(list_student[3])
print(list_student) 

tuple_student[3] = "2001-12-31"

#Lab 1B
#%%
#Example 3.1
tuple1 = 1, 3, 5, 7
print(tuple1)
tuple2 = (1, 3, 5, 7)
print(tuple2)
#Are tuple1 and tuple2 the same? “==” is a comparison operator
print(tuple1 == tuple2)
tuple3 = ("Jack", "John", "Alice")
print(tuple3)
tuple4 = (1, "Jack", 2, "John")
print(tuple4)

#%%
#Example 3.2
print(tuple4[0])
print(tuple4[1])
print(tuple4[2])
print(tuple4[3])
print(tuple4[-1]) 
print(tuple4[-2])
print(tuple4[-3])
print(tuple4[-4])

#%%
#Example 3.3
list1 = [1, 3, 5, 7]
print(list1)
list2 = ["Jack", "John", "Alice"]
print(list2)
list3 = [1, "Jack", 2, "John"]
print(list3)
#Generate a list from a range
my_range = range(10, 20, 2)
print(my_range)
list4 = list(my_range)
print(list4)
#Generate a list from a tuple
tuple1 = ("John", "Alice", "Jack")
list5 = list(tuple1)
print(list5)
#Is list5 equal to tuple1?
print(list5 == tuple1)

#%%
#Example 3.4
list6 = ["Jack", "John", "Alice"]
print(list6)
print(list6[0])
print(list6[‐1])
print(len(list6))
list6.append("Jack")
print(list6)
list6.insert(2, "Jack")
print(list6)
list6.remove("Jack")
print(list6)
list6.sort()
print(list6)
list6.reverse()
print(list6)

#%%
#Example 3.5
a = list(range(10))  
print(a)
b = a[2:6]
print(b)
c = a[:5]
print(c)
d = a[5:]
print(d)
e = a[3:10:2]
print(e)

#%%
#Example 3.6
family = {"Jack":35, "Linda":32, "Alice":6}
print(family)
print(len(family))
family["David"] = 68
print(family)
print(len(family))
family["Alice"] = 7
print(family)
family.pop("David")
print(family)
stu = {"17212345":["CHAN DAI MAN", "2000‐01‐01", "Male"],
       "17216789":["WONG Maggie", "2000‐06‐21", "Female"]}
print(stu["17212345"])
#stu["17212345"] is a list. So what is stu["17212345"][0]?
print(stu["17212345"][0])
print(stu["17216789"])
#stu["17216789"] is a list. So what is stu["17216789"][2]?
print(stu["17216789"][2])
#add the Address information into the dictionary
stu["17212345"].append("KOWLOON TONG")
print(stu["17212345"])
stu["17216789"].append("SAI KONG")
print(stu["17216789"])