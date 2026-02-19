maths_mark = 40
english_mark = 60
hindi_mark = 50 
science_mark = 70
total_marks = maths_mark + english_mark + hindi_mark + science_mark
print(' The total marks obtained by the student is : ' + str(total_marks))
percentage = (total_marks / 400) * 100
percentage = int(percentage)
print(' The percentage obtained by the student is : ' + str(percentage) + '%')