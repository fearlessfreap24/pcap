class Stack:
    def __init__(self) -> None:
        self.__Stack_List = []
        self.__top = None

    def push(self, val):
        self.__Stack_List.append(val)
        self.__top = val

    def pop(self):
        val = self.__Stack_List[-1]
        del self.__Stack_List[-1]
        if len(self.__Stack_List) == 0:
            self.__top = None
        else:
            self.__top = self.__Stack_List[-1]
        return val

    def peek(self):
        return self.__top


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

    def get_sum(self):
        return self.__sum



if __name__ == "__main__":
    stack = Stack()
    for I in range(10):
        stack.push(I)
    
    for J in range(10):
        print(f"pop = {stack.pop()}, peek = {stack.peek()}")

    add_stack = AddingStack()

    for i in range(10):
        add_stack.push(i)
        print(f"i = {i}, sum = {add_stack.get_sum()}")

    for i in range(10):
        print(f"sum before pop = {add_stack.get_sum()}, pop = {add_stack.pop()}, sum = {add_stack.get_sum()}")