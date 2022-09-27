names = ["mahmoud", 'farida', "ali", "hassan",
         "mohamed", "khaled", "taha", "pyton"]


# 1- uppercase normal list
new_name_upper_list = []

for name in names:
    new_name_upper_list.append(name.upper())

print(new_name_upper_list)

# 1- uppercase list comprehension
print([name.upper() for name in names])

# 1- uppercase functional programming
print(list(map(lambda name: name.upper(), names)))

# 2 - contains ‘a’ in a list using  normal list
new_name_a = []

for name in names:
    if name.find("a") != -1:
        new_name_a.append(name)
print(new_name_a)

# 2 - contains ‘a’ in a list using list comprehension
print([name for name in names if name.find("a") != -1])

# 2 - contains ‘a’ in a list using functional programming
print(list(filter(lambda name: name.find("a") != -1, names)))


# 3 - starts with ‘t’ in a list using normal list
new_name_t = []

for name in names:
    if name.startswith("t"):
        new_name_t.append(name)

print(new_name_t)

# 3 - starts with ‘t’ in a list using list comprehension

print([name for name in names if name.startswith("t")])
# print([name for name in names if name[0] == "t"])

# 3 - starts with ‘t’ in a list using functional programming
print(list(filter(lambda name: name.startswith("t"), names)))
# print(list(filter(lambda name: name[0]== "t",names)))


# 4 - contains 2 or more ‘a’ letter using normal list
new_name_letter = []

for name in names:
    if name.count("a") >= 2:
        new_name_letter.append(name)
print(new_name_letter)

# 4 - contains 2 or more ‘a’ letter using list comprehension
print([name for name in names if name.count("a") >= 2])

# 4 - contains 2 or more ‘a’ letter using functional programming
print(list(filter(lambda name: name.count("a") >= 2, names)))
