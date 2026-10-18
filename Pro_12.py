name = input("Your name: ")
club = input("Club name: ")

member_number = 8
points = 9.5
is_active = True
print("Member number: ", member_number, "-> type: ", type(member_number))
print("points: ", points, "-> type: ", type(points))
print("active: ", is_active, "-> type: ", type(is_active))

badge_code = name[0:3] + club[-1:] + str(member_number)
print("Badge code: ", badge_code)

print("\n=== Club badge ===")
print("Member: " + name)
print("Club: " + club)
print("Code: " + badge_code)
print("Points: " + str(points) + "| active: " + str(is_active))
