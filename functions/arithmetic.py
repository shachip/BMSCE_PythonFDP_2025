def add(n1,n2):
    return n1+n2


def sub(n1,n2):
    return n1 - n2


def mul(n1,n2):
    return n1 * n2


def div(n1,n2):
    return n1/n2


n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
operation = int(input("enter op no: "))

match operation:
    case 1:
        print(f"sum is {add(n1,n2)}")
    case 2:
        print(f"diff is {sub(n1,n2)}")
    case 3:
        print(f"product is {mul(n1,n2)}")
    case 4:
        print(f"quotient is {div(n1,n2)}")
    case 5:
        print(f"OKAY BYE")
    case _:
        print("Invalid operation")

