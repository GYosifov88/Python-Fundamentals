usernames = input().split(', ')
users = []
for word in usernames:
    valid_username = ''
    if 3 <= len(word) <=16:
        for char in word:
            if char.isalnum() or char == '-' or char == '_':
                valid_username += char
        users.append(valid_username)

    for name in users:           
        if name == word:
            print(name)





           











