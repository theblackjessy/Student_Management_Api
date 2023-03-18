# Convert grade from percentage value to grade
def get_letter_grade(percent_grade):
    if percent_grade >= 90:
        return 'A'
    elif percent_grade < 90 and percent_grade >= 80:
        return 'B'
    elif percent_grade < 80 and percent_grade >= 70:
        return 'C'
    elif percent_grade < 70 and percent_grade >= 60:
        return 'D'
    elif percent_grade < 60 and percent_grade >= 50:
        return 'E'
    else:
        return 'F'
    
# Get GPA from the letter grade
def convert_grade_to_gpa(letter_grade):
    if letter_grade == 'A':
        return 5.0
    elif letter_grade == 'B':
        return 3.9
    elif letter_grade == 'C':
        return 2.9
    elif letter_grade == 'D':
        return 1.9
    else:
        return 0