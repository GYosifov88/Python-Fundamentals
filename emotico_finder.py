# text = input().split(' ')
# for word in text:
#     emoticon = ''
#     if ':' in word:
#         if word[1] != ' ':
#             emoticon = ':' + word[1]
#             print(emoticon)
import ntpath


def emoticon_finder(text):
    result = [text[i] + text[i+1] for i in range(len(text)) if text[i] == ':' and text[i+1] != ' ']
    print('\n'.join(result))


text = input()
emoticon_finder(text)