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