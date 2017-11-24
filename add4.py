a = [0,1,2,3,4,5,6,7,8,9]
b1 = [x**2 for x in a]
b2 = list(map(lambda x: x**2,a))
print('{}\t {} {}'.format(a, b1, b2))