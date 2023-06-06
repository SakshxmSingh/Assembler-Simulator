class rf:

    def __init__(self):
        self.registers = {'R0':'0000000000000000',
                          'R1':'0000000000000000',
                          'R2':'0000000000000000',
                          'R3':'0000000000000000',
                          'R4':'0000000000000000',
                          'R5':'0000000000000000',
                          'R6':'0000000000000000',
                          'FLAGS':'0000000000000000'}
    
    def writeData(self, key, value):
        self.registers[key] = value

    def fetchData(self, key):
        return self.registers[key]

    def dump(self):
        for i in self.registers:
            if i == 'FLAGS':
                print(self.registers[i])
            else:
                print(self.registers[i], end=' ')