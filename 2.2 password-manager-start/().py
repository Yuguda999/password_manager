# coding: utf-8
# import modules
import json
import pandas as pd
def Add_student():
    """The function adds student details and performance and stores it locally in a json file"""
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
# fetch the list of student statuses
try:
    with open('database.json', 'r') as data_file:
        data = json.load(data_file)
except FileNotFoundError:
    print('File does not Exist')
else:
    for name in data:
        print(f"{name}: {data[name][status]}")
# fetch the list of student statuses
try:
    with open('database.json', 'r') as data_file:
        data = json.load(data_file)
except FileNotFoundError:
    print('File does not Exist')
else:
    for name in data:
        print(f"{name}: {data[name]['Status']}")
# To Obtain a response from the script for any student to determine if they passed, failed, or need to retake the subject
try:
    with open('database.json', 'r') as data_file:
        data = json.load(data_file)
except FileNotFoundError:
    print('File does not Exist')
else:
    name_or_id = input("Enter student's name/id: ")
    for name in data:
        if result == name_or_id or data[name]['id'] == name_or_id:
            print(f"Name: {name}\nStatus: {data[name]['Status']}")
# To Obtain a response from the script for any student to determine if they passed, failed, or need to retake the subject
try:
    with open('database.json', 'r') as data_file:
        data = json.load(data_file)
except FileNotFoundError:
    print('File does not Exist')
else:
    name_or_id = input("Enter student's name/id: ")
    for name in data:
        if name == name_or_id or data[name]['id'] == name_or_id:
            print(f"Name: {name}\nStatus: {data[name]['Status']}")
try:
    with open('database.json', 'r') as data_file:
        data = json.load(data_file)
except FileNotFoundError:
    print('File does not Exist')
else:
    for name in data:
        print(data[name])
# Bonus Point
try:
    with open('database.json', 'r') as data_file:
        data = json.load(data_file)
except FileNotFoundError:
    print('File does not Exist')
else:
    for name in data:
        student_details_dict={
            'Name':name,
            'ID':data[name]['id'],
            'Chem Quiz':data[name]['quiz_scores']['chemistry'],
            'Bio Quiz':data[name]['quiz_scores']['biology'],
            'Phy Quiz':data[name]['quiz_scores']['physics'],
            'Math Quiz':data[name]['quiz_scores']['math'],
            'Chem HW':data[name]['homework']['chemistry'],
            'Bio HW':data[name]['homework']['biology'],
            'Phy HW':data[name]['homework']['physics'],
            'Math HW':data[name]['homework']['math'],
            'Chem Attnd':data[name]['class_attendance']['chemistry'],
            'Bio Attnd':data[name]['class_attendance']['biology'],
            'Phy Attnd':data[name]['class_attendance']['physics'],
            'Math Attnd':data[name]['class_attendance']['math'],
            'Chem Exam':data[name]['exam']['chemistry'],
            'Bio Exam':data[name]['exam']['biology'],
            'Phy Exam':data[name]['exam']['physics'],
            'Math Exam':data[name]['exam']['math'],
            'Chem AVG':data[name]['chem_avg'],
            'Bio AVG':data[name]['bio_avg'],
            'Phy AVG':data[name]['phy_avg'],
            'Math AVG':data[name]['math_avg'],
            'Avg Score':data[name]['Average Score'],
            'GPA':data[name]['GPA'],
            'Grade':data[name]['Grade'],
            'Status':data[name]['Status']
        }
print(student_details_dict)
# Bonus Point
try:
    with open('database.json', 'r') as data_file:
        data = json.load(data_file)
except FileNotFoundError:
    print('File does not Exist')
else:
    dictionary={}
    for name in data:
        student_details_dict={
            'Name':name,
            'ID':data[name]['id'],
            'Chem Quiz':data[name]['quiz_scores']['chemistry'],
            'Bio Quiz':data[name]['quiz_scores']['biology'],
            'Phy Quiz':data[name]['quiz_scores']['physics'],
            'Math Quiz':data[name]['quiz_scores']['math'],
            'Chem HW':data[name]['homework']['chemistry'],
            'Bio HW':data[name]['homework']['biology'],
            'Phy HW':data[name]['homework']['physics'],
            'Math HW':data[name]['homework']['math'],
            'Chem Attnd':data[name]['class_attendance']['chemistry'],
            'Bio Attnd':data[name]['class_attendance']['biology'],
            'Phy Attnd':data[name]['class_attendance']['physics'],
            'Math Attnd':data[name]['class_attendance']['math'],
            'Chem Exam':data[name]['exam']['chemistry'],
            'Bio Exam':data[name]['exam']['biology'],
            'Phy Exam':data[name]['exam']['physics'],
            'Math Exam':data[name]['exam']['math'],
            'Chem AVG':data[name]['chem_avg'],
            'Bio AVG':data[name]['bio_avg'],
            'Phy AVG':data[name]['phy_avg'],
            'Math AVG':data[name]['math_avg'],
            'Avg Score':data[name]['Average Score'],
            'GPA':data[name]['GPA'],
            'Grade':data[name]['Grade'],
            'Status':data[name]['Status']
        }
        dictionary.update(student_details_dict)
print(dictionary)
# import modules
import json
import pandas as pd
import csv
# Bonus Point
try:
    with open('database.json', 'r') as data_file:
        data = json.load(data_file)
except FileNotFoundError:
    print('File does not Exist')
else:
    dictionary={}
    for name in data:
        student_details_dict={
            'Name':name,
            'ID':data[name]['id'],
            'Chem Quiz':data[name]['quiz_scores']['chemistry'],
            'Bio Quiz':data[name]['quiz_scores']['biology'],
            'Phy Quiz':data[name]['quiz_scores']['physics'],
            'Math Quiz':data[name]['quiz_scores']['math'],
            'Chem HW':data[name]['homework']['chemistry'],
            'Bio HW':data[name]['homework']['biology'],
            'Phy HW':data[name]['homework']['physics'],
            'Math HW':data[name]['homework']['math'],
            'Chem Attnd':data[name]['class_attendance']['chemistry'],
            'Bio Attnd':data[name]['class_attendance']['biology'],
            'Phy Attnd':data[name]['class_attendance']['physics'],
            'Math Attnd':data[name]['class_attendance']['math'],
            'Chem Exam':data[name]['exam']['chemistry'],
            'Bio Exam':data[name]['exam']['biology'],
            'Phy Exam':data[name]['exam']['physics'],
            'Math Exam':data[name]['exam']['math'],
            'Chem AVG':data[name]['chem_avg'],
            'Bio AVG':data[name]['bio_avg'],
            'Phy AVG':data[name]['phy_avg'],
            'Math AVG':data[name]['math_avg'],
            'Avg Score':data[name]['Average Score'],
            'GPA':data[name]['GPA'],
            'Grade':data[name]['Grade'],
            'Status':data[name]['Status']
        }
        with open('data.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in student_details_dict.items():
                writer.writerow([key,value])
# Bonus Point
try:
    with open('database.json', 'r') as data_file:
        data = json.load(data_file)
except FileNotFoundError:
    print('File does not Exist')
else:
    dictionary={}
    for name in data:
        student_details_dict={
            'Name':name,
            'ID':data[name]['id'],
            'Chem Quiz':data[name]['quiz_scores']['chemistry'],
            'Bio Quiz':data[name]['quiz_scores']['biology'],
            'Phy Quiz':data[name]['quiz_scores']['physics'],
            'Math Quiz':data[name]['quiz_scores']['math'],
            'Chem HW':data[name]['homework']['chemistry'],
            'Bio HW':data[name]['homework']['biology'],
            'Phy HW':data[name]['homework']['physics'],
            'Math HW':data[name]['homework']['math'],
            'Chem Attnd':data[name]['class_attendance']['chemistry'],
            'Bio Attnd':data[name]['class_attendance']['biology'],
            'Phy Attnd':data[name]['class_attendance']['physics'],
            'Math Attnd':data[name]['class_attendance']['math'],
            'Chem Exam':data[name]['exam']['chemistry'],
            'Bio Exam':data[name]['exam']['biology'],
            'Phy Exam':data[name]['exam']['physics'],
            'Math Exam':data[name]['exam']['math'],
            'Chem AVG':data[name]['chem_avg'],
            'Bio AVG':data[name]['bio_avg'],
            'Phy AVG':data[name]['phy_avg'],
            'Math AVG':data[name]['math_avg'],
            'Avg Score':data[name]['Average Score'],
            'GPA':data[name]['GPA'],
            'Grade':data[name]['Grade'],
            'Status':data[name]['Status']
        }
        with open('data.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in student_details_dict:
                writer.writerow([key,value])
# Bonus Point
try:
    with open('database.json', 'r') as data_file:
        data = json.load(data_file)
except FileNotFoundError:
    print('File does not Exist')
else:
    dictionary={}
    for name in data:
        student_details_dict={
            'Name':name,
            'ID':data[name]['id'],
            'Chem Quiz':data[name]['quiz_scores']['chemistry'],
            'Bio Quiz':data[name]['quiz_scores']['biology'],
            'Phy Quiz':data[name]['quiz_scores']['physics'],
            'Math Quiz':data[name]['quiz_scores']['math'],
            'Chem HW':data[name]['homework']['chemistry'],
            'Bio HW':data[name]['homework']['biology'],
            'Phy HW':data[name]['homework']['physics'],
            'Math HW':data[name]['homework']['math'],
            'Chem Attnd':data[name]['class_attendance']['chemistry'],
            'Bio Attnd':data[name]['class_attendance']['biology'],
            'Phy Attnd':data[name]['class_attendance']['physics'],
            'Math Attnd':data[name]['class_attendance']['math'],
            'Chem Exam':data[name]['exam']['chemistry'],
            'Bio Exam':data[name]['exam']['biology'],
            'Phy Exam':data[name]['exam']['physics'],
            'Math Exam':data[name]['exam']['math'],
            'Chem AVG':data[name]['chem_avg'],
            'Bio AVG':data[name]['bio_avg'],
            'Phy AVG':data[name]['phy_avg'],
            'Math AVG':data[name]['math_avg'],
            'Avg Score':data[name]['Average Score'],
            'GPA':data[name]['GPA'],
            'Grade':data[name]['Grade'],
            'Status':data[name]['Status']
        }
        with open('data1.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in student_details_dict:
                writer.writerow([key,value])
# Bonus Point
try:
    with open('database.json', 'r') as data_file:
        data = json.load(data_file)
except FileNotFoundError:
    print('File does not Exist')
else:
    dictionary={}
    for name in data:
        lst = [name]
        student_details_dict=[
            name,
          data[name]['id'],
    data[name]['quiz_scores']['chemistry'],
   data[name]['quiz_scores']['biology'],
   data[name]['quiz_scores']['physics'],
    data[name]['quiz_scores']['math'],
  data[name]['homework']['chemistry'],
 data[name]['homework']['biology'],
 data[name]['homework']['physics'],
  data[name]['homework']['math'],
     data[name]['class_attendance']['chemistry'],
    data[name]['class_attendance']['biology'],
    data[name]['class_attendance']['physics'],
     data[name]['class_attendance']['math'],
    data[name]['exam']['chemistry'],
   data[name]['exam']['biology'],
   data[name]['exam']['physics'],
    data[name]['exam']['math'],
   data[name]['chem_avg'],
  data[name]['bio_avg'],
  data[name]['phy_avg'],
   data[name]['math_avg'],
    data[name]['Average Score']data[name]['GPA'],
data[name]['Grade'],
 data[name]['Status']
            ]
#         with open('data1.csv', 'a') as csv_file:
#             writer = csv.writer(csv_file)
#             for key, value in student_details_dict:
#                 writer.writerow([key,value])
            
# Bonus Point
try:
    with open('database.json', 'r') as data_file:
        data = json.load(data_file)
except FileNotFoundError:
    print('File does not Exist')
else:
    dictionary={}
    for name in data:
        lst = [name]
        student_details_dict=[
            name,
            data[name]['id'],
            data[name]['quiz_scores']['chemistry'],
            data[name]['quiz_scores']['biology'],
            data[name]['quiz_scores']['physics'],
            data[name]['quiz_scores']['math'],
            data[name]['homework']['chemistry'],
            data[name]['homework']['biology'],
            data[name]['homework']['physics'],
            data[name]['homework']['math'],
            data[name]['class_attendance']['chemistry'],
            data[name]['class_attendance']['biology'],
            data[name]['class_attendance']['physics'],
            data[name]['class_attendance']['math'],
            data[name]['exam']['chemistry'],
            data[name]['exam']['biology'],
            data[name]['exam']['physics'],
            data[name]['exam']['math'],
            data[name]['chem_avg'],
            data[name]['bio_avg'],
            data[name]['phy_avg'],
            data[name]['math_avg'],
            data[name]['Average Score'],
            data[name]['GPA'],
            data[name]['Grade'],
            data[name]['Status']
            ]
#         with open('data1.csv', 'a') as csv_file:
#             writer = csv.writer(csv_file)
#             for key, value in student_details_dict:
#                 writer.writerow([key,value])
            
# Bonus Point
# reading the json filr
try:
    with open('database.json', 'r') as data_file:
        data = json.load(data_file)
except FileNotFoundError:
    print('File does not Exist')
else:
    # creating a header and values for the dataframe
    header= ['Name','ID','Cem Quiz','Bio Quiz','Phy Quiz','Mth Quiz','Chem HW','Bio HW','Phy HW',
             'Math HW','Chem Attnd','Bio Attnd','Phy Attnd','Math Attnd','Chem Exam','Bio Exam',
             'Phy Exam','Math Exam','Chem AVG','Bio AVG',   'Phy AVG',  'Math AVG', 'Avg Score',
             'GPA','Grade','Status']
    values=[]
    #looping through to fetch needed data from the json file
    for name in data:
        student_details_list=[
            name,
            data[name]['id'],
            data[name]['quiz_scores']['chemistry'],
            data[name]['quiz_scores']['biology'],
            data[name]['quiz_scores']['physics'],
            data[name]['quiz_scores']['math'],
            data[name]['homework']['chemistry'],
            data[name]['homework']['biology'],
            data[name]['homework']['physics'],
            data[name]['homework']['math'],
            data[name]['class_attendance']['chemistry'],
            data[name]['class_attendance']['biology'],
            data[name]['class_attendance']['physics'],
            data[name]['class_attendance']['math'],
            data[name]['exam']['chemistry'],
            data[name]['exam']['biology'],
            data[name]['exam']['physics'],
            data[name]['exam']['math'],
            data[name]['chem_avg'],
            data[name]['bio_avg'],
            data[name]['phy_avg'],
            data[name]['math_avg'],
            data[name]['Average Score'],
            data[name]['GPA'],
            data[name]['Grade'],
            data[name]['Status']
            ]
        values.append(student_details_list)
# to create the dataframe
df = pd.DataFrame(values, columns = headers)
print(df)
# to create the dataframe
df = pd.DataFrame(values, columns = header)
print(df)
# to save data to csv or excel package
def Save():
    print('save as:\n1. csv\2. excel')
    choice = input('save file as(1/2): ')
    file_name= input('Enter file name: ')
    if choice == 1:
        df.to_csv(f'{file_name}.csv')
    elif choice == 2:
        df.to_excel(f'{file_name}.xlsx')
    
