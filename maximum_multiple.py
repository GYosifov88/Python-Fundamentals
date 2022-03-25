divisor = int(input())
boundary = int(input())
count = 0
max_num = -10000000000000000000000000
for i in range (boundary):
    count += 1
    if count % divisor == 0:
        max_num = count

print(max_num)