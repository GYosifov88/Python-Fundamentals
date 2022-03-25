def sum_func(first_word, second_word):
    total_sum = 0
    for i in range(len(first_word)):
        if i < len(second_word):
            total_sum += ord(first_word[i]) * ord(second_word[i])
        else:
            total_sum += ord(first_word[i])

    return total_sum


def char_multi(first_world, second_world):
    result = 0
    if len(first_world) > len(second_world):
        result = sum_func(first_world, second_world)

    else:
        result = sum_func(second_world, first_world)

    print(result)


text = input().split(' ')
char_multi(text[0], text[1])

