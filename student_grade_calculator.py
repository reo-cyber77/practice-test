grades = [] # Creating a list to store 5 grades
try:
    for i in range(5):
        g = int(input(f'Enter grade #{i+1}: '))
        
        # Validation for the 0-100 range
        if g < 0 or g > 100:
            print("Invalid grade range!")
            
        grades.append(g) # Adds each grade to the list

    fnl_avg = sum(grades) / 5
    
    if fnl_avg >= 75:
        print(f'Average: {fnl_avg}')
        print('Status: Passed')
    else:
        print(f'Average: {fnl_avg}')
        print('Status: Failed')

except Exception:
    print('Invalid grade input!')
finally:
    print('Grade computation completed.')