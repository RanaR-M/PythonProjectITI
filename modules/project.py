import csv, pandas as pd


class Project:
    def __init__(self, username, title, details, totalTarget, startDate, endDate):
        self.username = username
        self.title = title
        self.details = details
        self.totalTarget = totalTarget
        self.startDate = startDate
        self.endDate = endDate

    def saveProject(self):
        if self.startDate < self.endDate:
            self.saveToCSV()
            return True
        else:
            return False

    def saveToCSV(self):
        with open("projectDB.csv", "a") as csvfile:
            csvwriter = csv.writer(csvfile)
            fields = [self.username, self.title, self.details,
                      str(self.totalTarget), str(self.startDate), str(self.endDate)]
            csvwriter.writerow(fields)

    @staticmethod
    def viewallprojects():
        df = pd.read_csv('projectDB.csv')
        with pd.option_context('display.max_rows', None,
                               'display.max_columns', None,
                               'display.precision', 3,
                               ):
            print(df)

    @staticmethod
    def edituserproject(username, index, field, edit):
        df = pd.read_csv('projectDB.csv')
        edit = str(edit)
        index = int(index)
        if df.loc[index, 'username'] == username:
            if field == 'startDate':
                if df.loc[index, 'endDate'] > edit:
                    df.loc[index, field] = edit
                    return True
                else:
                    return False
            elif field == 'endDate':
                if df.loc[index, 'startDate'] < edit:
                    df.loc[index, field] = edit
                    return True
                else:
                    return False
            else:
                df.loc[index, field] = edit
                df.to_csv('projectDB.csv', index=False)
                return True
        else:
            # print("user doesn't have permission")
            return False

    @staticmethod
    def deleteuserproject(username, index):
        df = pd.read_csv('projectDB.csv')
        index = int(index)
        if df.loc[index]['username'] == username:
            df.drop(index, inplace=True)
            df.to_csv('projectDB.csv', index=False)
            return True
        else:
            # print("user doesn't have permission")
            return False

    @staticmethod
    def searchbydate(date, letter):
        df = pd.read_csv('projectDB.csv')
        if letter == 's':
            temp_df = df.loc[df['startDate'] == date]
            with pd.option_context('display.max_rows', None,
                                   'display.max_columns', None,
                                   'display.precision', 3,
                                   ):
                print(temp_df)
                return True
        elif letter == 'e':
            temp_df = df.loc[df['endDate'] == date]
            with pd.option_context('display.max_rows', None,
                                   'display.max_columns', None,
                                   'display.precision', 3,
                                   ):
                print(temp_df)
                return True
        else:
            return False
            # print('wrong letter')
