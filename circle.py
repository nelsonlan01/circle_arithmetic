def sel(var):
    if var == 1:
        add()
    elif var == 2:
        minus()
    elif var == 3:
        multiple()
    elif var == 4:
        divide()
    elif var <= 0 or var >= 5:
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
        total = total + (m - i)
        i += 1
    print(total)


def add_api(m, n):
    total = 0
    i = 0
    while i < n:
        total = total + (m - i)
        i += 1
    return total


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
            total = total - (m - i)
        i += 1
    print(total)


def minus_api(m, n):
    total = 0
    i = 0
    while i < n:
        if i == 0:
            total = m
        elif i != 0:
            total = total - (m - i)
        i += 1
    return total


def multiple():
    print("Selected Multiplication")
    total = 1
    print("Enter m value")
    m = int(input())
    print("Enter n value")
    n = int(input())
    i = 0
    if n <= m:
        while i < n:
            total = total * (m - i)
            i += 1
        print(total)
    elif n > m:
        print(0)
        print("Success #1 -- Return with value 0")


def multiple_api(m, n):
    total = 1
    i = 0
    if n <= m:
        while i < n:
            total = total * (m - i)
            i += 1
        return total
    elif n > m:
        print("Success #1 -- Return with value 0")
        return 0


def divide():
    print('Selected Division')
    total = 0.0
    d_zero = False
    print("Enter m value")
    m = int(input())
    print("Enter n value")
    n = int(input())
    i = 0
    while i < n:
        if n > m:
            print("Error #2 -- Undefined divide by 0")
            d_zero = True
            break
        elif i == 0:
            total = m
        elif i != 0:
            total = total / (m - i)
        i += 1
    if d_zero == False:
        print(total)


def divide_api(m, n):
    total = 0.0
    d_zero = False
    i = 0
    while i < n:
        if n > m:
            d_zero = True
            print("Error #2 -- Undefined divide by 0")
            break
        elif i == 0:
            total = m
        elif i != 0:
            total = total / (m - i)
        i += 1
    if d_zero == False:
        return total


def error():
    print("Error #1 -- Invalid input, please rerun program.")


def default():
    print("Please enter selection")

print(30 * "-", "MENU", 30 * "-")
print("Please enter mode")
print("1 : For menu selection")
print("2 : For API testing")
mode = int(input())
print(30 * "-", "MENU", 30 * "-")

if mode == 1:
    # -------MANUAL-------
    print(30 * "-", "MENU", 30 * "-")
    print("Please enter selection")
    print("1 : for Circle Adding")
    print("2 : for Circle Subtraction")
    print("3 : for Circle Multiplication")
    print("4 : for Circle Division")
    print(30 * "-", "MENU", 30 * "-")
    sel(int(input()))
    # -------MANUAL-------
elif mode == 2:
    # -------API-------
    print(add_api(3, 3))  # 6
    print(minus_api(3, 2))  # 1
    print(multiple_api(4, 3))  # 24
    print(divide_api(3, 2))  # 1.5
    # -------API-------
