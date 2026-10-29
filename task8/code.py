
# Smart Campus Incident and Maintenance Prioritization

incidents = []

severity_values = {
    "high": 3,
    "medium": 2,
    "low": 1
}

n = int(input("Enter number of incidents: "))

for i in range(n):
    print(f"\nEnter details for Incident {i + 1}")

    incident_id = input("Incident ID: ")
    description = input("Description: ")
    location = input("Location: ")

    severity = input(
        "Severity (High/Medium/Low): "
    ).strip().lower()

    while severity not in severity_values:
        print("Invalid severity! Enter High, Medium, or Low.")
        severity = input("Severity: ").strip().lower()

    frequency = int(input("Reported frequency: "))

    while frequency < 0:
        print("Frequency cannot be negative.")
        frequency = int(input("Reported frequency: "))

    severity_score = severity_values[severity]
    score = (severity_score * 10) + (frequency * 2)

    if score >= 35:
        priority = "High"
    elif score >= 20:
        priority = "Medium"
    else:
        priority = "Low"

    incidents.append([
        incident_id,
        description,
        location,
        severity.title(),
        frequency,
        score,
        priority
    ])

# Sort incidents by score in descending order
incidents.sort(key=lambda x: x[5], reverse=True)

print("\n--- RANKED INCIDENT REPORT ---")
print("-" * 100)
print(f"{'ID':<8}{'Description':<23}{'Location':<16}"
      f"{'Severity':<12}{'Frequency':<12}"
      f"{'Score':<8}{'Priority'}")
print("-" * 100)

for incident in incidents:
    print(f"{incident[0]:<8}{incident[1]:<23}"
          f"{incident[2]:<16}{incident[3]:<12}"
          f"{incident[4]:<12}{incident[5]:<8}"
          f"{incident[6]}")

# Generate priority summary
high_count = sum(1 for x in incidents if x[6] == "High")
medium_count = sum(1 for x in incidents if x[6] == "Medium")
low_count = sum(1 for x in incidents if x[6] == "Low")

print("\n--- PRIORITY SUMMARY ---")
print("Total incidents:", len(incidents))
print("High priority:", high_count)
print("Medium priority:", medium_count)
print("Low priority:", low_count)

