

nums =[3,2, 2, 2, 3]


element_counts = {}
for item in nums:
    element_counts[item] = element_counts.get(item, 0) + 1

values = []
for value in element_counts.values():
    values.append(value)

print(max(values))

for key, value in element_counts.items():
    if value == max(values):
        print(key)

