def count(name):
  n=len(name)
  vowel=0
  const=0
  name.lower()
  for i in range (n):
    if(name[i].lower()=='a' or name[i].lower()=='e' or name[i].lower()=='i' or name[i].lower()=='o' or name[i].lower()=='u'   ):
      vowel=vowel+1
    elif(name[i]==' ' or name[i]=='.' or name[i]==','):
      continue
    else :
      const=const+1
  print("Vowel ",vowel," Consonants",const)
name=input("Enter the String")
count(name)



def even(l1):
  l2=[]
  n=len(l1)
  for i in range (n):
    if(l1[i]%2==0):
      l2.append(l1[i])
  return l2
n=int(input("Enetr the numbers"))
l1=[]
for i in range (n):
  ele=int(input("Enter element"))
  l1.append(ele)
even(l1)



def long(l1):
  n=len(l1)
  max=0
  k=0
  for i in range (n):
    if(max<len(l1[i])):
      max=len(l1[i])
      k=i
    elif(max==len(l1[i])):
      continue
  return l1[k]
n=int(input("Enter the lenght"))
l1=[]
for i in range(n):
  ele=input("Enter the Strings")
  l1.append(ele)

print(long(l1))

#Leetcode
class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        n = len(nums)
        return nums[n//2]

    class Solution(object):
        def canConstruct(self, ransomNote, magazine):
            m = list(magazine)
            for i in ransomNote:
                if i in m:
                    m.remove(i)
                else:
                    return False
            return True

        class Solution(object):
            def firstUniqChar(self, s):
                count = [0] * 26
                n = len(s)
                for i in range(n):
                    ch = s[i]
                    k = ord(ch) - ord('a')
                    count[k] += 1
                for i in range(n):
                    ch = s[i]
                    k = ord(ch) - ord('a')
                    if count[k] == 1:
                        return i
                return -1