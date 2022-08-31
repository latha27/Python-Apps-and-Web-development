def count_numbers(sorted_list, less_than):
    count = 0
    for i in sorted_list:
        if i < less_than:
            count = count + 1
    return count



if __name__ == "__main__":
    sorted_list = [8, 9, 5, 7]
    print(count_numbers(sorted_list, 4)) # should print 2