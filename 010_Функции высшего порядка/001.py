def f(x):
    return x* x
a = f
print(a(5))
print(id(f))
print(f(5))
print(id(a))