result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count = 0 
for item in result:
   if item == "head":
      count += 1
print("Heads count: ",count)

for i in range(1,11):
   if i%2 == 0:
      print(i*i)


month_list = ["January", "February", "March", "April", "May"]
expense_list = [2340, 2500, 2100, 3100, 2980]
e = input("Enter expense amount: ")
e = int(e)

month = -1
for i in range(len(expense_list)):
   if e == expense_list[i]:
      month = i
      break
   
if month != -1:
   print(f'you spent {e} in {month_list[month]}')
else:
   print(f'you didn\'t spend {e} in any month')


for i in range(5):
   print(f"you ran {i+1} miles")
   tired = input("Are you tired? ")
   if tired == 'yes':
      break

if i == 4:
   print("Hurray! you are a rockstsr you just finished 5 km race!")
else:
   print("you didn't finish 5 km race but hey congrats anyways! you still ran {i+1} miles")


for i in range (1,6):
   s = ' '
   for j in range (i):
      s += '*'
   print(s)