eden = []
print(eden)

grades = [98, 87, 90, 100, 0, 10, 7]
print('student grades', grades)

marks_that_dont_count = [76, 95, 65] * 34
print('some marks that dont count repeated A LOT OF TIMES', marks_that_dont_count)

print('number of marks',len(grades))

print('the first number in the list of marks is ', grades[0])
print('the last number in the list of marks is ', grades[-1])

the_first_five_digits = grades[0:5]
print('the first five digits in the list are',the_first_five_digits )

backwords_marks = grades[::-1]
print('the marks back backwords are', backwords_marks)

def match_marks(mark_list):
    count = 0
    matched_marks = []
 
    for mark in mark_list:
        mark_text = str(mark)
 
        if len(mark_text) > 1 and mark_text[0] == mark_text[-1]:
            count += 1
            matched_marks.append(mark)
 
    print("Marks with first and last digit same:", matched_marks)
    return count
 
same_digit_count = match_marks([88, 72, 99, 65, 77])
print("Number of matching marks:", same_digit_count)

total = 0
for grade in grades:
    total += grade

    average = total / len(grades)

    print('Sum of marks', total)
    print('average is ', average)

    grades.sort()

    print('The lowest mark is ', grades[0])
    print('The highest mark is ', grades[-1])

    print("")
print("===== STUDENT MARKS LIST ANALYZER =====")
print("Sorted Marks:", grades)
print("Total Marks:", total)
print("Average Marks:", average)
print("Lowest Mark:", grades[0])
print("Highest Mark:", grades[-1])
print("=======================================")


