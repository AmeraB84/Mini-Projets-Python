def convert_to_array(serie_numbers):
    # Convert to string
    #st = str(serie_numbers)
    # num_list = []
    # for num in st:
    #     num_list.append(int(num))
    # num_list.reverse()
    # return num_list
    return [int(num) for num in str(serie_numbers)[::-1]]


print(convert_to_array(159874))
