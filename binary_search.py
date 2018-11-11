def binary_search(num_to_find, sorted_num_list):
    lower_index = 0
    upper_index = len(sorted_num_list) - 1
    while lower_index <= upper_index:
        middle_index = (upper_index - lower_index) // 2 + lower_index
        if sorted_num_list[middle_index] == num_to_find:
            return middle_index
        elif sorted_num_list[middle_index] < num_to_find:
            lower_index = middle_index + 1
        else:
            upper_index = middle_index - 1
    return -1

l = [1,4,5,5,75,78]
print(binary_search(78 ,l))
