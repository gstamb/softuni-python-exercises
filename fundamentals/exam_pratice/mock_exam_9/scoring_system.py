students = int(input())
lectures = int(input())
bonus = int(input())
max_bonus = [0]
lectures_attended = [0]
for student in range(students):
    attended = int(input())
    if lectures == 0:
        continue
    else:
        current_bonus = attended / lectures * (5 + bonus)
        max_bonus.append(current_bonus)
        lectures_attended.append(attended)

print(f"Max Bonus: {max(max_bonus):.0f}.")
print(f"The student has attended {max(lectures_attended)} lectures.")
