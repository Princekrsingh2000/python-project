def syemmetry(str):
    n=len(str)
    flag=0
    if n%2:
        mid=n//2+1
        
    else:
        mid=n//2
    
    start=0
    start1=mid
    
    while start<mid and start1<n:
        if str[start] == str[start1]:

            start+=1
            start1+=1
        else:
            flag=1
            break
    if flag == 0:
        return "yes symmetrical"
    else:
        return "not"

str="khokho"
print(syemmetry(str))
str="khokho"
for i in range(len(str)):
    if i%2:
        #print(i)
        mid= i//2+1
    else:
        mid=i//2
print(mid)
