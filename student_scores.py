student_scores = input("Enter student scores: ").split()
highest_score = 0
highest_index = -1
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
for k in range (0, len(student_scores)):
    if student_scores[k] > highest_score:
        highest_score = student_scores[k]
        highest_index = student_scores.index(highest_score)
print(student_scores)
print(f"Highest Score: {highest_score}, Highest Index: {highest_index}")