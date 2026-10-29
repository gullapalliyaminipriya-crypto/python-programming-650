
n = int(input("Enter number of subjects: "))
max_grace = int(input("Enter maximum grace marks per subject: "))

subjects = []
total = 0
maximum_total = 0
all_passed = True

for i in range(n):
    print("\nSubject", i + 1)
    name = input("Enter subject name: ")
    maximum = int(input("Enter maximum marks: "))
    marks = int(input("Enter obtained marks: "))
    pass_marks = int(input("Enter pass marks: "))

    grace = 0

    if marks < pass_marks:
        required = pass_marks - marks

        if required <= max_grace and marks + required <= maximum:
            grace = required

    final_marks = min(marks + grace, maximum)

    if final_marks < pass_marks:
        all_passed = False

    total += final_marks
    maximum_total += maximum

    subjects.append((name, marks, grace, final_marks))

print("\n--- Examination Result ---")

for name, marks, grace, final_marks in subjects:
    print(name, ": Original =", marks,
          ", Grace =", grace,
          ", Final =", final_marks)

percentage = (total / maximum_total) * 100

print("\nTotal Marks:", total, "/", maximum_total)
print("Percentage:", round(percentage, 2), "%")

if not all_passed:
    print("Classification: FAIL")
elif percentage >= 75:
    print("Classification: DISTINCTION")
elif percentage >= 60:
    print("Classification: FIRST CLASS")
elif percentage >= 50:
    print("Classification: SECOND CLASS")
else:
    print("Classification: PASS")

