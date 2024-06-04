def countdigit(n):
    count = 0
    while n>0:
        n =n//10
        count +=1
    return count  
n = int(input("Enter the number: "))
ans = countdigit(n)
print(ans)
