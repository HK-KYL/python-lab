
#Lab 4
#%%
# # Exercise 1
def longestWord(s):
    storage = s.split(" ")
    longest = storage[0]
    for i in range(len(storage)):
        if len(storage[i]) &gt; len(longest):
            longest = storage[i]
    
    return longest

longestWord("Hello World Computer Science is fun")
#%%
#Exercise 2
def caesarEncrypt(s, step):
    result = ""
    for i in range(len(s)):
        if s[i].islower():
            result += chr((ord(s[i]) - ord('a') + step) % 26 + ord('a'))
        elif s[i].isupper():
            result += chr((ord(s[i]) - ord('A') + step) % 26 + ord('A'))
        else:
            result += s[i]
    return result

caesarEncrypt("Hello World!", 3)

#%%
#Exercise 3
def copy(x, y):
    file1 = open(x, "r")
    lines = file1.readlines()
    file1.close
    file2 = open(y, "x")
    for s in lines:
        file2.write(s)
    file2.close()
    
copy("demo.txt","newFile.txt")