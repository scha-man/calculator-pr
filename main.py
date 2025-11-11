def calculate(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    return None

def main():
    assert calculate(3, '+', 2) == 5
    assert calculate(4, '-', 2 ) == 2

if __name__ == '__main__':
    main()
