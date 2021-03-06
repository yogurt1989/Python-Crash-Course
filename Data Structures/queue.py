# Python Crash Course 
# queue.py
# Created by Mauro J. Pappaterra on 11 of March 2018.

# A Python implementation of a Queue
# A queue is a FIFO data structure. This is a single ended queue.
# e.g.: 5 -> 4 -> 3 -> 2 -> 1

class queue():

    def __init__(self, element = None):
        "Class constructor"
        self.data = element # head of the queue
        self.tail = None

    def queue (self, element):
        "Adds element to the tail of the queue"
        if (self.data == None):
            self.data = element # if queue is empty add element to head
            return

        current = self

        while (current.tail != None):
            current = current.tail # find the tail of the queue

        current.tail = queue(element) # add new element to the tail of the queue

    def unqueue (self):
        "Pops out element from the head of the queue"
        if (not self.data == None):
            data = self.data  # return current element

            if (self.tail == None): # return last element on the queue
                self.data = None
                return data

            self.data = self.tail.data # second element becomes new head of the queue
            self.tail = self.tail.tail

            return data
        else:
            print("The queue is empty!")

    def is_empty (self):
        "Returns True if the queue is empty"
        return (self.data == None)

    def size(self):
        "Returns size of the queue"
        if (not self.data == None):
            counter = 1
            current = self
            while (current.tail != None):
                counter += 1
                current = current.tail

            return counter
        else:
            return 0

    def print_queue (self):
        "Prints contents of the queue"
        if (self.data != None):
            elements = [self.data]

            current = self
            while(current.tail != None):
                current = current.tail
                elements.append(current.data)

            printout =''
            for element in elements[::-1]:
                printout += str(element) + ' -> '
            print(printout[0:-3])

        else:
            print("The queue is empty!")

# ALL TESTS
q1 = queue()

q1.queue(1)
q1.queue(2)
q1.queue(3)
q1.queue(4)
q1.queue(5)

q1.print_queue()

print(q1.unqueue())
print(q1.unqueue())
print(q1.unqueue())

q1.print_queue()

print(q1.unqueue())
print(q1.unqueue())
print(q1.unqueue())

q1.print_queue()

q2 = queue("a")

q2.queue("b")
q2.queue("c")
q2.queue("d")
q2.queue("e")
q2.queue("f")
q2.queue("g")

q2.print_queue()

q2.queue("h")
q2.queue("i")
q2.queue("j")
q2.queue("k")

q2.print_queue()
print(q2.size())

print(q2.unqueue())
print(q2.unqueue())
print(q2.unqueue())
print(q2.unqueue())
print(q2.unqueue())
print(q2.unqueue())

q2.print_queue()
print(q2.size())

print(q2.unqueue())
print(q2.unqueue())
print(q2.unqueue())
print(q2.unqueue())
print(q2.unqueue())

q2.print_queue()
print(q2.unqueue())