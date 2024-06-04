n=5
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()


n = 5
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()


n = 5
for i in range(n):
    for j in range(i+1):
        print(j+1,end="")
    print()


n = 5
for i in range(n):
    for j in range(i+1):
        print(i+1,end="")
    print()





n=5
for i in range(n):
    for j in range(n-i):
        print("*",end="")
    print()


n = 5 
for i in range(n):
    for j in range(n-i):
        print(j+1,end="")
    print()


n = 5
for i in range(n):
    for j in range(n-1-i):
        print(" ", end="")
    for j in range(2*i+1):
        print("*",end="")
    print()


n = 5
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for j in range(2*(n-1-i)+1):
        print("*",end="")
    print()


n = 5
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(n):
    for j in range(n-i):
            print("*",end="")
    print()


n = 5
for i in range(n):
    for j in range(i+1):
        if (i+j)%2==0:
            print("1",end="")
        else:
            print("0",end="")
    print()

n = 4
for i in range(n):
    for j in range(i+1):
        print(j+1,end="")
    
    for j in range((n-i-1)*2):
        print(" ",end="")
    for j in range(i+1,0,-1):
        print(j,end="")
    print()


n = 5
k = 1
for i in range(n):
    for j in range(i+1):
        print(k,end=" ")
        k +=1
    print()

n = 5
def numtochar(num):
    return(chr(num+65))
for i in range(n):
    for j in range(i+1):
        print(numtochar(j),end="")
    print()


n = 5
def numtochar(num):
    return(chr(num+65))
for i in range(n):
    for j in range(n-i):
        print(numtochar(j),end="")
    print()


n = 5
def numtochar(num):
    return(chr(num+65))
for i in range(n):
    for j in range(i+1):
        print(numtochar(i),end="")
    print()

n = 4
def numtochar(num):
    return(chr(num+65))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i):
        print(numtochar(j),end="")
    for j in range(i,-1,-1):
        print(numtochar(j),end="")
    print()

n = 5
k=n-1
def numtochar(num):
    return(chr(num+65))
for i in range(n):
    for j in range(i+1):
        print(numtochar(k+j),end="")
    k -=1
    print()

n = 5
for i in range(2*n):
    if i<n:
        for j in range(n-i):
            print("*",end="")
        for j in range(2*i):
            print(" ",end="")
        for j in range(n-i):
            print("*",end="")
    else:
        for j in range(i-n+1):
            print("*",end="")
        for j in range((2*n-i-1)*2):
            print(" ",end="")
        for j in range(i-n+1):
            print("*",end="")

    print() 


n = 5
for i in range(2*n-1):
    if i<n:
        for i in range(i+1):
            print("*",end="")
        for j in range((n-i-1)*2):
            print(" ",end="")
        for j in range((i+1)):
            print("*",end="") 
    else:
        for j in range(2*n-i-1):
            print("*",end="")
        for j in range((i-n+1)*2):
            print(" ",end="")
        for j in range(2*n-i-1):
            print("*",end="")    
    print()

n = 5 
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()


n = 4
for i in range(2*n-1):
    for j in range(2*n-1):
        row = min(i,2*n-2-i)
        col = min(j,2*n-2-j)
        ans = min(row,col)
        print(n-ans,end="")
    print()