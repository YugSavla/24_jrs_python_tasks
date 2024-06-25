#write your answer here
#Yug Savla
q1# take an input from user is should be a number and find out how many digit it has
num=int(input("Enter a number"))
num1=num
if(num<0):
    num=-num
i=0
while(num>0):
    num=num//10
    i=i+1
if(num1==0):
    print("No. of digits are", 1)
else :
    print("No. of digits are", i)
q2# take an input from the user the factorial of a number if the user enters a string print not a valid input
fac=input("Enter a number for factorial")
if(fac.isalpha()==True):
    print("Invalid Input ")
else :
    fac = int(fac)
    if (fac < 0):
        print("Wrong number")
    else:
        i = 1
        while(fac>=1):
            i=fac*i
            fac=fac-1
        print("Value of the factorial is",i)
q3# create a program

Computers ={
  "Laptop1" : {"brand" : "DELL","OS" : "Windows"},
  "Laptop2" : {"brand" : "HP", "OS" : "Linux"},
  "Desktop" : {"brand" : "Apple","OS" : "Mac-OS"}
}
# from this above data create a list brand,OS
Computers ={
  "Laptop1" : {"brand" : "DELL","OS" : "Windows"},
  "Laptop2" : {"brand" : "HP", "OS" : "Linux"},
  "Desktop" : {"brand" : "Apple","OS" : "Mac-OS"}
}
#First Way
#brand=[]
#brand.append(Computers["Laptop1"]["brand"])
#brand.append(Computers["Laptop2"]["brand"])
#brand.append(Computers["Desktop"]["brand"])
#print(brand)

#Second Way

#OS=[Computers["Laptop1"]["OS"],Computers["Laptop2"]["OS"],Computers["Desktop"]["OS"]]
#print(OS)

#3rd Way
#brand=[]
#OS=[]
#for laptop, key in Computers.items():
#   brand.append(key["brand"])
#   OS.append(key["OS"])
#print(brand)
#print(OS)

#Q4 Leetcode add 2
class Solution(object):
    def twoSum(self, nums, target):
        n=len(nums)
        for i in range(0, n):
            for j in range(i+1, n):
                if(nums[i]+nums[j]==target):
                    return [i,j]
        return []
#Q5  Printing 1 2 4 8 other than variable addition
a = 1
for i in range(4):
    print(a)
    a = a << 1
