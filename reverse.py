n = int(input("Enter an integer: "))
revnum = 0
while n>0:
    rem = n%10
    revnum = revnum*10 + rem
    n=n//10
print(revnum)