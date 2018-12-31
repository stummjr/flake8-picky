
data = list(range(100))

x = map(lambda x: 2 * x, data)
print(x)

y = filter(lambda x: x % 2 == 0, data)
print(y)
