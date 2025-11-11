def calculate(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b != 0:
            return a // b
        else:
            raise Exception('division by 0')
    return None

def main():
    assert calculate(3, '+', 2) == 5
    assert calculate(4, '-', 2 ) == 2
    try:
        calculate(10,'/', 0)
        assert False
    except Exception:
        pass
    assert calculate(10, '*', 5) == 50
    assert calculate(10, '/', 5) == 2

if __name__ == '__main__':
    main()
