initial_text = input().split(' ')
palindrome_word = input()
palindrome_list = []

for word in initial_text:
    if word == "".join(reversed(word)):
        palindrome_list.append(word)

print(palindrome_list)
print(f"Found palindrome {palindrome_list.count(palindrome_word)} times")