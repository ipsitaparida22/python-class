def armstrong(num):
    ans = 0 
    k = len(str(num))
    temp = num
    while num>0:
        rem = num%10
        ans = ans+ rem**k
        num = num//10
    return temp==ans

ans=armstrong(12)
print(ans)