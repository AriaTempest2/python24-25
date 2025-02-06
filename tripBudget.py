print("Welcome to The Budget Calculator")
budget = "$6000"
print(f"Your budget is {budget}")

airfare = int(input("Enter the airfare for each passenger: ")) * 4
days = int(input("Enter the amount of days you'll be away: "))
food = (int(input("enter the daily food budget per person: ")) * 4) * days
excursion = int(input("Enter the total cost for excursions: "))
souvenirs = int(input("Enter the total budget for souvenirs: "))

print(f"Airfare: ${airfare}")
print(f"Food: ${food}")
print(f"Excursions: ${excursion}")
print(f"Souvenirs: ${souvenirs}")
total = airfare + food + excursion + souvenirs
print(f"Total: ${total}")
if total <= 6000:
    print(f"Your trip is in budget! you have ${6000 - total} left over")
else:
    print(f"You're out of budget! Reduce your spending by ${total - 6000}")