n = list(input())
num_list = (list(map(lambda x:int(x), n)))
num_list = sorted(num_list, reverse=True)
print(*[i for i in num_list], sep='')