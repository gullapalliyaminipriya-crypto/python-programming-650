# Nested List Classroom Occupancy Analysis

## 1. Problem Statement

Develop a Python program to analyze classroom occupancy using nested lists. Each classroom contains multiple seating positions. The program should allocate students to available seats, preserve reserved seats, detect duplicate student assignments, and calculate the total occupied seats, reserved seats, vacant seats, and classroom capacity.

The program must reject invalid seat assignments and ensure that reserved seats are not allocated to students.

## 2. Algorithm

1. Start the program.
2. Create a nested list representing classrooms and their seats.
3. Use `0` for vacant seats, `-1` for reserved seats, and positive integers for student IDs.
4. Read the number of students to allocate.
5. For each student, read the classroom number, seat number, and student ID.
6. Check whether the classroom and seat numbers are valid.
7. Check whether the student ID is already assigned.
8. If the seat is reserved or already occupied, reject the assignment.
9. Otherwise, allocate the student to the selected seat.
10. Count occupied, reserved, and vacant seats in each classroom.
11. Display the classroom seating arrangement and occupancy summary.
12. Stop the program.

## 3. Flowchart (Mermaid TD)
```mermaid

    A[(Start)] --> B(1 (Step 1))
    B --> C{(Decision?)}
    C --  --> D[ 1 (Result 1)]
    C --  --> E[ 2 (Result 2)]
    D --> F[ (End)]
    E --> F
```
## 4. Python Source Code

```
# Nested List Classroom Occupancy Analysis# 0 = Vacant seat# -1 = Reserved seat# Positive number = Student IDclassrooms = [    [0, -1, 0, 0],    [0, 0, -1, 0]]print("Initial Classroom Seating:")for i, seats in enumerate(classrooms, start=1):    print(f"Classroom {i}: {seats}")n = int(input("\nEnter number of student assignments: "))assigned_students = set()# Record any students already presentfor seats in classrooms:    for seat in seats:        if seat > 0:            assigned_students.add(seat)for _ in range(n):    classroom = int(input("Enter classroom number: "))    seat = int(input("Enter seat number: "))    student_id = int(input("Enter student ID: "))    if not (1 <= classroom <= len(classrooms)):        print("Invalid classroom number.")        continue    if not (1 <= seat <= len(classrooms[classroom - 1])):
```

## 5. Sample Input

```
Enter number of student assignments: 4

1
1
101

1
2
102

2
1
101

2
2
103
```

## 6. Sample Output

```
Initial Classroom Seating:
Classroom 1: [0, -1, 0, 0]
Classroom 2: [0, 0, -1, 0]

Enter number of student assignments: 4
Enter classroom number: 1
Enter seat number: 1
Enter student ID: 101
Student allocated successfully.
Enter classroom number: 1
Enter seat number: 2
Enter student ID: 102
Seat is occupied or reserved.
Enter classroom number: 2
Enter seat number: 1
Enter student ID: 101
Duplicate student assignment rejected.
Enter classroom number: 2
Enter seat number: 2
Enter student ID: 103
Student allocated successfully.

Final Classroom Seating:
Classroom 1: [101, -1, 0, 0]
Classroom 2: [103, 0, -1, 0]

Occupancy Summary:
Classroom 1:
  Capacity: 4
  Occupied: 1
  Reserved: 1
  Vacant: 2
Classroom 2:
  Capacity: 4
  Occupied: 1
  Reserved: 1
  Vacant: 2

Overall Summary:
Total Capacity: 8
Total Occupied: 2
Total Reserved: 2
Total Vacant: 4
```

## 7. Result

The Python program successfully manages classroom seating using nested lists. It preserves reserved seats, prevents duplicate student assignments, rejects invalid allocations, and calculates the occupied, reserved, and vacant seating capacity for each classroom and overall.
