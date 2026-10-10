tup = tuple(input("data1: ").split(","))
val = int(input('value: '))

print(f"tuple * {val} = {(tup * val)}")

tup2 = tuple(input("data2: ").split(","))
print("concatenation:",tup+tup2)