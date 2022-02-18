student_name = input("Enter students name: ")
degree_name = input("Enter the degree program: ")
credits_degree = float(input("Enter total credits: "))
credits_taken = float(input("Enter credits taken: "))

credits_left = credits_degree - credits_taken

print("Degree Program:", degree_name)
print("Student Name:", student_name)
print("Credits Left:", credits_left)
