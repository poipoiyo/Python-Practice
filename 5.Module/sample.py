from collections import Counter

food = ["beef", "beef", "fish", "beef", "pork", "chicken", "fish", "pork"]
count_food = Counter(food)

print("List :", food)
print("\nCounter :", count_food)

lunch = ["beef", "fish"]
count_lunch = Counter(lunch)

print("\n\n--- count_food - count_lunch ---")
print(count_food - count_lunch)

print("\n--- count_food & count_lunch ---")
print(count_food & count_lunch)

print("\n--- count_food | count_lunch ---")
print(count_food | count_lunch)


