class Queue():
    def __init__(self):
        self.data = []

    def insert(self, item):
        self.data.append(item)
    
    def remove(self):
        if len(self.data) > 0:
            return self.data.pop(0)
        
    def get_first(self):
        if len(self.data) > 0:
            return self.data[0]
    
    def empty(self):
        return not len(self.data) > 0
    

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    

def organize_queues(people):
    priority_queue = []
    simple_queue = []
    for person in people:
        if person["age"] >= 60:
            priority_queue.append(person)
        else:
            simple_queue.append(person)
        
    return {
        "simple": simple_queue, 
        "priority": priority_queue
    }


def get_people():
    action = 1

    people = []
    while action != 0:
        name = input("insert person's name ")
        age = int(input("insert person's age "))
        # person = Person(name, age)
        person = {
            "name": name,
            "age": age
        }
        people.append(person)

        print()
        action = int(input("insert 0 to stop and 1 to include another person "))

    queues = organize_queues(people)

    return queues


if __name__ == '__main__':
    people = get_people()

    simple_queue = Queue()
    priority_queue = Queue()

    count = 0

    for person in people.get("simple"):
        simple_queue.insert(person)
    for person in people.get("priority"):
        priority_queue.insert(person)
    
    while not (simple_queue.empty() and priority_queue.empty()):
        if not priority_queue.empty() and count < 2:
            person = priority_queue.remove()
            print(f'Atendendo PRIORITÁRIO: {person["name"]}')
            count += 1
        
        elif not simple_queue.empty():
            person = simple_queue.remove()
            print(f'Atendendo SIMPLES: {person["name"]}')
            count = 0 

        elif not priority_queue.empty():
            person = priority_queue.remove()
            print(f'\nAtendendo PRIORITÁRIO: {person["name"]}')
