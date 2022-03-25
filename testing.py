class Georgi:
    def __init__(self, first):
        self.first = first


    def kvartal(self, kvartal):
        if kvartal == 'Asparuhovo':
            return "Eat fish in VArna"
        elif kvartal == 'Mladost':
            return "Eat shkembe in Varna"

name = input()
kvartal = input()
george = Georgi(name)

print (george.kvartal(kvartal))