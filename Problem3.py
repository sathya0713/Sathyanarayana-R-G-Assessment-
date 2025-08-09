def odd_series_limit(n: int):
    limit = n if n % 2 != 0 else n - 1
    series = []
    for i in range(1, limit + 1, 2):
        series.append(i)
    return series

print(odd_series_limit(6))
