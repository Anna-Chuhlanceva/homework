immutable_var = (1, 2, [0, 5, 9], 1<5, 'hello world')
print (immutable_var)
# immutable_var [0]=9 не получилось, потому что этот элемент должен остаться неизменным
# print (immutable_var)
immutable_var [2][0]= 'summer'
mutable_list = [1, 11, 'winter', 3>5, [0, 12, 'hello', 135, 'Anna']]
mutable_list [4][0]=123
print(mutable_list)