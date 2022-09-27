# task 1

def evenNumbers_oddNumbers():
    list_num = input("Enter Numbers: ")
    list_arr = list_num.split(" ")
    arr = [eval(i) for i in list_arr]
    num_init = []
    num_float = []
    for num in arr:
        if num % 2:
            num_init.append(num)
        else:
            num_float.append(num)
    print(f"num_init {num_init}")
    print(f"num_float {num_float}")


# evenNumbers_oddNumbers()


# Task2

def evenNumbers_oddNumbers():
    sentence = input("Enter sentence: ")
    sentence_list = sentence.split(" ")
    not_dup = []

    for word in sentence_list:
        if word not in not_dup:
            not_dup.append(word)
    print(" ".join(not_dup))


# evenNumbers_oddNumbers()


# task3

def printNumbers():
    end = int(input("Enter Number: "))

    for num in range(0, end + 1):
        print(num)


# printNumbers()

# task4

def numberAcceptDivision():
    start = int(input("Enter Start Number: "))
    end = int(input("Enter End Number: "))

    for num in range(0, start + 1):
        if num % end:
            print(num)


# numberAcceptDivision()

# task5
def numbersDivision():
    start = int(input("Enter Start Number: "))
    end = int(input("Enter End Number: "))

    for num in range(0, 100):
        if num % start or num % end:
            print(num)


# numbersDivision()


# task6

class Game:
    def __init__(self):
        first_loop = True
        while first_loop:
            print('''
            welcome to Gamse
            Enter Game Number
            1- Even numbers and odd numbers
            2- word count sentence
            3- prints numbers
            4- number accept division
            5- numbers accept division
            X- exit
            ''')
            user_choice = input("Enter Game Number: ")
            second_loop = True
            if user_choice == "1":
                list_num = input("Enter Numbers: ")
                self.evenNumbers_oddNumbers(list_num)
            elif user_choice == "2":
                sentence = input("Enter sentence: ")
                self.wordCountSentence(sentence)
            elif user_choice == "3":
                end = int(input("Enter Number End: "))
                self.printNumbers(end)
            elif user_choice == "4":
                start = int(input("Enter Start Number : "))
                end = int(input("Enter End Number : "))
                self.numberAcceptDivision(start, end)
            elif user_choice == "5":
                start = int(input("Enter Start Number : "))
                end = int(input("Enter End Number : "))
                self.numbersDivision(start, end)
            elif user_choice == "x":
                print("Goodbye...")
                exit()
            else:
                print("please try again")
                continue
            while second_loop:
                play_again = input("Press y to play again , x to exit: ")

                if play_again == "x":
                    print("Goodbye...")
                    exit()
                elif play_again == "y":
                    second_loop = False
                    first_loop = True
                else:
                    print("please tray again")
                    continue

    def evenNumbers_oddNumbers(self, list_num):
        list_arr = list_num.split(" ")
        arr = [eval(i) for i in list_arr]
        num_init = []
        num_float = []
        for num in arr:
            if num % 2:
                num_init.append(num)
            else:
                num_float.append(num)
        print(f"num_init {num_init}")
        print(f"num_float {num_float}")

    def wordCountSentence(self, sentence):
        sentence_list = sentence.split(" ")
        not_dup = []

        for word in sentence_list:
            if word not in not_dup:
                not_dup.append(word)
        print(" ".join(not_dup))

    def printNumbers(self, end):
        for num in range(0, end + 1):
            print(num)

    def numberAcceptDivision(self, start, end):
        for num_start in range(0, start + 1):
            for num_end in range(1, end + 1):
                if num_start % num_end == 0:
                    print(f"{num_start} % {num_end} = {num_start % num_end}")
            print("--------------")

    def numbersDivision(self, start, end):
        for num_start in range(1, start + 1):
            for num_end in range(1, 100):
                if num_start % num_end == 0:
                    print(f"{num_start} % {num_end} = {num_start % num_end}")
            print("--------------")
        for num_start in range(1, end + 1):
            for num_end in range(1, 100 + 1):
                if num_start % num_end == 0:
                    print(f"{num_start} % {num_end} = {num_start % num_end}")
            print("---------------------------")


Game()
