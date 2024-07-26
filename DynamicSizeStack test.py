from ss20_datastructs import DynamicSizeStack

stack = DynamicSizeStack(1, 2, 3)
print(stack)
print(repr(stack))
print(stack.peek())
stack.push(4)
print(stack)
print(stack.peek())
print(stack.is_empty())
for i in stack:
    print(i)
popped = stack.pop()
print(popped)
print(stack)
print(stack.peek())
for i in range(3):
    print(stack, stack.pop())
    print(stack.is_empty())
try:
    print(stack.pop())
except IndexError as e:
    print("IndexError:", e)
for k in range(2, 11, 2):
    stack.push(k)
print(stack)
stack2 = DynamicSizeStack()
print(stack2)
stack2.push(1)
stack2.push(3)
stack2.push(7)
print(stack2)