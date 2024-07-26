from ss20_datastructs import UnboundedListQueue

queue = UnboundedListQueue(1, 2, 3)
print(queue)
print(repr(queue))
print(queue.is_empty())
try:
    while True:
        print(queue, queue.dequeue())
except IndexError as e:
    print("IndexError:", e)
print(queue.is_empty())
for i in range(1, 5):
    queue.enqueue(i)
print(queue)
print(queue.is_empty())
print(queue.peek())
print(queue.dequeue(), queue)
queue.enqueue(6)
print(queue)
print(queue.dequeue(), queue)
print(queue.peek())
for k in queue:
    print("-", i)