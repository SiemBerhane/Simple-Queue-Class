
class StaticQueues():

    def __init__(self, queue, maxLength):
        self.queue = queue
        self.front = 0
        self.rear = 0
        self.size = 0
        self.max = maxLength

    def Size(self):
        return self.size

    def isFull(self):
        return (self.Size() >= self.max)

    def isEmpty(self):
        return not self.queue

    def enQueue(self, object):
        if self.isFull():
            print("Queue is full")
            return self.queue

        self.queue[self.rear] = object

        self.rear += 1
        self.size += 1

        return self.queue

    def deQueue(self):
        if self.isEmpty():
            print("Queue is empty")
            return self.queue

        removedElement = self.queue[self.front]
        self.front += 1
        self.size -= 1


        return removedElement


class PriorityQueue():

    def __init__(self, queue, maxNum):
        self.size = 0
        self.queue = queue
        self.maxSize = maxNum

    def PatientsPriority(self):
        over = False
        Counter1 = 0
        Counter2 = 0
        Counter1Plus2 = 0

        while over == False and not self.isFull():
            ID = input("Enter the patient ID or enter 0 to quit: ")
            
            if ID[0] == '0':
                over = True
                return self.queue            
            elif ID[0] == '1':
                self.queue.insert(Counter1, ID)
                Counter1 += 1
                Counter1Plus2 += 1
            elif ID[0] == '2':
                self.queue.insert(Counter1Plus2, ID)
                Counter2 += 1
                Counter1Plus2 += 1
            else:
                self.queue.append(ID)

            self.size += 1

        if self.isFull():
            print("Can\'t take any more patients")

        return self.queue

    def deQueue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
            
        removedElement = self.queue[0]
        self.queue.pop()
        return removedElement

    def isEmpty(self):
        return not self.queue

    def isFull(self):
        return (self.size >= self.maxSize)

    def GetSize(self):
        return self.size


class CircularQueue():

    def __init__(self, queue, maxSize):
        self.queue = queue
        self.front = 0
        self.rear = 0
        self.size = 0
        self.max = maxSize

    def isEmpty(self):
        return not self.queue

    def isFull(self):
        return (self.size >= self.max)

    def Size(self):
        return self.size

    def enQueue(self, object):
        if self.isFull():
            print("Queue is full")
            return self.queue
        
        self.queue[self.rear] = object
        self.rear = (self.rear + 1) % self.max
        self.size += 1

        return self.queue

    def deQueue(self):
        if self.isEmpty():
            print("Queue is empty")
            return self.queue

        removedElement = self.queue[self.front]

        self.queue[self.front] = ''
        self.front = (self.front + 1) % self.max
        self.size -= 1

        return removedElement






        

