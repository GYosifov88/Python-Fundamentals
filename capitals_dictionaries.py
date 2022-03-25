countries = input().split(", ")
capitals = input().split(", ")

combined = zip(countries, capitals)
dict = dict(combined)

for country in dict.keys():
    print (f"{country} -> {dict[country]}")