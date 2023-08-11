student_scores={
    "harry":81,
    "Ron":78,
    "hermoine":99,
    "braco":74,
    "neville":62,
}


student_grades={}
for student in student_scores:
    if student_scores[student]>90:
        student_grades[student]="Outstanding"
    elif student_scores[student]>80:
        student_grades[student]="goodexceeds expectations"
    elif student_scores[student]>70:
        student_grades[student]="Acceptable"

    else:
        student_grades[student]="Fail"







print(student_grades)