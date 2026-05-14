def add_grade(st_grade_list, st_name, st_subject, st_grade):
    student_grade_dict = {
        'Name': st_name,
        'Subject': st_subject,
        'Grade': st_grade
    }
    st_grade_list.append(student_grade_dict)
    with open ('student_record.txt', 'a') as student_records:
        student_records.write(f'\n{name}|{subject}|{grade}')
    print('Student Record Recorded Successfully!')

def view_all_grades(st_grade_list):
    if not st_grade_list:
        print('No Records yet!')
    else:
        for student_grade in st_grade_list:
            print(f'{student_grade['Name']}|{student_grade['Subject']}|{student_grade['Grade']}')

def search_student(st_grade_list, search_student):
    for list_of_student_record in st_grade_list:
        if search_student in list_of_student_record['Name']:
            print(f'{list_of_student_record['Name']}|{list_of_student_record['Subject']}|{list_of_student_record['Grade']}')
        
        elif search_student not in list_of_student_record['Name']:
            print('Student Not Found!')

def compute_avg(st_grade_list):
    if not st_grade_list:
        print('No Student Records yet!')
        return
    
    all_grades = [grade_avg['Grade'] for grade_avg in st_grade_list]

    total = sum(all_grades)
    class_avg = total/len(st_grade_list)
    highest = max(all_grades)

    print(f'Class Average: {class_avg:.2f}')
    print(f'Highest Average: {highest:.2f}')







student_grade_list = []
print('==== STUDENT GRADE RECORD SYSTEM ====',
      '\n\n1 - Add Grade',
      '\n2 - View All Grades',
      '\n3 - Search Student',
      '\n4 - Compute Average',
      '\n5 - Exit')

while True:
    choice = input('Choose: ')
    if choice == '1':
        name = input('Name: ')
        subject = input('Subject: ')
        grade = int(input('Grade: '))
        add_grade(student_grade_list, name, subject, grade)
    elif choice == '2':
        print('=== STUDENT GRADES ===')
        view_all_grades(student_grade_list)
    elif choice == '3':
        search = input('Enter Student to Search: ')
        search_student(student_grade_list, search)
    elif choice == '4':
        compute_avg(student_grade_list)
    elif choice == '5':
        print('Exiing System...')
        break
    else:
        print('Invalid Choice!')
