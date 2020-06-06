def sel(var):
    if var == 1:
        add()
    elif var == 2:
        minus()
    elif var == 3:
        multiple()
    elif var == 4:
        divide()
    elif var<=0 or var>=5:
        error()


def add():
    print("Selected Addition")
    total = 0
    print("Enter m value")
    m = int(input())
    print("Enter n value")
    n = int(input())
    i = 0
    while i < n:
        total = total + (m-i)
        i += 1
    print(total)


def minus():
    print("Selected Subtraction")
    total = 0
    print("Enter m value")
    m = int(input())
    print("Enter n value")
    n = int(input())
    i = 0
    while i < n:
        if i == 0:
            total = m
        elif i != 0:
            total = total - (m-i)
        i += 1
    print(total)


def multiple():
    print("Selected Multiplication")
    total = 1
    print("Enter m value")
    m = int(input())
    print("Enter n value")
    n = int(input())
    i = 0
    while i < n:
        total = total * (m-i)
        i += 1
    print(total)


def divide():
    print('Selected Division')
    total = 0.0
    print("Enter m value")
    m = int(input())
    print("Enter n value")
    n = int(input())
    i = 0
    while i < n:
        if n > m:
            break
        elif i == 0:
            total = m
        elif i != 0:
            total = total / (m-i)
        i += 1
    print(total)

def error():
    print("Error #1 -- Invalid input, please rerun program.")
# --------------
print("Please enter selection")
print("Enter '1' for Circle Adding")
print("Enter '2' for Circle Subtraction")
print("Enter '3' for Circle Multiplication")
print("Enter '4' for Circle Division")
sel(int(input()))
