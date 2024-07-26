from ss20_datastructs import FixedSizeStack

stack = FixedSizeStack(5, 1, 2, 3)
print(stack)
print(repr(stack))
print(stack.is_full())
print(stack.is_empty())
try:
    while True:
        print(stack.size, stack, stack.pop())
except IndexError as e:
    print("IndexError:", e)
print(stack.is_full())
print(stack.is_empty())
try:
    for i in range(1, 11):
        stack.push(i)
        print(stack)
except IndexError as e:
    print("IndexError:", e)
print(stack.is_full())
print(stack.is_empty())