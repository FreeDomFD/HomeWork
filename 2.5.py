def Urav(A1,A2,B1,B2,C1,C2):
    D = A1 * B2 - A2 * B1
    x = (C1 * B2 - C2 * B1) / D
    y = (A1 * C2 - A2 * C1) / D
    print(x, y)

Urav(1,2,3,4,5,6)
