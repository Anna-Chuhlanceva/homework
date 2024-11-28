my_dict = {'Anna' : 1989, 'Eugi' : 1988, 'Kate': 1988, 'Darya': 1990}
print(my_dict)
print (my_dict['Anna'])
my_dict['Bone'] = 2015
print (my_dict['Bone'])
my_dict.update({'Masha': 1991,
                'Ksusha': 1985})
print(my_dict)
a= my_dict.pop('Masha')
print(a)
print(my_dict)

my_set = {'Anna' , 1, 4, 2, 1, 11, 111, 0 ,(123, 15, 28), 'Anna'}
print(my_set)
my_set.add( 'Eugi')
my_set.add( '123')
#my_set.update('Olga', 'Denis')
my_set.remove('Anna')
print(my_set)

