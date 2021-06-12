# traditional approach
# inputs = list()
# current = input('Write Something')
# while current != "quit":
#     inputs.append(current)
#     current = input("Write someting more: ")


# simplify using walrus

inputs = list()
while(current := input('Write something: ')) != 'quit':
    inputs.append(current)