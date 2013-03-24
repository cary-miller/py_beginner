'''
This is a triple-quoted comment
'''

a_variable = 1
a_variable = 4356
a_variable = 'a'
a_variable = 'your message here'

# this is a comment
x = 2  # another comment


this_is_a_list = [1, 2, 'a', 'b', a_variable]

# We access list items by indexing
item_2 = this_is_a_list[1]
item_1 = this_is_a_list[0]
# Note the zero-based indexing.
# It can be non-intuitive at first but there are good reasons for it.

# Lists have *methods* that we can use to extract useful things or find out
# more about the list or perform useful work.
sorted_list = this_is_a_list.sort()


this_is_a_dictionary = {'a':1, 'bb':33, 'another':a_variable}
# We access dictionary items by name
a_thing = this_is_a_dictionary['bb']
a_second_thing = this_is_a_dictionary['another']

# Like lists, dictionaries have *methods* but not the same ones.
d_keys = this_is_a_list.keys()
print d_keys
# print is a a useful builtin function.














