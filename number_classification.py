numbers_list = input().split(', ')
numbers = list(map(int, numbers_list))
positives = list(i for i in numbers if i >= 0)
positive = ', '.join([str(a) for a in positives])
negatives = list(i for i in numbers if i < 0)
negative = ', '.join([str(a) for a in negatives])
evens = list(i for i in numbers if i % 2 == 0)
even = ', '.join([str(a) for a in evens])
odds = list(i for i in numbers if i % 2 != 0)
odd = ', '.join([str(a) for a in odds])

print(f"Positive: {positive}")
print(f"Negative: {negative}")
print(f"Even: {even}")
print(f"Odd: {odd}")