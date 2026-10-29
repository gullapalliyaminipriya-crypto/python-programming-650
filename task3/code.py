
capacity = float(input("Enter tank capacity: "))
level = float(input("Enter initial water level: "))
threshold = float(input("Enter threshold level: "))
days = int(input("Enter number of days: "))

first_day = -1

for day in range(1, days + 1):
    inflow = float(input(f"Day {day} inflow: "))
    outflow = float(input(f"Day {day} outflow: "))

    level = level + inflow - outflow

    if level > capacity:
        print("Overflow detected!")
        level = capacity

    if level < 0:
        print("Water shortage detected!")
        level = 0

    print(f"Day {day} water level: {level:.2f}")

    if level >= threshold and first_day == -1:
        first_day = day

if first_day != -1:
    print("Threshold first reached on day:", first_day)
else:
    print("Threshold was not reached.")

print("Final water level:", f"{level:.2f}")

