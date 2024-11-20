from stack_class import Stack


def pair_of_brackets(bracket_in: str, bracket_out: str) -> bool:
    brackets_dict = {'(': ')', '[': ']', '{': '}'}
    if bracket_in in brackets_dict:
        return brackets_dict[bracket_in] == bracket_out
    else:
        return False


def correct_stack(string: str) -> str:
    res = {1: "Сбалансированно", 0: "Несбалансированно"}
    brackets_stack = Stack(string)
    buffer_stack = []
    for i in brackets_stack.stack:
        if i in '([{':
            buffer_stack.append(i)
        else:
            if not buffer_stack:
                return res[0]
            else:
                if pair_of_brackets(buffer_stack[-1], i):
                    del buffer_stack[-1]
                else:
                    return res[0]
    if not buffer_stack:
        return res[1]
