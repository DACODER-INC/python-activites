def shutdown(app1, app2, app3):
    choice = str(input(f"Are you sure you want to shutdown {app1}, {app2}, and {app3}? (yes/no): "))
    if choice == 'yes':
        print('shutting down...')
    elif choice == 'no':
        print('shutdown aborted')
    else:
        print('invalid input')
shutdown('word', 'minecraft', 'brave')
