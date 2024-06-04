
n = int(input("Enter an integer: "))
revnum = 0
while n>0:
    rem = n%10
    revnum = revnum*10 + rem
    n=n//10
if n == revnum:
   print("it is a palindrome")
else:
   print("it is not a palindrome")
