# Laboratory 1 - Installment 2
# Author: Lauren Mark F. Dela Torre
# A simple expense tracker

print("=" * 40)
print("\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

print("\nMAIN MENU")
print("\t[1] Add an expense\t(coming soon)")
print("\t[2] View all expenses\t(coming soon)")
print("\t[3] Show total spent\t(coming soon)")
print("\t[4] Exit\t\t(coming soon)")

print()
name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

print()
item1 = input("First expense? ")
amount1 = float(input("Amount? "))

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

total = amount1 + amount2
average = total / 2

print()
print("-" * 40)
print("SUMMARY")
print(f"\t- {item1}:\t${amount1}")
print(f"\t- {item2}:\t${amount2}")
print(f"Total spent:\t${total}")
print(f"Average:\t${average}")
print("-" * 40)

print(f"Made by: Lauren Mark F. Dela Torre | Installment 2")