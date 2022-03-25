sequence = input().split(', ')
numbers_sequence = list(map(int, sequence))
counter = 10
list =[]
while len(numbers_sequence) > 0:
    list = ([num for num in numbers_sequence if (counter - 10) < num <= counter ])
    print (f"Group of {counter}'s: {list}")
    numbers_sequence = ([num for num in numbers_sequence if (counter - 10) < num > counter])
    counter += 10