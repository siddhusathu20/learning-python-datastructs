from ss20_datastructs import DoublyLinkedList

linky = DoublyLinkedList([1, 2, 3, 4])
print(list(linky))
print(repr(linky))
linky.append(7)
print(linky)
print(linky[0], linky[2], linky[4])
print(linky[1], linky[3])
print(linky.get(6))
print(linky.get(7, "Error"))
try:
    print(linky[5], linky[6], linky[7])
except IndexError as e:
    print("IndexError:", e)
print(linky[-1], linky[-3], linky[-5])
print(linky[-2], linky[-4])
print(linky.get(-3))
print(linky.get(-7))
try:
    for _ in range(6):
        print(linky.pop(), linky)
except IndexError as e:
    print("IndexError:", e)
for i in range(2, 13, 2):
    linky.append(i)
print(linky)
print(len(linky))
print(tuple(linky))
for k in linky:
    print(k)
print(linky, linky.get_end())
print(linky.delete(2))
print(linky)
print(linky.delete(4))
print(linky, linky.get_end())
print(linky.delete(0))
print(linky)
print(linky.delete(1))
print(linky)
linky.insert(1, 0)
print(linky)
linky.insert(7, 2)
print(linky)
print(linky.get(2))
print(linky[0], linky[2])
linky.insert(16, 3)
print(linky)
linky.insert(20, 4)
print(linky)
print(linky.get(5))
print(linky.get_end())
linky[3] = 72
print(linky)
linky[0] = 25
print(linky)
linky[5] = 256
print(linky)
linky[1] = 20
print(linky)
try:
    linky[6] = 512
except IndexError as e:
    print("IndexError:", e)
print(linky.index(72))
print(linky.index(20))
print(linky.indices(20))
print(linky.indices(128))
try:
    print(linky.index(128))
except ValueError as e:
    print("ValueError:", e)
print(linky)
print(linky.pop_left(), linky)
linky.append_left(-7)
print(linky)
print("---")
print(linky[1:5])
print(linky[1:5:2])
print(linky[:5])
print(linky[:5:3])
print(linky[:])
print(linky[::2])
print(linky[3:])
print(linky[3::2])
print(linky[::-1])
print(linky[::-2])
print(linky[3::-2])
print(linky[4:1:-1])
linky[3:] = [5, 6]
print(linky)
linky[1:3] = [1, 2, 3]
print(linky)