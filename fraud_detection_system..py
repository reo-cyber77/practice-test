user1_ips = {"192.168.1.1", "10.0.0.1"}
user2_ips = {"192.168.1.1", "172.16.0.5"}

user1_devices = {"iPhone", "Laptop"}
user2_devices = {"Laptop", "Tablet"}
common_ip = user1_ips.intersection(user2_ips)
print(f'Common IPs: {common_ip}')
common_devices = user1_devices.intersection(user2_devices)
print(f'Common Devices: {common_devices}')


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