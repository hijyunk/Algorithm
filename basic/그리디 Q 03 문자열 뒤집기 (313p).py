s = input()

part_0 = s.split('1')
part_0 = list(filter(None, part_0))
part_1 = s.split('0')
part_1 = list(filter(None, part_1))

print(len(part_1)) if len(part_1) <= len(part_0) else print(len(part_0))