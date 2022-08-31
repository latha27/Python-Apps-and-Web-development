
user_input = int(input("Enter the decimal integer number:"))
s = ''
def solution():
    global s, user_input
    while user_input != 0:
        if user_input % 2 == 0:
            s = s + '0'
        else:
            s = s + '1'
            user_input = user_input-1
        user_input = user_input / 2
    output = s[::-1]
    print(output)
    longest_gap = 0

    rows = output.split('1')
    print(rows)
    if output[0] != '1' or output[len(output) - 1] != '1':
        return 0

    if output[0] != '1':
        rows.remove(0)
    if output[len(output) - 1] != '1':
        index = len(rows) - 1
        if rows[index]:
            rows.remove(index)

    for i, item in enumerate(rows):
        if len(item) > longest_gap:
            longest_gap = len(item)

    return longest_gap

print(solution())
