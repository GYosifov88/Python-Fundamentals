number = int(input())
positives = []
negatives = []
sum_negattives = 0
positives_number = 0
for i in range (number):
    current_num = int(input())
    if current_num >= 0:
        positives.append(current_num)
        positives_number += 1
    else:
        negatives.append(current_num)
        sum_negattives += current_num

print(positives)
print(negatives)
print(f"Count of positives: {positives_number}")
print(f"Sum of negatives: {sum_negattives}")

