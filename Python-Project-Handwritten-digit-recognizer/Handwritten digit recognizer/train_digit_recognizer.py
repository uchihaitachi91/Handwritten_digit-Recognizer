A = dict()
B = dict()
Y = dict()

A = {"a": 0.2, "b": 0.5, "c": 0.3, "d": 0.8, "e": 0.1}
B = {"a": 1, "b": 0.2, "c": 0.4, "d": 0.5, "d": 0.2}

print('The 1st fuzzy set :', A)
print('The 2nd fuzzy set :', B)

for A_key, B_key in zip(A, B):
    A_value = A[A_key]
    B_value = B[B_key]

    if A_value > B_value:
        Y[A_key] = A_value
    else:
        Y[B_key] = B_value

print('The union of the fuzzy set :', Y)

for A_key, B_key in zip(A, B):
    A_value = A[A_key]
    B_value = B[B_key]
    B_value = 1 - B_value

    if A_value < B_value:
        Y[A_key] = A_value
    else:
        Y[B_key] = B_value

print('The difference of fuzzy set is :', Y)

for A_key, B_key in zip(A, B):
    A_value = A[A_key]
    B_value = B[B_key]

    if A_value < B_value:
        Y[A_key] = A_value
    else:
        Y[B_key] = B_value
print('thw intersection of the fuzzy set:', Y)