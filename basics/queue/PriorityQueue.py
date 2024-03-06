from dataclasses import dataclass, field
from typing import Any
from queue import PriorityQueue
import heapq
import bisect


@dataclass(order=True)
class Data:
  priority: int
  item: Any = field(compare=False)


# using queue
q = PriorityQueue()

q.put(Data(5, "how"))
q.put(Data(4, "to"))
q.put(Data(1, "do"))
q.put(Data(3, "in"))
q.put(Data(2, "java"))

for i in range(5):
  print(q.get())


# Using heapq

class Item:
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return 'Item({!r})'.format(self.name)


class PriorityQueue:
  def __init__(self):
    self._queue = []
    self._index = 0

  def push(self, item, priority):
    heapq.heappush(self._queue, (-priority, self._index, item))
    self._index += 1

  def pop(self):
    return heapq.heappop(self._queue)[-1]


q = PriorityQueue()
q.push(Item('how'), 1)
q.push(Item('to'), 5)
q.push(Item('do'), 4)
q.push(Item('in'), 2)
q.push(Item('java'), 1)

q.pop()


# using bisect

class PriorityQueue:
  def __init__(self):
    self.queue = []

  def insert(self, data, priority):
    bisect.insort(self.queue, (priority, data))

  def pop(self):
    return self.queue.pop()[1]


q = PriorityQueue()

q.insert('how', 5)
q.insert('to', 4)
q.insert('do', 5)
q.insert('in', 8)
q.insert('java', 1)

for i in range(5):
  print(q.pop())
