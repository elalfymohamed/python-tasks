import datetime


def ageCalculator():
    print("Age Calculator")

    now_year = int(datetime.datetime.now().strftime("%Y"))
    now_month = int(datetime.datetime.now().strftime("%m"))
    now_day = int(datetime.datetime.now().strftime("%d"))

    try:
        year = int(input("Please enter a year: "))
        month = int(input("Please enter a month: "))
        day = int(input("Please enter a day: "))

        age = 0

        if month <= 12 and day <= 31 and len(str(year)) == 4:
            if year < now_year:
                age = now_year - year
            if month > now_month:
                age -= 1
                print(
                    f"You will be {age + 1 } years old in {month - now_month} months")
            elif month == now_month and day > now_day:
                age -= 1
                print(
                    f"You will be {age + 1} years old in {day - now_day} days")

            print(f"your age is {age} years")
        else:
            print("please try again")

    except:
        print("please try again")


ageCalculator()
