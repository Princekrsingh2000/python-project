str="gfg gfg gfg"
d={}
str1=str.split(" ")
for i in str1:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1

print(d)

    
# str="gfg is a best"

# for i in str.split():
#     res=(i,str.count(i))

# print(res)

