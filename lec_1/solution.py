#write your answer here
#Yug Savla
1. LeetCode Solution
class Solution(object):
    def twoSum(self, nums, target):
        n=len(nums)
        for i in range(0, n):
            for j in range(i+1, n):
                if(nums[i]+nums[j]==target):
                    return [i,j]
        return []
2.  Printing 1 2 4 8 other than variable addition
a = 1
for i in range(4):
    print(a)
    a = a << 1
