def daysCalculatorInMonth():

    try:
        start_month = int(input("please enter start month: "))
        end_month = int(input("please enter end month: "))

        if start_month >= 12 or end_month >= 12 or start_month >= end_month:
            print("please try again")
        else:
            print(f"days {(start_month - end_month) * 30}")
    except:
        print("please try again")


def daysCalculatorInYears():

    try:
        start_year = int(input("please enter start year: "))
        end_year = int(input("please enter end year: "))

        if start_year >= 12 or end_year >= 12 or start_year <= end_year:
            print("please try again")
        else:
            years = start_year - end_year
            print(f"days {years * 30}")
    except:
        print("please try again")


def daysCalculatorInDate():
    print("enter the date as the example -> day-month-year \n ")

    try:
        start_date = input("please enter start date: ").split("-")
        end_date = input("please enter end date: ").split("-")

        start = list(filter(lambda a: a != " ", start_date))
        end = list(filter(lambda a: a != " ", end_date))

        int_start = [eval(i) for i in start]
        int_end = [eval(i) for i in end]

        if int_start[0] > 30 or int_start[1] > 12 or len(str(int_start[2])) > 4:
            print("please try again")
        elif int_end[0] > 30 or int_end[1] > 12 or len(str(int_end[2])) > 4:
            print("please try again")
        elif int_start[0] > int_end[0] or int_start[1] > int_end[1] or int_start[2] > int_end[2]:
            print("please try again")
        else:
            day = int_end[0] - int_start[0]
            month = (int_end[1] - int_start[1]) * 30
            year = (int_end[2] - int_start[2]) * 12 * 30

            print(f"days {day + month + year}")

    except:
        print("please try again")


if __name__ == "__main__":
    print('''
        Days Calculator
        please select
        1- Days Calculator of month
        2- Days Calculator of year
        3- Days Calculator of Date ''')

    select = input("enter select: ")

    if select == "1":
        daysCalculatorInMonth()
    elif select == "2":
        daysCalculatorInYears()
    elif select == "3":
        daysCalculatorInDate()
    else:
        print("please try again")

