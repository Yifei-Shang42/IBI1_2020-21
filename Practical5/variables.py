a = 020502
b = 190784
c = 100321
d = abs(a - c)
e = abs(a - b)

if d > e:
    print("d is greater")
elif d == e:
    print("d == e")
else:
    print("e is greater")

X = True
Y = False
Z = (X and not Y) or (Y and not X)
print(Z)

X = False
Y = True
Z = (X and not Y) or (Y and not X)
print(Z)

W = X != Y
if W == Z:
    print(W == Z)

