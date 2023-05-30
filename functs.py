def noset(a, u):
    U = list(u)
    A = list(a)
    C = []
    for i in U:
        if i not in A:
            C.append(i)
    return set(C)


def union(a, b):
    a = list(a)
    b = list(b)
    c = b.copy()
    for i in a:
        if i not in c:
            c.append(i)
    return set(c)


def dif(a, b):
    a = list(a)
    b = list(b)
    C = []
    for i in range(len(a)):
        if a[i] not in b:
            C.append(a[i])
    return set(C)


def cross(a, b):
    A = list(a)
    B = list(b)
    C = []
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                C.append(A[i])
    return set(C)


def symdif(a, b):
    a = list(a)
    b = list(b)
    c = []
    for i in range(len(a)):
        if a[i] not in b:
            c.append(a[i])
    for j in range(len(b)):
        if b[j] not in a:
            c.append(b[j])
    return set(c)
