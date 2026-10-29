
# Nested List Classroom Occupancy Analysis

# 0 = Vacant seat
# -1 = Reserved seat
# Positive number = Student ID

classrooms = [
    [0, -1, 0, 0],
    [0, 0, -1, 0]
]

print("Initial Classroom Seating:")
for i, seats in enumerate(classrooms, start=1):
    print(f"Classroom {i}: {seats}")

n = int(input("\nEnter number of student assignments: "))

assigned_students = set()

# Record any students already present
for seats in classrooms:
    for seat in seats:
        if seat > 0:
            assigned_students.add(seat)

for _ in range(n):
    classroom = int(input("Enter classroom number: "))
    seat = int(input("Enter seat number: "))
    student_id = int(input("Enter student ID: "))

    if not (1 <= classroom <= len(classrooms)):
        print("Invalid classroom number.")
        continue

    if not (1 <= seat <= len(classrooms[classroom - 1])):
        print("Invalid seat number.")
        continue

    if student_id <= 0:
        print("Invalid student ID.")
        continue

    if student_id in assigned_students:
        print("Duplicate student assignment rejected.")
        continue

    if classrooms[classroom - 1][seat - 1] != 0:
        print("Seat is occupied or reserved.")
        continue

    classrooms[classroom - 1][seat - 1] = student_id
    assigned_students.add(student_id)
    print("Student allocated successfully.")

# Display final seating arrangement
print("\nFinal Classroom Seating:")
for i, seats in enumerate(classrooms, start=1):
    print(f"Classroom {i}: {seats}")

# Calculate occupancy summary
total_capacity = 0
total_occupied = 0
total_reserved = 0
total_vacant = 0

print("\nOccupancy Summary:")
for i, seats in enumerate(classrooms, start=1):
    occupied = sum(1 for seat in seats if seat > 0)
    reserved = seats.count(-1)
    vacant = seats.count(0)
    capacity = len(seats)

    total_capacity += capacity
    total_occupied += occupied
    total_reserved += reserved
    total_vacant += vacant

    print(f"Classroom {i}:")
    print(f"  Capacity: {capacity}")
    print(f"  Occupied: {occupied}")
    print(f"  Reserved: {reserved}")
    print(f"  Vacant: {vacant}")

print("\nOverall Summary:")
print("Total Capacity:", total_capacity)
print("Total Occupied:", total_occupied)
print("Total Reserved:", total_reserved)
print("Total Vacant:", total_vacant)

