# Grade Calculator


def grade_calculator(name, portfolio_grade, poster_grade, exam_grade):
    """
    Input:
        name: student's name (string)
        portfolio_grade: student's code portfolio grade (positive int)
        poster_grade: student's poster presentation grade (positive int)
        exam_grade: student's final exam grade (positive int)
    Returns:
        Students name (string) and final grade (positive float)
    """
    final_grade = poster_grade*0.3 + portfolio_grade*0.4 + exam_grade*0.3

    return name, final_grade

# example
result = grade_calculator("John Wick", 82, 96, 79)

student_name = result[0]
final_mark = result[1]

print(student_name, final_mark)