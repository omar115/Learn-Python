letters = ["a", "b", "c"]

# add

# example -1
letters.append("d")
# example-2
letters.insert(0, "-")  # will insert into specific list

# remove

#example-1
letters.pop(0)  # will remove first index value
# example-2
letters.remove("b") # will remove b value
# example-3
del letters[0:3]    # will remove first to index 2
# example- 4
letters.clear() # will remove entire list
# example-5
print(letters)