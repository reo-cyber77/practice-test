name = input('Enter student name:')
grade = int(input('Enter student grade:'))
student_record = {'name': name, 'grade': grade}
find_student = input('Enter student name:')
if not student_record['name'] == find_student:
    print('Student not found')
else:
    print(f"{student_record['name']} has a grade of {student_record['grade']}")
