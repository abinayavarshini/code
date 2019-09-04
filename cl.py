class Stack: 
    def __init__(self):
        self.abi = []
    def is_empty(self):
        return self.abi == []
    def push(self, data):
        self.abi.append(data)
    def pop(self):
        return self.abi.pop()
pri= Stack()
barathi = input(' ') 
for char in barathi:
    pri.push(char)
rev_text = ''
while not pri.is_empty():
    rev_text = rev_text + pri.pop()
if barathi== rev_text:
    print('YES')
else:
    print('NO')
