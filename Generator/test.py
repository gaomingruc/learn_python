g_1 = (i for i in range(10))

print(next(g_1))
print(next(g_1))
print(next(g_1))
print(next(g_1))
print(next(g_1))

print("-" * 10)

for i in g_1:
    print(i)

print("-" * 10)

def point_x_y():
    x = 0
    k = 2
    b = 1
    while True:
        y = k * x + b
        tuple_k_b = yield x, y
        if tuple_k_b:
            k, b = tuple_k_b
        x += 1

g_xy = point_x_y()
print(next(g_xy))
print(next(g_xy))
print(next(g_xy))
print(next(g_xy))
print(g_xy.send((1, 0)))
print(next(g_xy))
print(next(g_xy))
print(next(g_xy))
print(next(g_xy))