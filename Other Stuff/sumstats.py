import numpy as np

people = ['a', 'b', 'c', 'd', 'e']
def getAllPossibleOrderings(people):
    if len(people) == 1:
        return [people]
    else:
        res = []
        for i in range(0, len(people)):
            for j in getAllPossibleOrderings(people[:i] + people[i+1:]):
                res.append([people[i]] + j)
        return res

res = getAllPossibleOrderings(people)
count = 0
for i in res:
    if i[0] == 'a' and i[1] != 'b' and i[2] != 'c':
        count += 1
    elif i[0] != 'a' and i[1] == 'b' and i[2] != 'c':
        count += 1
    elif i[0] != 'a' and i[1] != 'b' and i[2] == 'c':
        count += 1
print(count/len(res))

count = 0
for i in res:
    if (i[0] == 'a' or i[1] == 'a' or i[2] == 'a') and (i[0] != 'b' and i[1] != 'b' and i[2] != 'b'):
        count += 1
    elif (i[0] != 'a' and i[1] != 'a' and i[2] != 'a') and (i[0] == 'b' or i[1] == 'b' or i[2] == 'b'):
        count += 1
        
print(count/len(res))

count = 0
for i in res:
    if i[0] == 'a' or i[1] == 'b' or i[2] == 'c':
        count += 1
print(count/len(res))