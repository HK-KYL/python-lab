#A3
#%%
#Question 1

def countNumber(s):
    result = {}
    for c in s.lower():
        if c not in result:
            result[c] = 1
        else:
            result[c] += 1
    return result

#Test case
print(countNumber("Google.com"))
print(countNumber("Yahoo.com"))

#%%
#Question 2
import string
def alphabetCheck(s):
    s = s.lower()
    for c in string.ascii_lowercase:
        if c not in s:
            return False
    return True

#Test case
print(alphabetCheck("The quick brown fox jumps over the lazy cat"))
print(alphabetCheck("The quick brown fox jumps over the lazy dog"))

#%%
#Question 3
def removeDuplicate(s):
    result = ""
    for c in s:
        if c.lower() not in result.lower():
            result += c
    return result

# Test case
print(removeDuplicate("Google"))
print(removeDuplicate("Hello"))

#%%
#Question 4
def convertLower(str, n):
    result = str[0:n].lower() + str[n:]
    return result

#Test case
print(convertLower("UNITED STATES", 5))
print(convertLower("UNITED STATES", 8))

#%%
#Question 5
def countVowels(s):
    vowels = "aeiou"
    count = 0
    for c in s:
        if c.lower() in vowels:
            count += 1
    return count

#Test case
print(countVowels("Internet"))
print(countVowels("AEIOU"))

#%%
#Question 6
import numpy as np
even = np.arange(100, 200 + 1, 2)
print(even)
print(len(even))

#%%
#Question 7
import numpy as np
one = np.ones(100, int)
five = np.full(100, 5, int)
ten = np.full(100, 10, int)
result = np.concatenate((one, five, ten))
print(result)

#%%
#Question 8
import numpy as np

def addVector(matrix, vector):
    return matrix + vector
   
givenMatrix = np.array([8, 9, 10, 5, 6, 7], int).reshape(2,3)
vector = np.array([2, 3, 4])

#Test case
print(addVector(givenMatrix, vector))

#%%
#Question 9
import numpy as np

def convertTemperature(centigrade):
    return centigrade * 9 / 5 + 32

#Test case
cen = np.array([19.4, 22.0, 55.2, 99.8])
print("Centigrade: " ,cen)
print("Fahrenheit: ", convertTemperature(cen))

#%%
#Question 10
import numpy as np

result = []
sumArray = np.zeros((100,100))
for i in range(10):
    result.append(np.random.randn(100, 100))
    sumArray += result[i]
    print("Array " , i + 1)
    print(result[i])
    print("Min: ", result[i].min())
    print("Max: ", result[i].max())
    print("Mean: ", result[i].mean())
    print("Standard Deviation: ", result[i].std())
    

print("Sum array")
print(sumArray)
print("Min: ", sumArray.min())
print("Max: ", sumArray.max())
print("Mean: ", sumArray.mean())
print("Standard Deviation: ", sumArray.std())
                
    