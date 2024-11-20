class Stack:
    stack: list

    def __init__(self, string: str) -> None:
        self.stack = [i for i in string]

    def is_empty(self) -> bool:
        result = True
        if self.stack:
            result = False
        return  result

    def push(self, elem: str) -> None:
        self.stack.append(elem)

    def pop(self) -> str:
        result = self.stack[-1]
        del self.stack[-1]
        return result

    def peek(self) -> str:
        return self.stack[-1]

    def size(self) -> int:
        return self.stack.__len__()
