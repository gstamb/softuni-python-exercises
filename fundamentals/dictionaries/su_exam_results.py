exam_results = {}

while True:
    entry = input()
    if entry == "exam finished":
        break

    if entry.find("banned") == -1:
        name, language, score = entry.split("-")
        if language not in exam_results:
            exam_results[language] = []
            entry = f"{name} | {int(score)}"
            exam_results[language].append(entry)
        else:
            existing = [x for x in exam_results[language] if x.startswith(name)]
            if existing:
                old_score = int(existing[0].split(" | ")[1])
                if old_score > int(score):
                    entry = ""
                    exam_results[language].append(entry)
                else:
                    index = exam_results[language].index(existing[0])
                    exam_results[language][index] = ""
                    entry = f"{name} | {int(score)}"
                    exam_results[language].append(entry)
            else:
                entry = f"{name} | {int(score)}"
                exam_results[language].append(entry)
    else:
        name, _ = entry.split("-")
        for language, score in exam_results.items():
            for index, student in enumerate(score):
                if student.startswith(name):
                    exam_results[language][index] = ""

result = "Results:\n"
for language, exam_score in exam_results.items():
    for index, student in enumerate(exam_score):
        if student != "":
            result += f"{student}\n"
result += "Submissions:\n"
for language, exam_score in exam_results.items():
    result += f"{language} - {len(exam_score)}\n"
print(result)
