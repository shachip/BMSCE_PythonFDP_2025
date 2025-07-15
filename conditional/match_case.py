month = int(input("Enter month number: "))
match month:
    case 1:
        print("Jan")
    case 2:
        print("Feb")
    case 3:
        print("Mar")
    case 4:
        print("apr")
    case 5:
        print("may")
    case 6:
        print("jun")
    case _:
        print("Either INVALID or not in the first six months")