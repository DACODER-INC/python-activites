option = (input('Enter either 1 for bike or 2 for car: ')).strip().upper()
if option == '1':
    print('You have selected bike choose your preferences down below')
    bike_type = str(input('Enter either 1 for electric bike or 2 for manual bike: ')).strip().upper()
    if bike_type == '1':
        print('You have selected electric bike, choose your preferences down below')
    electric_bike_type = str(input('Enter either 1 for mountain bike or 2 for road bike: ')).strip().upper()
    if electric_bike_type == '1':
        print('You have selected electric mountain bike')
    elif electric_bike_type == '2':
        print('You have selected electric road bike')
elif option == '2':
    print('You have selected car choose your preferences down below')
    car_type = str(input('Enter either 1 for sedan or 2 for suv: ')).strip().upper()
    if car_type == '1':
        print('You have selected sedan')
        type_of_sedan = str(input('enter either 1 for electric sedan or 2 for gas sedan: ')).strip().upper()
        if type_of_sedan == '1':
            print('You have selected electric sedan')
        elif type_of_sedan == '2':
            print('You have selected gas sedan')
    elif car_type == '2':
        print('You have selected suv')
        type_of_suv = str(input('enter either 1 for electric suv or 2 for gas suv: ')).strip().upper()
        if type_of_suv == '1':
            print('You have selected electric suv')
        elif type_of_suv == '2':
            print('You have selected gas suv')

