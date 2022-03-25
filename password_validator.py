def password_checker():
    digits = 0
    for i in password:
        if i.isnumeric():
            digits +=1
    if 6 <= len(password) <= 10 and password.isalnum() == True and digits >= 2:
        print ("Password is valid")
    if len(password) > 10 or len(password) < 6:
        print("Password must be between 6 and 10 characters")
    if password.isalnum() != True:
        print("Password must consist only of letters and digits")
    if digits < 2:
        print("Password must have at least 2 digits")


password = input()

password_checker()