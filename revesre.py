class Solution:
    
    def revStr (ob, S):
        # code here 
        n=len(S)-1
        reverse_str=""
        while n>=0:
            reverse_str+=S[n]
            n-=1
        return reverse_str



ob = Solution()
S='abcdegtf'
print(ob.revStr(S))