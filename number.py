#You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.
length = 92
width = 48.8
area = length * width
print(area)


#You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back?
num_of_packets = 9
cost_per_packets = 1.49
total_cost = num_of_packets*cost_per_packets
total_paid = 20
cash_back = total_paid - total_cost
print("money returned: ",cash_back)

#You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length. If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles. Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)
length= 5.5
per_cost = 500
area = length ** 2
total_cost = area * per_cost
print("The total cost is : ", total_cost)

#Print binary representation of number 17
num = 17
print("The binary of number 17 is: ",format(num,'b'))