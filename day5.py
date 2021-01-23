l=[1, 2, 7, 4, 5, 6, 0, 3]
def func1(l,n):
    count=0
    for i in l:
        index=l.index(i)+1
        for x in range(index,len(l)):
            if i+l.index(x)==n:
                count+=1
    return count

l=[1, 2, 7, 4, 5, 6, 0, 3]
n=6
print(func1(l,n))


def find_pairs_of_numbers(l,n):
    count=0
    for i in range(len(l)):
        for j in range(i,len(l)):

            if(j<0 and i<0):
                continue
            if(l[i]==l[j]):
                continue
            if l[i]+l[j]==n:
                count+=1

    if count==0:
        return 0
    return count
l=[1, 2, 7, 4, 5, 6, 0, 3]
n=6
print(find_pairs_of_numbers(l,n))


# def find_pairs(lst, key):
#     count = 0
#     if sum(lst[count:count+1]) == key:
#         count += 1
#         return count
#     else:
#         return find_pairs(lst[1:],key)

# find_pairs(list(range(1, 100, 2)), 55) #0
# find_pairs(list(range(1, 100, 2)), 56)

# list_of_marks = (12,18,25,24,2,5,18,20,20,21)
# marks=0
# for x in list_of_marks:
#     marks+=x
# print(marks)
# l=[]
# for i in list_of_marks:
#     if i==20:
#         l.append(l.count(i))
# print(l)
def find_more_than_average(list_of_marks):
    marks=0
    count=0
    for i in list_of_marks:
        marks+=i
    average=marks/len(list_of_marks)
    for x in list_of_marks:
        if x>average:
            count+=1
    percentage=(count*100)/len(list_of_marks)
    return percentage
def sort_marks(list_of_marks):
    list_of_marks=sorted(list_of_marks)
    return list_of_marks

def generate_frequency(list_of_marks):
    frequency=[]
    for x in range(26):
        count=0
        for y in list_of_marks:
            if x==y:
                count+=1
        frequency.append(count)
    return frequency
list_of_marks = (12,18,25,24,2,5,18,20,20,21)
print(find_more_than_average(list_of_marks))
print(generate_frequency(list_of_marks)) #[0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 2, 1, 0, 0, 1, 1]
print(sort_marks(list_of_marks))

# for x in range(26):
#     print(x)

# l=[23,34,55]
# s=str(l)
# print(s[12])
# print(s[0]+s[1])
# print(type(s))

# print(s)

def find_largest(l):
    num=""
    l=sorted(l)
    for x in range(len(l)-1,-1,-1):
        num+=str(l[x])
    return num

l=[23,34,55]
print(find_largest(l))

def check_double_number(number):
    num1=str(number*2)
    number=str(number)
    count=0
    for x in number:
        if x in num1:
            count+=1
        else:
            return False
    if count==len(number):
        return True
number=125874
print(check_double_number(number))
