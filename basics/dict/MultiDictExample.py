from multidict import MultiDict

# Creating a Multidict
multidict = MultiDict()
multidictWithItems = MultiDict([('key', 'value1'), ('key', 'value2'), ('new_key', 'value3')])

multidict.clear()

# Adding Items into MultiDict
multidict['key'] = 'value'
# <MultiDict('key': 'value')>
print(multidict)
multidict.add('key', 'another_value')
# <MultiDict('key': 'value', 'key': 'another_value')>
print(multidict)
multidict.setdefault('key_default', 'default_value')
# <MultiDict('key': 'value', 'key': 'another_value', 'key_default': 'default_value')>
print(multidict)

multidict.clear()

# Accessing Values
multidict.add('fruit', 'apple')
multidict.add('fruit', 'banana')
multidict.add('fruit', 'orange')

print(multidict['fruit']) # apple
print(multidict.get('fruit', default='No fruit')) # apple
print(multidict.getone('fruit', default='No fruit'))  # apple
print(multidict.getall('fruit', default='No fruit'))  # ['apple', 'banana', 'orange']

multidict.clear()

# Updating values in Multidict
multidict['key'] = 'value'
multidict.add('key', 'another_value')
multidict.update({'key': 'new_value'})

print(multidict)
multidict.clear()

# Updating a specific value in the multidict

multidict['key'] = 'value'
multidict.add('key', 'another_value')

update_key = 'key'
existing_value = 'another_value'
new_value = 'new_value'

if update_key in multidict:
  values = multidict.getall(update_key)

  if existing_value in values:
    index_to_update = values.index(existing_value)
    values[index_to_update] = new_value
    multidict.update({update_key: values})

print("Updated Multidict:", multidict)

# Deleting values from Multidict
del multidict['key']

multidict.pop('new_key')
# multidict.popone('new_key')
# multidict.popall('new_key')
# multidict.popitem()

print(multidict)

# Clearing Multidict
multidict.clear()

print(multidict)
