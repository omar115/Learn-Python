letters = ["a", "b", "c"]

# add

# example -1
letters.append("d")
# example-2
letters.insert(0, "-")

# remove

#example-1
letters.pop(0)
# example-2
letters.remove("b")
# example-3
del letters[0:3]
# example- 4
letters.clear()
# example-5
print(letters)