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
    return 0


def multiple():
    print("Selected Multiplication")
    return 0


def divide():
    print("Selected Division")
    return 0

def error():
    print("Error #1 -- Invalid input, please rerun program.")
# --------------
print("Please enter selection")
print("Enter '1' for Circle Adding")
sel(int(input()))
