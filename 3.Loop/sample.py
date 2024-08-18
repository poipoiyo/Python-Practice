# check flag
print("----- sample 1 -----\n")
i = 1
while i < 5:
    # The condition you want to find
    if i > 6:
        print("i is out of range.")
        break
    i = i+1
else:
    print("i is in the range") 

print("\n----- sample 2 -----")
flag = False
for i in range(5):
    # The condition you want to find
    if i > 3: 
        flag = True
        break

s = "Flag is " + "True" if flag else "False"
print(s, "\n")

# enumerate
print("\n----- sample 3 -----")
seasons = ['spring', 'summer', 'fall', 'winter']
for i, season in enumerate(seasons):
   print(i, season)

# create list
print("\n----- sample 4 -----")
x = [i+2 for i in range(5)]
print(x)

# all , any
print("\n----- sample 5 -----")
x = [s == "summer" for s in seasons]
if any(x):
    print("There is summer in list seasons.")
else:
    print("There is no summer in list seasons.")

if all(x):
    print("There are all summers in list seasons.")
else:
    print("There are not all summers in list seasons.")




