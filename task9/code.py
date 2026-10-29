
# Railway Fare and Reservation Calculator

def calculate_basic_fare(distance):
    if distance <= 100:
        return 100
    elif distance <= 300:
        return 250
    elif distance <= 500:
        return 400
    else:
        return 600


def calculate_concession(age, fare):
    if age < 12:
        return fare * 0.50
    elif age >= 60:
        return fare * 0.20
    else:
        return 0


def main():
    n = int(input("Enter number of passengers: "))

    if n <= 0:
        print("Invalid number of passengers.")
        return

    total_payable = 0

    class_rates = {
        "Sleeper": 1.0,
        "AC3": 1.8,
        "AC2": 2.5
    }

    reservation_fee = 40
    cancellation_rate = 0.25

    for i in range(1, n + 1):
        print(f"\nPassenger {i}")

        name = input("Enter passenger name: ")
        age = int(input("Enter age: "))
        distance = float(input("Enter distance in km: "))
        travel_class = input(
            "Enter class (Sleeper/AC3/AC2): "
        ).strip()

        reserved = input(
            "Reservation required? (yes/no): "
        ).strip().lower()

        cancelled = input(
            "Ticket cancelled? (yes/no): "
        ).strip().lower()

        if age < 0 or distance <= 0:
            print("Invalid age or distance. Skipping passenger.")
            continue

        if travel_class not in class_rates:
            print("Invalid travel class. Skipping passenger.")
            continue

        if reserved not in ("yes", "no") or cancelled not in ("yes", "no"):
            print("Invalid reservation status. Skipping passenger.")
            continue

        # Calculate fare
        basic_fare = calculate_basic_fare(distance)
        class_fare = basic_fare * class_rates[travel_class]
        concession = calculate_concession(age, class_fare)
        discounted_fare = class_fare - concession

        fee = reservation_fee if reserved == "yes" else 0
        total_fare = discounted_fare + fee

        if cancelled == "yes":
            penalty = total_fare * cancellation_rate
            refund = total_fare - penalty
            payable = penalty
        else:
            penalty = 0
            refund = 0
            payable = total_fare

        total_payable += payable

        print("\n--- Fare Details ---")
        print("Passenger Name:", name)
        print(f"Basic Fare: Rs. {basic_fare:.2f}")
        print(f"Class Fare: Rs. {class_fare:.2f}")
        print(f"Age Concession: Rs. {concession:.2f}")
        print(f"Reservation Fee: Rs. {fee:.2f}")
        print(f"Total Fare: Rs. {total_fare:.2f}")
        print(f"Cancellation Penalty: Rs. {penalty:.2f}")
        print(f"Refund Amount: Rs. {refund:.2f}")
        print(f"Final Payable Amount: Rs. {payable:.2f}")

    print("\n==============================")
    print(f"Total Payable: Rs. {total_payable:.2f}")
    print("==============================")


if __name__ == "__main__":
    main()

