class Queue:
  def __init__(self):
    self.queue = []

  def enqueue(self, item):
    self.queue.insert(0, item)

  def dequeue(self):
    index = len(self.queue) - 1
    item = self.queue[index]
    del self.queue[index]
    return item
  
  def is_empty(self):
    if len(self.queue) == 0:
      return True
    else:
      return False
    
  def size(self):
    return len(self.queue)

q = Queue()
print(q.queue)
q.enqueue('one')
print(q.queue)
q.enqueue('two')
print(q.queue)
q.dequeue()
print(q.queue)
print(q.is_empty())
print(q.size())
