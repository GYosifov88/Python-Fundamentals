text = input().split("\\")

for word in text:
    if '.' in word:
        needed = word.split('.')
        filename = needed[0]
        extension = needed[1]
        print(f"File name: {filename}")
        print(f"File extension: {extension}")



