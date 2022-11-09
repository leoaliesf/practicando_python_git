import numpy as np
# question (https://tutorial.eyehunts.com/info/data-structures-and-algorithms-questions/)
#firts---- 
print('How do you find the missing number in a given integer array of 1 to 100?')
completerange = set(np.arange(1,11))
list1 = set([9,2,3,4,5,1,7])
print (completerange - list1)
print()
#second-----
print('How do you find the duplicate number on a given integer array?')
import collections
list2 = [1,1,2,3,4,5,6,7,9,10]
print([item for item, count in collections.Counter(list2).items() if count > 1])
print()
#third-------
print('How do you find the largest and smallest number in an unsorted integer array?')
list3 = np.random.randint(-100,200,100)
print('this is the largest:',list3.max())
print('this is the smaller:',list3.min())
print('solve without module')
# solve without module import
num_max=-9999999**35
num_min=9999999**35
for n in range(len(list3)):
    if num_max >= list3[n]:
        continue
    else:
        num_max = list3[n]
for n in range(len(list3)):
    if num_min <= list3[n]:
        continue
    else:
        num_min = list3[n]
print('this is the largest:',num_max,' ','this is the smaller:',num_min)
print()



#Fourth--------
print('How do you find all pairs of an integer array whose sum is equal to a given number?')
given_num= 14
list4 = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13])
def result(lista,num):
    list5=[]
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i] + lista[j] == num:
                list5.append(tuple([lista[i],lista[j]]))
    return list5

print(result(list4, given_num))
print()
#five -----
print('How do you find duplicate numbers in an array if it contains multiple duplicates?')
import collections
list6 = np.array([1,1,2,3,4,5,6,7,9,10,11,1,3,2,5,10,1,3])
print([item for item, count in collections.Counter(list6).items() if count > 1]) # if you wanna see the duplicate numbers and count dis-comment belove and commet all this line
print([(item, count) for item, count in collections.Counter(list6).items() if count > 1])
print()
#six -----
print('How are duplicates removed from a given array ?')
list7 = np.random.randint(1,20,100)
print(list(set(list7)))
text ="hello every one"
print(list(set(text))) 
list8 = ['hello', 3, 3.8, 'hi', 1, 2.3, 3, 'hi']
print(list(set(list8)))
print()

