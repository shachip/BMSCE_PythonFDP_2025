a = [1, "Hello", 10.5, True] #heterogenous
#array is homogenous

myList = [1,2,3,4,5]
anotherList = list(range(2,101,2)) #creating list using in-built function


print(myList)
print(anotherList)

#accessing elements
print(myList[2])
print(myList[2:8])
print(myList[-3:-8])


#modifying list
myList[-2] = 300
myList.append(11)        #in-built list functions
myList.insert(5,3000)
print(myList)

myList.remove(5)
print(myList)
myList.pop()
print(myList)

myList.sort(reverse=True)
print(myList)
