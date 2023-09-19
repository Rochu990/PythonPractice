from collections import Counter

my_list = [11,1,1,1,2,2,2,2,23,3,3,33,3,4,4,4,5,5,5,6,66,7,7,7,7,7,8,8,8,8,8,9,9,9]

counter = Counter(my_list)

print(counter)

most_common = counter.most_common(1)
print(most_common[0][0])
