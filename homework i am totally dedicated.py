class DailyMessage:
    def __init__(self):
        self.message = ''

    
    def get_message(self):
        self.message = input('Enter a message')

    def print_message(self):
        print('This is your message in uppercase', self.message.upper())



daily_text = DailyMessage()
daily_text.get_message()
daily_text.print_message()



class HelperSession():
    def __init__(self):
        print('Your daily helper has been created')

    def __del__(self):
        print('Your daily helper has been destroyed')

def create_session():
    print('Making daily helper...')
    session = HelperSession()
    print('Session is ready...')
    return session



print('')
print('Calling create_session function...')
session_obj = create_session()
print('Program is still running...')


class PairFinder:
    def find_pair(self, numbers, target):
        lookup = {}

        for index, number in enumerate(numbers):
            needed_number = target - number
            
            if needed_number in lookup:
                return (lookup[needed_number], index)

            lookup[number] = index


        return None


numbers = (10,20,30,40,50,60,70,80,90)

target_value = int(input('Enter target number to search'))

result = PairFinder().find_pair(numbers, target_value)
if result is not None:
    print("index1=%d, index2=%d" % result)
else:
    print("No matching pair found.")
 

del session_obj
print("Program End")









