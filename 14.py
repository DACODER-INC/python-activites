while True:
     try: 
       amount = int(input('Enter the amount of money you want to withdraw : '))
       break # valid input, exit loop except ValueError:
     
     except ValueError:
         print(' Invalid input. Please enter a valid integer amount.')
note1 = amount // 100
note2 = (amount%100)// 50
note3 = ((amount%100)%50)//20
print(' The number of 100 rupee notes you will get is : ' + str(note1))
print(' The number of 50 rupee notes you will get is : ' + str(note2))
print(' The number of 20 rupee notes you will get is : ' + str(note3))

