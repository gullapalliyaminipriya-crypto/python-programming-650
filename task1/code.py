print("HOSPITAL BILLING SYSTEM")

consultation = float(input("Enter consultation charges: "))
diagnostic = float(input("Enter diagnostic charges: "))
treatment = float(input("Enter treatment charges: "))

eligible = input("Eligible for concession (yes/no): ").lower()

if consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid charges")

elif eligible not in ["yes", "no"]:
    print("Invalid concession choice")

else:
    total = consultation + diagnostic + treatment

    if eligible == "yes":
        discount = total * 0.10
    else:
        discount = 0

    final_bill = total - discount

    if final_bill < 1000:
        category = "Low Payment"
    elif final_bill <= 5000:
        category = "Medium Payment"
    else:
        category = "High Payment"

    print("\n----- BILL DETAILS -----")
    print("Total Bill:", total)
    print("Discount:", discount)
    print("Final Bill:", final_bill)
    print("Patient Classification:", category)
