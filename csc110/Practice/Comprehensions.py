my_set = {1, 2, 3}

print({4 for x in my_set})
print({x ** 2 for x in my_set})
# print({char ** 2 for char in 'Jamie'})
print({char * 2 for char in 'Jamie'})
print([char * 2 for char in 'Jamie'])
print([char + '!' for char in 'Mario'])
print(1 in my_set)
print({x: x ** 2 for x in my_set})
print({x for x in range(30, 51)})
