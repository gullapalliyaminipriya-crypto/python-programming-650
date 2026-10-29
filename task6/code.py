
def analyze_identifier(identifier):
    valid_branches = ["CSE", "ECE", "AIM", "EEE"]

    identifier = identifier.strip().upper()

    # Validate length
    if len(identifier) != 9:
        return None

    year_code = identifier[0:2]
    branch_code = identifier[2:5]
    student_number = identifier[5:9]

    # Validate year and student number
    if not year_code.isdigit() or not student_number.isdigit():
        return None

    # Validate branch
    if branch_code not in valid_branches:
        return None

    admission_year = 2000 + int(year_code)

    return {
        "identifier": identifier,
        "year": admission_year,
        "branch": branch_code,
        "student_number": student_number
    }


def main():
    try:
        n = int(input("Enter number of student records: "))

        if n <= 0:
            print("Error: Number of records must be positive.")
            return

        records = []
        branch_groups = {}
        year_groups = {}

        for i in range(n):
            identifier = input(
                f"Enter registration ID {i + 1}: "
            )

            student = analyze_identifier(identifier)

            if student is None:
                print("Invalid identifier:", identifier)
                continue

            records.append(student)

            branch = student["branch"]
            year = student["year"]

            branch_groups.setdefault(branch, []).append(
                student["identifier"]
            )
            year_groups.setdefault(year, []).append(
                student["identifier"]
            )

            print("Valid identifier")
            print("Admission Year:", year)
            print("Branch:", branch)
            print("Student Number:", student["student_number"])
            print()

        print("\n--- Branch Classification ---")
        for branch, ids in sorted(branch_groups.items()):
            print(branch, ":", ", ".join(ids))

        print("\n--- Admission Year Classification ---")
        for year, ids in sorted(year_groups.items()):
            print(year, ":", ", ".join(ids))

        print("\nTotal valid records:", len(records))
        print("Total invalid records:", n - len(records))

    except ValueError:
        print("Error: Please enter a valid integer for record count.")


if __name__ == "__main__":
    main()

