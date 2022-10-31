n = int(input())
apart = [list(map(int, input().split())) for _ in range(n)]

from itertools import product
temp = list(product([j[0] for j in apart],[j[0] for j in apart]))
temp2 = [i[1] for i in apart] * n
val = 0
val_list = []
for i in range(len(temp)):
    val += abs(temp[i][0]-temp[i][1])*temp2[i]
    if (i+1)%n == 0: 
        val_list.append(val)
        val = 0
        
print(val_list.index(min(val_list))+1)