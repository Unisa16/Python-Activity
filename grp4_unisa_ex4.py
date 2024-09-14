# Condition in if statement
def check_condition(num): return True if num > 15 else False

# Test the condition
print("20 > 15:", check_condition(20))
print("7 > 15:", check_condition(7))

# List, Tuple, Set, Dictionary with String, int, boolean
my_list = ["anime", 42, True]
my_tuple = ("roadtrip", 23, False)
my_set = {"onlinegames", 17, True}
my_dict = {"nickname": "Ravine", "age": 21, "is_gamer": False}

# Print collections
print("\nList:", my_list)
print("Tuple:", my_tuple)
print("Set:", my_set)
print("Dictionary:", my_dict)

# Access elements
print("\nList - String:", my_list[0], "Int:", my_list[1], "Bool:", my_list[2])
print("Tuple - String:", my_tuple[0], "Int:", my_tuple[1], "Bool:", my_tuple[2])

# Access Set elements (types)
print("\nSet elements with types:", [(e, type(e)) for e in my_set])

# Access Dictionary elements
print("\nDictionary - String:", my_dict["nickname"], "Int:", my_dict["age"], "Bool:", my_dict["is_gamer"])
