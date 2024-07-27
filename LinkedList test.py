from ss20_datastructs import SinglyLinkedList

linky = SinglyLinkedList(1, 2, 3, 4)
print(linky)
linky.append(7)
print(linky)
print(linky[0], linky[2], linky[4])
print(linky[1], linky[3])
print(linky.get(6))
try:
    print(linky[5], linky[6], linky[7])
except IndexError as e:
    print("IndexError:", e)
try:
    for _ in range(6):
        print(linky.pop(), linky)
except IndexError as e:
    print("IndexError:", e)
for i in range(2, 13, 2):
    linky.append(i)
print(linky)
print(len(linky))
print(list(linky))
print(tuple(list(linky)))
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
linky.insert(16, 3)
print(linky)
linky.insert(20, 4)
print(linky)
print(linky.get(5))
print(linky.get_end())