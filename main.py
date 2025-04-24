class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == '__main__':
  p1 = Person('Josue', 19)
  print(p1.age)
  print(p1.name)