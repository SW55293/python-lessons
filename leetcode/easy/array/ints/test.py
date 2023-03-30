

l = [[30,20000], [7,100], [43,0]]
l.sort()
print(l)

for x in range(1, len(l)):
    print(l[x-1][1])
    if l[x-1][1] > l[x][0]:
        print('False')
print('True')


'''
sorted = [[7, 100], [30, 20000], [43, 0]]
[x-1][1]                          | [x][0]      
1 = [0][1] -> [7,100]   [100]     | [1][0] = [7,100]   [7] 
2 = [1][1] -> [30,2000] [2000]    | [2][0] = [30,2000] [30]
3 = [2][1] -> [43,0]    [0]       | [3][0] = [43,0]    [43]

compares ending times per block with starting times 
'''