class AlgoHashTable:

    def __init__(self, size):
        '''Creates a hash table'''
        self.size = size
        self.hashMap = self.createBuckets()

    def createBuckets(self):
        '''Method to create buckets for the hash table'''
        return [[] for _ in range(self.size)]

    def setVal(self, key, value):
        '''Sets the value of a key value pair in the hash table'''
        hashedKey = hash(key) % self.size
        bucket = self.hashMap[hashedKey]
        foundKey = False
        for index, record in enumerate(bucket):
            recordKey, recordValue = record
            if recordKey == key:
                foundKey = True
                break
        if foundKey:
            bucket[index] = (key, value)
        else:
            bucket.append((key, value))

    def getVal(self, key):
        '''Returns the value of a key value pair in the hash table'''
        hashedKey = hash(key) % self.size
        bucket = self.hashMap[hashedKey]
        foundKey = False
        for index, record in enumerate(bucket):
            recordKey, recordValue = record
            if recordKey == key:
                foundKey = True
                break
        if foundKey:
            return recordValue
        else:
            return "No record found"

    def __str__(self):
        '''String method override'''
        return "".join(str(item) for item in self.hashMap)

hashTable = AlgoHashTable(256)

with open('data.txt') as f:
    for line in f:
        key, value = line.split(':')
        hashTable.setVal(key, value)

print(hashTable.getVal('brian@gmail.com'))
print(hashTable.getVal('example@example.com'))
