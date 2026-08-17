# Just as a reminder when we are working with INPUT METHOD it is not necessary to print them because it will do it automatically. 

first_name = input("First Name: ")
last_name = input("Last Name: ")
email = input("Email Address: ")
phone_number = input("Phone Nuber: ")
job_title = input("Job Title: ")
id_number = input("ID Number: ")
line = "--------------------------------------"

print ()
print (f"The ID card is: \n{line}")
print (f"{last_name.upper()}, {first_name} \n{job_title.title()} \nID: {id_number} \n \n{email.lower()} \n{phone_number}")
print (line)

