sugar_per_cookie = 1.5 / 48
butter_per_cookie = 1 / 48
flour_per_cookie = 2.75 / 48

cookies = int(input("Enter the number of cookies"))

sugar_needed = cookies * sugar_per_cookie
butter_needed = cookies * butter_per_cookie
flour_needed = cookies * flour_per_cookie

print("Ingredients Needed")
print("______________________")  # for underlining
print("Sugar:", sugar_needed, "cups")
print("Butter:", butter_needed)
print("Flour:", flour_needed)
