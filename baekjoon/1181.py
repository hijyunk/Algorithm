n = int(input())

words = []
for _ in range(n):
	words.append(input())

words = set(words)
print(*sorted(words, key=lambda x : (len(x), x)), sep="\n")