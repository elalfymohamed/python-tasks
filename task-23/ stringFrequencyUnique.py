def stringFrequencyUnique():
    string = input('enter string: ')
    string_list = string.split(" ")

    new_string_list = (list(filter(lambda a: a != "", string_list)))

    all_freq = {}

    for keys in new_string_list:
        all_freq[keys] = all_freq.get(keys, 0) + 1

    freq = [k for k, v in all_freq.items() if v == 1]

    print(len(freq))
    print(freq)


stringFrequencyUnique()
