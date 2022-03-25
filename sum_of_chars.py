number_of_letters = int(input())
sum = 0
digit = 0
for i in range (1, number_of_letters + 1):
    letter = input()
    sum += ord(letter)
print(f"The sum equals: {sum}")
