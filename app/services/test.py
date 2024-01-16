def foo(n, a, b):
    flag = 1
    if (a - b) > n:
        return flag
    else:
        flag += 1
        return foo(n, a + (a - b), b)


n, a, b = map(int, input().split())
print(a)
print(foo(n, a, b))
