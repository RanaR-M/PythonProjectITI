import datetime, pandas as pd
from modules.project import Project


def get_number(username):
    print('-' * 15)
    print(f'Welcome {username}, to the crowd funding library !')
    print('-' * 15)
    print('What do you want to do?')
    print('1. Create project')
    print('2. View all projects')
    print('3. Edit your project')
    print('4. Delete your project')
    print('5. Search for project using date')
    print('6. Exit program')
    number = int(input('Enter number for action: '))
    print('-' * 15)
    return number


def handel_orders(number, username):
    if number == 1:
        title = input('Enter title of project: ')
        details = input('Enter details of project: ')
        totalTarget = input('Enter total target of project: ')
        start = [input('Enter Start date year (YYYY): '),
                 input('Enter Start date month (mm): '),
                 input('Enter Start date day (dd): ')]
        startDate = datetime.date(int(start[0]), int(start[1]), int(start[2]))
        end = [input('Enter End date year (YYYY): '),
               input('Enter End date month (mm): '),
               input('Enter End date day (dd): ')]
        endDate = datetime.date(int(end[0]), int(end[1]), int(end[2]))
        print('-' * 15)
        p = Project(username, title, details, totalTarget, startDate, endDate)
        test = p.saveProject()
        if test:
            print('Project created successfully !!')
        else:
            print('Start and end date are wrong')

    elif number == 2:
        Project.viewallprojects()
        print('-' * 15)

    elif number == 3:
        Project.viewallprojects()
        print('-' * 15)
        index = input('Enter index of YOUR project that you want to edit: ')
        field = int(input('Enter (1) title (2) details (3) totalTarget (4) start date (5) end date: '))
        edit = ''
        if field == 1:
            field = 'title'
            edit = input('Enter your edit: ')
        elif field == 2:
            field = 'details'
            edit = input('Enter your edit: ')
        elif field == 3:
            field = 'total Target'
            edit = input('Enter your edit: ')
        elif field == 4:
            field = 'startDate'
            start = [input('Enter Start date year (YYYY): '),
                     input('Enter Start date month (mm): '),
                     input('Enter Start date day (dd): ')]
            edit = datetime.date(int(start[0]), int(start[1]), int(start[2]))
        elif field == 5:
            field = 'endDate'
            end = [input('Enter End date year (YYYY): '),
                   input('Enter End date month (mm): '),
                   input('Enter End date day (dd): ')]
            edit = datetime.date(int(end[0]), int(end[1]), int(end[2]))
        else:
            print('wrong number')

        print('-' * 15)
        test = Project.edituserproject(username, index, field, str(edit))
        if test:
            print('Edited successfully')
        elif not test and number in [4, 5]:
            print('wrong end or start number')
        elif not test and number in [1, 2, 3]:
            print("user doesn't have permission")
        print('-' * 15)

    elif number == 4:
        Project.viewallprojects()
        print('-' * 15)
        index = input('Enter index of YOUR project that you want to delete: ')
        test = Project.deleteuserproject(username, index)
        if test:
            print('Deleted successfully')
        else:
            print("user doesn't have permission")
        print('-' * 15)

    elif number == 5:
        letter = input('Enter s for start date or e for end date: ')
        date = [input('Enter date year (YYYY): '),
                input('Enter date month (mm): '),
                input('Enter date day (dd): ')]
        dateObj = datetime.date(int(date[0]), int(date[1]), int(date[2]))
        test = Project.searchbydate(str(dateObj), letter)
        if not test:
            print('wrong letter')
    elif number == 6:
        print('-' * 15)
        print('goodbye!!!')


def save_user(data):
    df = pd.DataFrame(data)
    df.to_csv('usersDB.csv', mode='a', index=False, header=False)


def get_user(email, password):
    df = pd.read_csv("usersDB.csv")
    user_info = df[['email', 'password']][df['email'] == email]
    if len(user_info) == 0:
        print('The email is not registered')
    else:
        if user_info.password.values == password:
            return True
        else:
            return False
