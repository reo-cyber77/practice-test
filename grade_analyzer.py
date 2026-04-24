grades = []


raw_input = input('Grades: ')

grades = [int(g.strip()) for g in raw_input.split(',')]



avg = sum(grades)/len(grades) 




print(f'Average {avg:.0f}')

if avg >= 75:

    print('Passed')

else:

    print('Failed')