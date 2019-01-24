my_hero_set = {"Iron Man", "Black Panther", "Captain America", "Hulk"}

# Junkyard
negative_zone = {"Dr. Doom", "Red Skull", "Moonknight"}

heroList = list(my_hero_set)
print("new hero list", heroList)
IronMan = heroList[0]

showroom = set()
# print(len(my_hero_set))

showroom.add("Thor")
# showroom.add(IronMan)
showroom.update({"Ant-Man", "Spider-Man", "Moonknight"})


# print(showroom)

showroom.discard("Thor")

# print(showroom)

# showroom.intersection(negative_zone)
# print(showroom.intersection(negative_zone))

# gotta update the variable in order to be able to print
showroom = showroom.union(negative_zone, my_hero_set)
print("showroom", showroom)

showroom.discard("Dr. Doom")
showroom.discard("Red Skull")

print("after discard", showroom)

