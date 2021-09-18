my_set = {1, 2, 3}

print({4 for x in my_set})
print({x ** 2 for x in my_set})
# print({char ** 2 for char in 'Jamie'})
print({char * 2 for char in 'Jamie'})
print([char * 2 for char in 'Jamie'])
print([char + '!' for char in 'Mario'])
print(1 in my_set)
print({x: x ** 2 for x in my_set})
print({x*2:x*3 for x in range (6)})
print({x for x in range(30, 51)})
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print({(x,y) for x in set1 for y in set2})
print({-x for x in set1})
print([x for x in range(5, -1, -1)])
