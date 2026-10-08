#assignment 1
tuple1 = tuple(x for x in range(1, 11))
print(f"Tuple 1: {tuple1}")

#assignment 2
print(f"First: {tuple1[0]}")
print(f"Middle: {tuple1[len(tuple1)//2]}")
print(f"Last: {tuple1[-1]}")

#assignment 3
print(f"First three: {tuple1[:3]}")
print(f"Last three: {tuple1[-3:]}")
print(f"Two Five: {tuple1[1:5]}")

#assignment 4
import random
#specify tuple constructor each time
nested_tuples = tuple(
    tuple(x for x in random.choices(range(1, 11), k=3))
    for r in range(3)
)
print(f"Set matrix: {nested_tuples}")
print(f"Matrix 2nd row, 3rd column: {nested_tuples[1][2]}")

#assignment 5
concat_1 = (1, 2, 3)
concat_2 = (4, 5, 6)
print(f"Concatenate: {concat_1 + concat_2}")

#assignment 6
dup_elements = tuple(x for x in random.choices(range(1, 11), k=5))
print(f"Duplicated elements: {dup_elements}")
print(f"Occurence of 2: {dup_elements.count(2)}")
try:
    print(f"First occurence of 2 is index {dup_elements.index(2)}")
except ValueError as v:
    print("Element 2 isn't in list.")

#assignment 7
unpack_tup = tuple(x for x in random.choices(range(1, 11), k=5))
a, b, c ,d, e = unpack_tup
print(f"Unpacking: {a}, {b}, {c}, {d}, {e}")

#assignment 8
first_five = [x for x in range(1, 6)]
tuple_five = tuple(first_five)
print(f"Initial list: {first_five}")
print(f"Converted to tuple: {tuple_five}")

#assignment 9
trituples = tuple(
    tuple(x for x in random.choices(range(90, 101), k=3))
    for r in range(3)
)
print(f"Trituples: {trituples}")

#assignment 10
back_again = list(tuple_five)
back_again.append(6)
round_and_round = tuple(back_again)
print(f"Adding 6: {round_and_round}")

#assignment 11
tuple_char = tuple(("h", "a", "l", "l", "o"))
print(f"Initial: {tuple_char}")
print(f"Initial joined: {"".join(tuple_char)}")

#assignment 12
places = {(5,10): "Tavern", (2, 3): "Restaurant", (8, 9): "Dungeon"}
for k, v in places.keys():
    print(f"Coordinates {k,v} is a {places.get((k,v))}")

#assignment 13