# queue = []
#
# def enqueue(data):
#     queue.append(data)
# def dequeue():
#     if len(queue) == 0:
#         print("the queue is empty")
#     else:
#         queue.pop(0)
# def traverse(queue):
#     for i in queue:
#         print(i)
# def isempty():
#     if len(queue) == 0:
#         print('the queue is empty')
#     else:
#         print("the queue is not empty")
# def size():
#     print(f'the size of the queue is {len(queue)}')
# def peek():
#     print(f"the peek element of the queue is {queue[-1]}")
#
# enqueue(90)
# enqueue(99)
# enqueue(66)
# traverse(queue)
# dequeue()
# print("after deleting")
# traverse(queue)
# enqueue(600)
#
# isempty()
# size()
# peek()
#
#
#
# IMPLEMENTATION OF STACK USING LINKED LIST
class node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class queue1:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    def traverse(self):
        if self.front is None:
            print("the queue is empty")
        else:
            current = self.front
            while current is not None:
                print(current.data)
                current = current.ref
    def enque(self,data):
        node1 = node(data)
        if self.front is None:
            self.front = node1
        else:
            self.rear.ref = node1
        self.rear = node1
        self.size  += 1
    def dequeue(self):
        if self.front  is None:
            print("the queue is empty you cant delete the elements in the queue")
            return
        else:
            deleted_data = self.front.data
            self.front  = self.front.ref
            if self.front is None:
                self.rear = None
            self.size -= 1
            return deleted_data


    def empty(self):
        if self.front is None:
            print("the queue is empty")
        else:
            print("the queue is not empty")

    def peek(self):
        print(f'the peek element of the queue is {self.front.data}')
    def sizeofthequeue(self):
        print(f'the size of the queue is {self.size}')

q  = queue1()
q.enque(89)
q.enque(19)
q.enque(8922)
q.dequeue()
q.sizeofthequeue()
q.peek()



q.traverse()