'''
This is a triple-quoted comment
'''

a_variable = 1
a_variable = 4356
a_variable = 'a'
a_variable = 'your message here'

# this is a comment
x = 2  # another comment


this_is_a_list = [222, 'x', 1, 'b', a_variable, 77]

# We access list items by indexing
item_2 = this_is_a_list[1]
item_1 = this_is_a_list[0]
# Note the zero-based indexing.
# It can be non-intuitive at first but there are good reasons for it.

# Lists have *methods* that we can use to extract useful things or find out
# more about the list or perform useful work.
this_is_a_list.sort()
another_list = [1,1,2,3,5,8,13,21]


this_is_a_dictionary = {'a':1, 'bb':33, 'another':a_variable}
# We access dictionary items by name
a_thing = this_is_a_dictionary['bb']
a_second_thing = this_is_a_dictionary['another']

# Like lists, dictionaries have *methods* but not the same ones.
d_keys = this_is_a_dictionary.keys()
print d_keys
# print is a a useful builtin function.
d_vals = this_is_a_dictionary.values()
d_things = this_is_a_dictionary.items()


# We can *re-assign* the elements of a list.
# We can *re-assign* the elements of a dictionary.
# We can add new elements to a dictionary.
# We can add new elements to a list.














