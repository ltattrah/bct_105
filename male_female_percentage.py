# input
males = int(input("Enter the number of males: "))
females = int(input("Enter the number of females: "))

total_number = males + females

male_percentage = (males / total_number) * 100
female_percentage = (females / total_number) * 100

# print("Percentage of males:", male_percentage, "%")
print(f"Percentage of males: {male_percentage:.2f} %")

print("Percentage of females:", female_percentage, "%")
