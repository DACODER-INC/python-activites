class India():
    def capital(self):
        print('new delhi is the capital of india'.upper())

    def language(self):
        print('Hindi is the most popular language in india')

    def type(self):
        print('India is a developing country')

class USA():
    def capital(self):
        print('Washington dc is the capital of the USA')

    def language(self):
        print('English is the most popular language in the USA ')

    def type(self):
        print('The usa is a developed country')

obj = India()
obj1 = USA()

for country in (obj, obj1): 
    country.capital()
    country.language()
    country.type()