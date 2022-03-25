number = int(input())
positives = []
negatives = []
odd = []
even = []
for i in range (number):
    current_number = int(input())
    if current_number >= 0:
        positives.append(current_number)
    else:
        negatives.append(current_number)
    if current_number % 2 == 0:
        even.append(current_number)
    else:
        odd.append(current_number)
command = input()

if command == "odd":
    print(odd)
elif command == "even":
    print(even)
elif command == "positive":
    print(positives)
elif command == "negative":
    print(negatives)
