current_exams = {}
exam_results = {}
while True:
    exam = input()
    if exam == "end of contests":
        break
    # else
    exam, password = exam.split(":")
    current_exams[exam] = password

while True:
    submission = input()
    if submission == "end of submissions":
        break

    contest, password, user, score = submission.split("=>")
    if contest in current_exams:
        if password == current_exams[contest]:
            if user in exam_results:
                if contest in exam_results[user]:
                    old_score = exam_results[user][contest]
                    if old_score < int(score):
                        exam_results[user][contest] = int(score)
                else:
                    exam_results[user][contest] = int(score)
            else:
                exam_results[user] = {contest: int(score)}

best_result = ("", -99999)
for user, score in exam_results.items():
    total_score = sum(score.values())
    if best_result[1] < total_score:
        best_result = (user, total_score)

print(f"Best candidate is {best_result[0]} with total {best_result[1]} points.")
print("Ranking:")
for user, score in sorted(exam_results.items()):
    print(user)
    for exam, points in sorted(score.items(), key=lambda item: item[1], reverse=True):
        print(f"#  {exam} -> {points}")
