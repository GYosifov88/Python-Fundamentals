import re

number_of_messages = int(input())
special_letters = ['s', 't', 'a', 'r']
pattern = r'@(?P<name>[a-zA-Z]+)[^\@\-\!\:\>]*:(?P<population>\d+)[^\@\-\!\:\>]*!(?P<attack>[A|D])![^\@\-\!\:\>]*->(?P<soldiers>\d+)'
attacked_planets_list = list()
destroyed_planets_list = list()

for i in range(number_of_messages):
    special_num = 0
    encrypted_text = input()
    decrypted_text = ''
    lowe_encrypted_text = encrypted_text.lower()
    for char in lowe_encrypted_text:
        if char in special_letters:
            special_num += 1
    for charc in encrypted_text:
        new_charc = chr(ord(charc) - special_num)
        decrypted_text += new_charc

    matches = re.finditer(pattern, decrypted_text)

    for match in matches:
        planet = match.group('name')
        population = int(match.group('population'))
        attack_type = match.group('attack')
        soldiers = int(match.group('soldiers'))
        if attack_type == 'A':
            attacked_planets_list.append(planet)
        elif attack_type == 'D':
            destroyed_planets_list.append(planet)

attacked_planets_list = sorted(attacked_planets_list)
destroyed_planets_list = sorted(destroyed_planets_list)

print(f"Attacked planets: {len(attacked_planets_list)}")
for planet in attacked_planets_list:
    print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planets_list)}")
for k in destroyed_planets_list:
    print(f"-> {k}")
