#main.py

#this is our entry point to the test code
#we will test the solution class
#for LeetCode problem 415
#the solution has been provided by ...

#instantiate an object of type Solution
from solutionPackage.Solution import *

mySolution = Solution()
'''
result = mySolution.addStrings("123", "456")    
print(result)#we expect 123+456=579
#do a test that will fail
result1 = mySolution.addStrings("aaa", "bbb")    
print(result1)#we expect to fail 
result2 = mySolution.addStrings("-123", "456")    
print(result2)#we expect -123+456=333
result3 = mySolution.addStrings("123.5", "456.1")    
print(result3)#we expect 123.5+456.1=579.6
result4 = mySolution.addStrings("123a", "456b")    
print(result4)#do not know what to expect 
result5 = mySolution.addStrings("123!", "456@")    
print(result5)#we expect 123+456=579
'''

#lets build a list of test cases and expected results
num1=["123", "999", "1000"]
num2=["456", "111", "2000"]
expectedResult=[579, 1110, 3000]

#write a loop to try all the test cases
for i in range(0,3):
    result=mySolution.addStrings(num1[i], num2[i])
    if int(result)==expectedResult[i]:
        print("test passed")
    else:
        print("test FAILED. Change Professions")
        print("expected result", expectedResult[i], "actual result", result)