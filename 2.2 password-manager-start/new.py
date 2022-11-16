import json

categories = ['quiz_scores', 'homework', 'class_attendance', 'exam']
name = input('Student Name:')
id = input("Enter student's ID: ")

# creating a dictionary container to hold student details
student_details = {name: {'id': id}}

# getting the totals of all subject to compute the average of each subject
chem_total = 0
bio_total = 0
phy_total = 0
mth_total = 0
total_score = 576

# setting initial average score for each category
Attendance_avg = 0
Quiz_avg = 0
Homework_avg = 0
Exam_avg = 0

# looping through each category to enter scores for each subject
for category in categories:
    print(f'Enter Scores for {category}')
    chem = int(input('Enter Chemistry Score: '))
    chem_total += chem

    bio = int(input('Enter Biology Score: '))
    bio_total += bio

    phy = int(input('Enter Physics Score: '))
    phy_total += phy

    mth = int(input('Enter Mathematics Score: '))
    mth_total += mth
    print('\n')

    # computing total score for each category
    if category == 'quiz_scores':
        Quiz_avg = ((chem+bio+phy+mth) * 30)/(4*190)
    elif category == 'homework':
        Homework_avg = ((chem+bio+phy+mth) * 15)/(4*190)
    elif category == 'class_attendance':
        Attendance_avg = ((chem+bio+phy+mth) * 12)/(4*96)
    elif category == 'exam':
        Exam_avg = ((chem+bio+phy+mth) * 43)/(4*100)

    # container for each categories
    new_category={'chemistry': chem,
             'biology': bio,
             'physics': phy,
             'math': mth}

    # appending each category to the student details container
    student_details[name][category] = new_category

# adding average scores of each student to student details container
student_details[name]['chem_avg'] = round(((chem_total/total_score)*100), 2)
student_details[name]['bio_avg'] = round(((bio_total/total_score)*100), 2)
student_details[name]['phy_avg'] = round(((phy_total/total_score)*100), 2)
student_details[name]['math_avg'] = round(((mth_total/total_score)*100), 2)

# computing average, gpa, grade and status
Average = round((Attendance_avg + Quiz_avg + Homework_avg + Exam_avg), 2)
GPA = round(((Average/100) * 5), 1)

# grade logic
grade = ''
if Average >= 90:
    grade = 'A'
elif Average >= 75:
    grade = 'B'
elif Average >= 65:
    grade = 'C'
elif Average >= 55:
    grade = 'D'
elif Average >= 50:
    grade = 'E'
elif Average <= 50:
    grade = 'F'

# status logic
status = ''
if grade == 'A' or grade == 'B' or grade == 'C' or grade == 'D':
    status = 'Pass'
elif grade == 'F':
    status = 'Fail'
elif grade == 'E':
    status = 'Retake'

# Adding average, grade, gpa and status to student details container
student_details[name]['Average Score'] = Average
student_details[name]['GPA'] = GPA
student_details[name]['Grade'] = grade
student_details[name]['Status'] = status


# STORING STUDENTS DETAILS TO A JSON FILE
try:
    with open('database.json', 'r') as data_file:
        data = json.load(data_file)
        data.update(student_details)

except FileNotFoundError:
    with open('database.json', 'w') as data_file:
        json.dump(student_details, data_file, indent=4)
else:
    with open('database.json', 'w') as data_file:
        json.dump(data, data_file, indent=4)

#SCRIPT UTILITY
