student_data = {
    "id1": {"name": "Sara", "class": "V", "subject": "english, math, science"},
    "id2": {"name": "David", "class": "V", "subject": "english, math, science"},
    "id3": {"name": "Sara", "class": "V", "subject": "english, math, science"},
    "id4": {"name": "Surya", "class": "V", "subject": "english, coding, math"}
}

print('Original student records:',student_data)

print('')
print('student id 1:')
print(student_data.get("id1", 'Not Found'))


print('')
print('student id 5:')
print(student_data.get("id5", 'Not Found'))

student_data['id5'] = {'name':'Anaya', 'class':'V', 'subject':'english, art, science'}
print('')
print('After adding id5:')
print(student_data)

student_data['id2']['subject'] = 'english, math, coding'
print('')
print('After changing id2')
print(student_data)