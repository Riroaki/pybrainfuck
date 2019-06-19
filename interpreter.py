import sys
from getch import getch


def tokenize(source: str) -> list:
    """Split source code into token list."""
    tokens = {'<', '>', '+', '-', '.', ',', '[', ']'}
    code = list(filter(lambda x: x in tokens, source))
    return code


def evaluate(code: list):
    """Execute code."""

    def get_brace_map() -> dict:
        _brace_map, _stack = {}, []
        for _index, _command in enumerate(code):
            if _command == '[':
                _stack.append(_index)
            elif _command == ']':
                if len(_stack) == 0:
                    raise SyntaxError()
                _left, _right = _stack.pop(), _index
                _brace_map[_left] = _right
                _brace_map[_right] = _left
        return _brace_map

    def parse_add():
        data[ptr['data']] = (data[ptr['data']] + 1) % 256

    def parse_sub():
        data[ptr['data']] = (data[ptr['data']] + 255) % 256

    def parse_left():
        ptr['data'] = max(0, ptr['data'] - 1)

    def parse_right():
        ptr['data'] += 1
        if ptr['data'] == len(data):
            data.append(0)

    def parse_out():
        sys.stdout.write(chr(data[ptr['data']]))

    def parse_in():
        data[ptr['data']] = getch()

    def parse_loop_start():
        if data[ptr['data']] == 0:
            ptr['code'] = brace_map[ptr['code']]

    def parse_loop_end():
        if data[ptr['data']] != 0:
            ptr['code'] = brace_map[ptr['code']]

    # Get brace map where left braces and right ones are binded
    brace_map = get_brace_map()
    # Bind command code in brainfuck with parser method
    command_map = {'+': parse_add, '-': parse_sub, '<': parse_left,
                   '>': parse_right, '.': parse_out, ',': parse_in,
                   '[': parse_loop_start, ']': parse_loop_end}
    data, end = [0], len(code)
    # Move ptrs into a dict so that local methods can modify them
    ptr = {'data': 0, 'code': 0}
    # Execute each command
    while ptr['code'] < end:
        command_bf = code[ptr['code']]
        command_py = command_map[command_bf]
        command_py()
        ptr['code'] += 1


def execute(source: str):
    """Execute source code of brainfuck language."""
    code = tokenize(source)
    evaluate(code)


def main():
    with open('test.bf', 'r') as f:
        source = f.read()
    execute(source)


if __name__ == '__main__':
    main()
