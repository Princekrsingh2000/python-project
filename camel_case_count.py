class Solution:
    def countCamelCase (self,s):
        # your code here
        count=0
        for i in s:
            if i>='A' and i<='Z':
                count+=1
        
        return count

str=Solution()
s= "ckjkUUYII"
#str.countCamelCase(s)
print(str.countCamelCase(s))