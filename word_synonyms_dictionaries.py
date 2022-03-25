number = int(input())
synonyms_dict = dict()
for num in range (number):
    word = input()
    synonym = input()

    if word not in synonyms_dict.keys():
        synonyms_dict[word] = list()

    synonyms_dict[word].append(synonym)

for word in synonyms_dict:
    synonyms = ", ".join(synonyms_dict[word])
    print(f"{word} - {synonyms}")