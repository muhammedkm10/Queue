class queueusingstack:
    def __init__(self):
        self.instack = []
        self.outstack = []
    def enque(self,data):
        self.instack.append(data)
    def dequeu(self):
        if len(self.instack)==0 and len(self.outstack) == 0:
            print('the queue is empty')
        else:
            for i in range(len(self.instack)):
               self.outstack.append(self.instack.pop())
            return self.outstack.pop()
    def traverse(self):
        if len(self.instack) == 0:
            for j in self.outstack:
                print(j)
        else:
            for i in self.instack:
                print(i)
    def isempty(self):
        if len(self.instack) == 0 and len(self.outstack) == 0:
            print('the queue is empty')
        else:
            print("the queue is not empty")
    def size(self):
       print(f'the size of the queue is {len(self.outstack) + len(self.instack)}')
    def peek(self):
        if len(self.instack) == 0 and len(self.outstack) == 0:
            print('the queue is empty')
        else:
            for i in range(len(self.instack)):
                self.outstack.append(self.instack.pop())
            print(f"the peek element of the queue is {self.outstack[-1]}")
q = queueusingstack()
q.enque(98)
q.enque(64)
# o = q.dequeu()
# q.isempty()
# q.size()
# print(o)
q.peek()
q.traverse()