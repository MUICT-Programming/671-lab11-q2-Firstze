one=[]
two=[]
n=int(input())

for i in range(n):
    lista = int(input())
    one.append(lista)

for i in range(n):
    listb = int(input())
    two.append(listb)

def summation(one,two):
    three=[]
    for i in range(len(one)):
        add = one[i]+two[i]
        three.append(add)
    return three
list_add = summation(one,two)

def find_min_max (list):
    max=list[0]
    min=list[0]
    for i in list:
        if i > max:
            max=i
    
    for i in list:
        if i < min:
            min=i

    min_max=(min,max)
    return min_max
print(summation(one,two))
print(find_min_max (list_add))
