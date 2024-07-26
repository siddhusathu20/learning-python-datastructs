from ss20_datastructs import BoundedListQueue

queue = BoundedListQueue(6, 1, 2, 3)
print(queue)
print(repr(queue))
print(queue.is_full())
print(queue.is_empty())
try:
    while True:
        print(queue.size, queue, queue.dequeue())
except IndexError as e:
    print("IndexError:", e)
print(queue.is_full())
print(queue.is_empty())
try:
    for i in range(1, 11):
        queue.enqueue(i)
        print(queue)
except IndexError as e:
    print("IndexError:", e)
print(queue.is_full())
try:
    while True:
        queue.dequeue()
        print(queue)
except IndexError as e:
    print("IndexError:", e)
print(queue.is_full())
print(queue.is_empty())
for k in queue:
    print(k)