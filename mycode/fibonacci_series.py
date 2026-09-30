def fibonacci_series(n):
    series = []

    a = 0
    b = 1

    for i in range(n):
        series.append(a)
        a, b = b, a + b

    return series