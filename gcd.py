def find_gcd(n1,n2):
    gcd = 1
    n1= int(input("Enter the value: "))
    n2=int(input("Enter the value: "))
    for i in range(1, min(n1,n2)+1):
        if n1%i==0 and n2 %i == 0:
          gcd = i
    gcd = find_gcd(n1,n2)
    print("GCD OF", n1, "and",n2,"is:",gcd)