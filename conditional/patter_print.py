n=5
for i in range (1,n):
    for j in range(n-i-1):
        print(" ",end=' ')

    for k in range(2*i-1):
        print("*", end=' ')
    print()