class Queue():
    def __init__(self):
        self.data = []

    def insert(self, item):
        self.data.append(item)
    
    def remove(self):
        if len(self.data) > 0:
            return self.data.pop(0)
        
    def get_first(self):
        if len(self.data > 0):
            return self.data[0]
    
    def empty(self):
        return not len(self.data > 0)


q = Queue()

q.insert(1)
q.insert(2)
q.insert(3)
q.insert(4)

q.remove()
q.get_first()
q.empty()