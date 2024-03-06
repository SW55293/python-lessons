numCourses = 4 #(0, 1, 2, 3)
prerequisites = [(1, 0), (2, 0), (3, 1), (3, 2)]

mapped = {n: [] for n in range(numCourses)}

for course, pre_req in prerequisites:
    print(pre_req)
    mapped[pre_req].append(course)

# print(mapped
output_lines = [f"{key}: {value}" for key, value in mapped.items()]
print("\n".join(output_lines))

# for key, value in mapped.items():
#     print(f"{key}: {value}")

output_lines = map(lambda item: f"{item[0]}: {item[1]}", mapped.items())
print("\n".join(output_lines))






from collections import defaultdict

mapped = defaultdict(list)
for course, pre_req in prerequisites:
    mapped[course].append(pre_req)