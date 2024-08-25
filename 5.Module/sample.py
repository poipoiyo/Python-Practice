from collections import Counter

food = ["beef", "beef", "fish", "beef", "pork", "chicken", "fish", "pork"]
count_food = Counter(food)

print(food)
print(count_food)

lunch = ["beef", "fish"]
count_lunch = Counter(lunch)

print(count_food - count_lunch)
# print(count_food & count_lunch)
# print(count_food | count_lunch)


