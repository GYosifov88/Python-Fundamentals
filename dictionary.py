initial_string = input().split(' | ')
words_dictionary = dict()
for k in initial_string:
    current_word = k.split(': ')
    word = current_word[0]
    explanation = current_word[1]
    if word not in words_dictionary:
        words_dictionary[word] = list()
        words_dictionary[word].append(explanation)
    else:
        words_dictionary[word].append(explanation)

testing_words = input().split(' | ')

action = input()

if action == 'Test':
    for o in testing_words:
        if o in words_dictionary.keys():
            print(f"{o}:")
            for el in words_dictionary[o]:
                print(f" -{el}")

elif action == 'Hand Over':
    for j in words_dictionary:
        print(j, end=' ')
