# names = []

# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())

# for line in sorted(names):
#     print(line)
###comment###
with open("names.csv") as file:
    for line in file:
        name,age = line.rstrip().split(",")
        print(f"{name}'s age is {age}")
