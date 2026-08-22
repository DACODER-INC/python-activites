class employee:
    def __init__(self):
        print('Employee created')
    def __del__(self):
        print('Employee destructed')




def create_obj():
    print('Making object')
    obj = employee()
    print('Function end')

    return obj
obj = create_obj()