full_name = input("Enter your full name (First, Middle, Last): ")

first, middle, last = full_name.split(",")

first = first.strip().capitalize()
middle = middle.strip().capitalize()
last = last.strip().title()  # For names like "dela cruz"

middle_initial = middle[0].upper() + "."

formatted_name = f"{last}, {first} {middle_initial}"

print(f"Formatted Name: {formatted_name}")
