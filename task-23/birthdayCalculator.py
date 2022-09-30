import datetime


def birthdayCalculator():
    print("Birthday Calculator")

    now_month = int(datetime.datetime.now().strftime("%m"))
    now_day = int(datetime.datetime.now().strftime("%d"))

    try:
        month = int(input("Please enter a month: "))
        day = int(input("Please enter a day: "))

        birthday = (12 - now_month) + month
        get_day = now_day - day
        get_month = now_month - month

        if month <= 12 and day <= 31:
            if month < now_month:
                if birthday > 0:
                    print(
                        f"your birthday is after {get_day} day / {birthday} month")
                else:
                    print(f"your birthday is after {get_day} day")
            else:
                if get_month > 0:
                    print(
                        f"your birthday is after {get_day} day / {get_month} month")
                else:
                    print(f"your birthday is after {get_day} day")
        else:
            print("please try again")

    except:
        print("please try again")


birthdayCalculator()
