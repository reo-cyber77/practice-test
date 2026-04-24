students_list = []
count = int(input('How many students to record? '))
for i in range(count):
    name = input('Name: ')
    math = int(input('Math: '))
    science = int(input('Science: '))
    english = int(input('English: '))

    student_records = (name, math, science, english)
    students_list.append(student_records)


students_tuple = tuple(students_list)

top_student = ''
highest_avg = 0

for s in students_tuple:
    student_name = s[0]
    avg = (s[1] +s[2] + s[3])/3
    print(f'{student_name} - Average: {avg:.2f}')

    if avg > highest_avg:
        highest_avg = avg
        top_student = student_name

print(f'\nTop Student: {top_student} with an average of {highest_avg:.2f}')



    

