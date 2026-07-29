habit_info = ('coding', False, 3, 96869968796896, 5.6)
print(habit_info)

weekly_habits = (1,0,0,1,0,1,0)
print(weekly_habits)

print('total days followed', len(weekly_habits))

print('day 1', weekly_habits[0])
print('day 7', weekly_habits[-1])

first_3_days = weekly_habits[0:3]
print('the first 3 days are', first_3_days)

weekend_habits = weekly_habits[5:7]
print('the habits on the weekend are ', weekend_habits)

weekly_habits = weekly_habits + (0,)
print('after adding one more day here are the results', weekly_habits)

completed = weekly_habits.count(1)
missed = weekly_habits.count(0)
print('completed days',completed)
print('missed days',missed)

done = 0
not_done = 0
for i in range(0, len(weekly_habits)):
    if weekly_habits[i] == 1:
        done += 1
    else:
        not_done += 1
if done > not_done:
    print('Well done')
else:
    print('Try to be more consistent')


print("")
print("===== WEEKLY HABIT TRACKER =====")
print("Habit Name:", habit_info[0])
print("Weekly Record:", weekly_habits)
print("Completed:", done)
print("Missed:", not_done)
print("================================")




