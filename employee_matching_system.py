employee_A = {"python", "sql", "excel"}
employee_B = {"python", "java"}
employee_C = {"sql", "excel", "powerbi"}

project_requirements = {"python", "sql"}
print(f'Project requirements: {project_requirements}')
if employee_A.issubset(project_requirements) == 'True':
    print('Empolyee A -> Qualified')
    skills = employee_A.difference(project_requirements)
    print(f'Matching skills: {skills}')




#Correction
# Change this:
if project_requirements.issubset(employee_A): 
    print('Employee A -> QUALIFIED')
    # Use intersection for matching skills
    matching = employee_A.intersection(project_requirements)
    print(f'Matching skills: {matching}')
else:
    # Use difference for missing skills
    missing = project_requirements.difference(employee_A)
    print(f'Missing skills: {missing}')

    