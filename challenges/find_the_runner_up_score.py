if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sorted_arr_set = set(sorted(arr))
    sorted_arr_list = list(sorted_arr_set)
    if len(sorted_arr_list) == 1:
        print(sorted_arr_list)

    if len(sorted_arr_list) == 2:
        print(min(sorted_arr_list))

    if len(sorted_arr_list) > 2:
        max_number = max(sorted_arr_list)
        sorted_arr_list.remove(max_number)
        print(max(sorted_arr_list))
