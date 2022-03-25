number_of_electrons = int(input())
filled_selfs = []
counter = 1

while True:
    element = 2 * (counter ** 2)

    if element < number_of_electrons:
        number_of_electrons -= element
        filled_selfs.append(element)
    else:
        filled_selfs.append(number_of_electrons)
        break
    counter +=1

print(filled_selfs)