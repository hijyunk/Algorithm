s1 = input()
s2 = input()
s3 = input()

fb = ['FizzBuzz', 'Fizz', 'Buzz']

if s1 not in fb:
    result = int(s1)+3
elif s2 not in fb:
    result = int(s2)+2
elif s3 not in fb:
    result = int(s3)+1

if result % 3 == 0 and result % 5 == 0: print(fb[0])
elif result % 3 == 0: print(fb[1])
elif result % 5 == 0: print(fb[2])
else: print(result)