class Object:
    def __init__(self, type):
        self.type = type

    def square(self, a, b):
        if self.type == 'square':
          return  a * b
        if self.type == 'triangle':
           return (a * b) / 2

vid = input()

object = Object(vid)
a = int(input())
b = int(input())

print(f'{object.square(a,b)}')
