print({x for x in range(10) if x > 5})
# sum of only even numbers
numbers = set(range(0, 10))
print(sum(numbers))
print(sum({x for x in numbers if x % 2 == 0}))
print(sum({x for x in numbers if x % 2 == 1}))
print([n ** 2 + n >= 20 for n in numbers])
print([n ** 2 + n >= 20 for n in numbers if n > 3])
