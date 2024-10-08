codes = list(map(int, input().split()))
if codes == list(range(1,9)): print('ascending')
elif codes == list(range(8,0,-1)): print('descending')
else: print('mixed')