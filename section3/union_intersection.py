list1 = [1, 3, 4, 5, 7]
list2 = [2, 3, 5, 6]

print((set(list1).union(set(list2))))
print((set(list1).intersection(set(list2))))

union_list = list2.copy()
for item in list1:
    if item not in list2:
        union_list.append(item)
print(sorted(union_list))

intersection_list = []
for item in list1:
    if item in list2:
        intersection_list.append(item)
print(sorted(intersection_list))
