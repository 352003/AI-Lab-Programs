def unify(a, b):
    c = []
    for i in range(len(a)):
        if a[i] != b[i]:
            print(f"{b[i]}/{a[i]}")
            c.append([a[i], b[i]])
    return c

a = ['a', 'b']
b = ['x', 'y']

if len(a) == len(b):
    result = unify(a, b)
    if not result:
        print("Allowed")

print(result)
