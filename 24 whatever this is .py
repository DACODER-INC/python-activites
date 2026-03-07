mark1 = int(input("Enter the mark of subject 1: "))
mark2 = int(input("Enter the mark of subject 2: "))
mark3 = int(input("Enter the mark of subject 3: "))
mark4 = int(input("Enter the mark of subject 4: "))
mark5 = int(input("Enter the mark of subject 5: "))
total = mark1 + mark2 + mark3 + mark4 + mark5
average = total / 5
percentage = (total / 500) * 100
print("Total marks: " + str(total))
print("Average marks: " + str(average))
print("Percentage: " + str(percentage) + "%")
if percentage >= 90:
    print("Grade: A")
elif percentage >= 80:
    print("Grade: B")
elif percentage >= 70:
    print("Grade: C")
elif percentage >= 60:
    print("Grade: D")
elif percentage >= 50:
 print('Grade D-')
else:
    print("Grade: F")