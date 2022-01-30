import collections
scientist = collections.namedtuple("scientist", [
    'name',
    'field',
    'born',
    'nobel',
])

print(scientist)
print(type(scientist))
ada = scientist(name="Ada Lovelace", field="math", born=1815, nobel=False)
print(ada)
print(ada.born)

# can not assign values
# try:
ada.name = 'Ed'
print(ada.name)