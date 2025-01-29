import pandas as pd

data = {
    "Math": [85, 78, 92, 60, 74, 88],
    "Science": [80, 82, 89, 65, 70, 90],
    "English": [75, 85, 78, 55, 72, 88],
    "History": [70, 75, 80, 50, 68, 82]
}
students = ["Student 1", "Student 2", "Student 3", "Student 4", "Student 5", "Student 6"]
exam_scores = pd.DataFrame(data, index=students)

# 1. Display the first three rows of the exam_scores DataFrame
print(exam_scores.head(3)),

# 2. Get the total number of students and subjects recorded in the DataFrame
total_students = len(exam_scores)
total_subjects = len(exam_scores.columns)
print(f"Total students: {total_students}, Total subjects: {total_subjects}")

# 3. List all subject names and student names
subject_names = exam_scores.columns.tolist()
student_names = exam_scores.index.tolist()
print("Subjects:", subject_names)
print("Students:", student_names)

# 4. Display the data type of each column in the DataFrame
print(exam_scores.dtypes)

# 5. Check if there are any missing values in the DataFrame
print(exam_scores.isnull().sum())

# 6. Retrieve the scores of "Student 3" in all subjects
student_3_scores = exam_scores.loc["Student 3"]
print("Student 3 scores:", student_3_scores)

# 7. Extract the scores of all students in "Math"
math_scores = exam_scores["Math"]
print("Math scores:", math_scores)

# 8. Retrieve the scores of "Student 1" and "Student 4" in "Science" and "English"
scores_student_1_4 = exam_scores.loc[["Student 1", "Student 4"], ["Science", "English"]]
print("Scores of Student 1 and Student 4 in Science and English:")
print(scores_student_1_4)

# 9. Slice the DataFrame to get the first 4 students and the first 3 subjects
subset = exam_scores.iloc[:4, :3]
print("Subset of first 4 students and 3 subjects:")
print(subset)

# 10. Retrieve the score of "Student 5" in "History" using .loc or .iloc
student_5_history_score = exam_scores.loc["Student 5", "History"]
print("Student 5 score in History:", student_5_history_score)

# 11. Update the score of "Student 2" in "Math" to 85
exam_scores.loc["Student 2", "Math"] = 85
print("Updated exam scores:")
print(exam_scores)

# 12. Add a new student, "Student 7", with scores [90, 85, 88, 80] for all subjects
exam_scores.loc["Student 7"] = [90, 85, 88, 80]
print("Exam scores with new student added:")
print(exam_scores)

# 13. Add 5 bonus marks to all students' scores
exam_scores += 5
print("Exam scores after adding 5 bonus marks:")
print(exam_scores)

# 14. Deduct 3 marks from the scores of "Student 4" in all subjects
exam_scores.loc["Student 4"] -= 3
print("Exam scores after deducting 3 marks from Student 4:")
print(exam_scores)

# 15. Calculate the percentage of marks obtained by each student, assuming each subject has a maximum of 100 marks
total_marks_per_student = exam_scores.sum(axis=1)
percentage_per_student = (total_marks_per_student / (100 * len(exam_scores.columns))) * 100
print("Percentage of marks for each student:")
print(percentage_per_student)

# 16. Calculate the total marks obtained by each student
print("Total marks obtained by each student:")
print(total_marks_per_student)

# 17. Determine the total marks scored in each subject
total_marks_per_subject = exam_scores.sum(axis=0)
print("Total marks scored in each subject:")
print(total_marks_per_subject)

# 18. Identify the student with the highest total marks
highest_total_marks_student = total_marks_per_student.idxmax()
print("Student with the highest total marks:", highest_total_marks_student)

# 19. Find the subject with the lowest total marks
lowest_total_marks_subject = total_marks_per_subject.idxmin()
print("Subject with the lowest total marks:", lowest_total_marks_subject)

# 20. Compute the average marks scored by each student across all subjects
average_marks_per_student = exam_scores.mean(axis=1)
print("Average marks scored by each student:")
print(average_marks_per_student)
