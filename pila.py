class Stack:
    def __init__(self):
        self.length = 0
        self.storage = list()

    def insert_data(self, data):
        self.length += 1  # self.length = self.length + 1
        self.storage.append(data)

    def get_data(self):
        if self.length < 1:
            raise Exception("Stack is empty, cannot get more data")
        self.length -= 1  # self.length = self.length - 1
        return self.storage.pop()

    def __str__(self):
        return str(self.storage)


pila1 = Stack()
pila1.insert_data(1)
pila1.insert_data(5)
pila1.insert_data(2)
print(pila1)

print(pila1.get_data())
print(pila1)
print(pila1.length)

print(pila1.get_data())
print(pila1)
print(pila1.length)

print(pila1.get_data())
print(pila1)
print(pila1.length)

print(pila1.get_data())
print(pila1)
print(pila1.length)

