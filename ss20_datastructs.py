class DynamicSizeStack:
    """
    Wrapper around a list that acts as a dynamically sized stack.
    
    The optional arguments passed to the constructor are used as values to initialise the stack with.
    """

    def __init__(self, *values):
        self._stack = list(values)
    
    def __len__(self):
        return len(self._stack)
    
    def __iter__(self):
        for element in self._stack:
            yield element
    
    def __repr__(self):
        return f"DynamicSizeStack({self._stack})"
    
    def __str__(self):
        return str(self._stack)
    
    def push(self, element):
        self._stack.append(element)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow")
        return self._stack.pop()
    
    def peek(self):
        return self._stack[-1]
    
    def is_empty(self):
        return True if len(self._stack) == 0 else False


class FixedSizeStack:
    """
    Wrapper around a list that acts as a fixed size stack.
    
    The first (and only mandatory) argument passed to the constructor specifies the stack's size.
    All arguments following it are elements used to initialise the stack.
    """

    def __init__(self, size: int, *values):
        self._stack = list(values)
        self.size = size
        if len(values) > size:
            raise ValueError("Too many values provided")
    
    def __len__(self):
        return len(self._stack)
    
    def __iter__(self):
        for element in self._stack:
            yield element
    
    def __repr__(self):
        return f"FixedSizeStack({self.size}, {self._stack})"
    
    def __str__(self):
        return str(self._stack)
    
    def push(self, element):
        if self.is_full():
            raise IndexError("Stack overflow")
        self._stack.append(element)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow")
        return self._stack.pop()
    
    def peek(self):
        return self._stack[-1]
    
    def is_empty(self):
        return True if len(self._stack) == 0 else False
    
    def is_full(self):
        return True if len(self._stack) >= self.size else False


class UnboundedListQueue:
    """
    Wrapper around a list that acts as a dynamically sized queue.
    
    The optional arguments passed to the constructor are used as values to initialise the queue with.
    """

    def __init__(self, *values):
        self._queue = list(values)
    
    def __len__(self):
        return len(self._queue)
    
    def __iter__(self):
        for element in self._queue:
            yield element
    
    def __repr__(self):
        return f"UnboundedListQueue({self._queue})"
    
    def __str__(self):
        return str(self._queue)
    
    def enqueue(self, element):
        self._queue.append(element)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue empty")
        return self._queue.pop(0)
    
    def peek(self):
        return self._queue[0]
    
    def is_empty(self):
        return True if len(self._queue) == 0 else False


class BoundedListQueue:
    """
    Wrapper around a list that acts as a fixed size (bounded) queue.
    
    The first (and only mandatory) argument passed to the constructor specifies the queue's size.
    All arguments following it are elements used to initialise the queue.
    """

    def __init__(self, size: int, *values):
        self._queue = list(values)
        self.size = size
        if len(values) > size:
            raise ValueError("Too many values provided")
    
    def __len__(self):
        return len(self._queue)
    
    def __iter__(self):
        for element in self._queue:
            yield element
    
    def __repr__(self):
        return f"BoundedListQueue({self.size}, {self._queue})"
    
    def __str__(self):
        return str(self._queue)
    
    def enqueue(self, element):
        if self.is_full():
            raise IndexError("Queue full")
        self._queue.append(element)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue empty")
        return self._queue.pop(0)
    
    def peek(self):
        return self._queue[0]
    
    def is_empty(self):
        return True if len(self._queue) == 0 else False
    
    def is_full(self):
        return True if len(self._queue) >= self.size else False


class SinglyLinkedList:
    """
    A simple singly linked list that can behave as a stack.
    """

    class Node:
        def __init__(self, data, pos):
            self.data = data
            self.pos = pos
            self.next = None

    def __init__(self, *values):
        self.start = None
        self.end = None
        self.size = 0
        if len(values) == 1:
            self.start = self.end = self.Node(values[0], 0)
            self.size = 1
        elif len(values) > 1:
            next_node = self.Node(values[0], 0)
            self.start = self.end = next_node
            self.size = 1
            for val in values[1:]:
                next_node.next = self.Node(val, self.end.pos + 1)
                next_node = next_node.next
                self.end = next_node
                self.size += 1
    
    def __str__(self):
        return str(self.to_list())
    
    def __repr__(self):
        return f"SinglyLinkedList({self.to_list()})"
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
        current_node = self.start
        while current_node is not None:
            yield current_node.data
            current_node = current_node.next
    
    def to_list(self):
        current_node = self.start
        converted = []
        while current_node is not None:
            converted.append(current_node.data)
            current_node = current_node.next
        return converted
    
    def append(self, element):
        if self.end is None:
            self.start = self.end = self.Node(element, 0)
        else:
            next_node = self.Node(element, self.end.pos + 1)
            self.end.next = next_node
            self.end = next_node
        self.size += 1
    
    def get(self, index):
        current_node = self.start
        while current_node is not None:
            if current_node.pos == index:
                return current_node.data
            current_node = current_node.next
        return None
    
    def pop(self):
        current_node = self.start
        if self.end is None:
            raise IndexError("List is empty, cannot pop from empty list")
        if self.start == self.end:
            deleted_value = self.end.data
            self.start = self.end = None
            self.size = 0
            return deleted_value
        while current_node is not None:
            if current_node.pos == self.size - 2:
                deleted_value = self.end.data
                current_node.next = None
                self.end = current_node
                self.size -= 1
                return deleted_value
            current_node = current_node.next
        return None
    
    def delete(self, index):
        current_node = self.start
        deleted_value = None
        if index == 0 and self.end is not None:
            deleted_value = self.start.data
            self.start = self.start.next
            self.size -= 1
        while current_node is not None:
            if current_node.pos == index - 1:
                deleted_value = current_node.next.data
                current_node.next = current_node.next.next
                self.size -= 1
            elif current_node.pos >= index:
                current_node.pos -= 1
            current_node = current_node.next
        return deleted_value
    
    def insert(self, element, index):
        if index >= self.size:
            raise IndexError("Cannot insert at that position, try append()")
        current_node = self.start
        if self.end is None:
            next_node = self.Node(element, 0)
            self.start = self.end = next_node
            self.size = 1
        elif index == 0:
            next_node = self.Node(element, 0)
            next_node.next = self.start
            self.start = next_node
            self.size += 1
        while current_node is not None:
            if current_node.pos == index - 1:
                next_node = self.Node(element, index)
                next_node.next = current_node.next
                current_node.next = next_node
                self.size += 1
                current_node = current_node.next
            elif current_node.pos >= index:
                current_node.pos += 1
            current_node = current_node.next