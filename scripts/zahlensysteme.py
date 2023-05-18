while True:
    A = input("A: ").split(',')
    B = input("B: ").split(',')

    I = input("I: ")

    ten = 0
    for i in range(len(I)):
        ten += A.index(I[i]) * len(A) ** (len(I)-1-i)

    V = []
    while ten!=0:
        mod = ten % len(B)
        V.insert(0, B[mod])

        ten = int(ten/len(B))

    O = ""
    for item in V:
        O += item
    print(O)
