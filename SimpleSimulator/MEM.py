class mem:
    def __init__(self):
        self.memory = ['0000000000000000'] * 128

    def initialize(self, input):
        for i in range(len(input)):
            self.memory[i] = input[i].strip()
    
    def dump(self):
        for i in range(len(self.memory)):
            print(self.memory[i])

    def fetchData(self, address):
        return self.memory[address]
    
    def writeData(self, address, data):
        self.memory[address] = data

    def readData(self, address):
        return self.memory[address]