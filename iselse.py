india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
city = input("Enter the city name:")
if city in india:
    print(f"{city} is in india")
elif city in pakistan:
    print(f"{city} is in pakistan")
elif city in bangladesh:
    print(f"{city} is in bangladesh")
else :
    print(f"i won't able to tell in which country this {city} is located")


city1 = input("enter city1: ")
city2 = input("enter city 2: ")
if city1 in india and city2 in india:
    print("both cities are in india")
elif city1 in pakistan and city2 in pakistan:
    print("both cities are in pakistan")
elif city1 in bangladesh and city2 in bangladesh:
    print("both cities are in bangladesh")
else:
    print("they don't belong to the same country")


sugarlevel = input("enter your sugar level:")
sugarlevel = float(sugarlevel)
if sugarlevel<80 :
    print("your sugar level is low")
elif sugarlevel>100 :
    print("your sugarlevel is high")
else:
    print("your sugarlevel is normal")


