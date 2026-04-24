student1 = {"math", "science", "english"}
student2 = {"science", "history", "english"}
all_subjects = student1.union(student2)
print(f'All subjects: {all_subjects}')
common_subjects = student1.intersection(student2)
print(f'Common subjects: {common_subjects}')
student1_unique = student1.difference(student2)
print(f'Student1 Unique Subjects: {student1_unique}')
student2_unique = student2.difference(student1)
print(f'Student2 Unique Subjects: {student2_unique}')

