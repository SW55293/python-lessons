'''
d = {
    <key>: <value>,
    <key>: <value>,
      .
      .
      .
    <key>: <value>
}

Or using dict()
d = dict([
    (<key>, <value>),
    (<key>, <value),
      .
      .
      .
    (<key>, <value>)
])
'''
# Dictionary elements are not accessed by numerical index:


def test_graph():
    numCourses = 4 #(0, 1, 2, 3)
    prerequisites = [(1, 0), (2, 0), (3, 1), (3, 2)]

    mapped = {n: [] for n in range(numCourses)}

    for course, pre_req in prerequisites:
        # print(pre_req)
        mapped[pre_req].append(course)

    print(mapped.items())
    print(mapped.keys())
    print(mapped.values())
    print()
    # enumerate(iterable, start)
    for c, p in enumerate(prerequisites):
        print(c,p)
    print()
    print(mapped)
    # enumerate will give the index position of each key
    for c, p in enumerate(mapped): 
        print( c, p)

    # other example
    from collections import defaultdict

    mapped = defaultdict(list)
    for course, pre_req in prerequisites:
        mapped[course].append(pre_req)



def test_dict():
    info = {}

    names = ['steph', 'potato', 'turd', 'cat', 'dog']
    for x in range(len(names)):
        info[x] =  names[x]  
     
    print(info)


print(test_dict())








''' 
output_lines = [f"{key}: {value}" for key, value in mapped.items()]
print("\n".join(output_lines))

# for key, value in mapped.items():
#     print(f"{key}: {value}")

output_lines = map(lambda item: f"{item[0]}: {item[1]}", mapped.items())
print("\n".join(output_lines))

'''




