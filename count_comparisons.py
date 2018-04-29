def count_comparisons_first_element(array):
    assert type(array) == list #Array must be a list#
    m = len(array)
    if m == 1 or m == 0:
        return 0
    else:
        pivot_point = array[0]
        i = 1
        for j in range(1, m):
            if array[j] < pivot_point:
                array[j], array[i] = array[i], array[j]
                i += 1
        array[0],array[i-1] = array[i-1], array[0]
        return (m-1) + count_comparisons_first_element(array[0:i-1]) + count_comparisons_first_element(array[i:])

def count_comparisons_final_element(array):
    assert type(array) == list #Array must be a list#
    m = len(array)
    if m == 1 or m == 0:
        return 0
    else:
        pivot_point = array[m-1]
        left = []
        right = []
        for i in range(0, m-1):
            if array[i] > pivot_point:
                right += [array[i]]
            else:
                left = [array[i]] + left
        return (m-1) + count_comparisons_final_element(left) + count_comparisons_final_element(right)

def count_comparisons_medium_element(array):
    assert type(array) == list #Array must be a list#
    m = len(array)
    if m == 1 or m == 0:
        return 0
    else:
        pivot_point_list = [array[0], array[(m-1)//2], array[m-1]]
        p_e = pivot_point_list[0]
        if max(pivot_point_list) == p_e:
            pivot_point = max(pivot_point_list[1:])
        else:
            if min(pivot_point_list[1:]) > p_e:
                pivot_point = min(pivot_point_list[1:])
            else:
                pivot_point = p_e
        left = []
        right = []
        for i in range(0, m-1):
            if array[i] > pivot_point:
                right += [array[i]]
            else:
                left = [array[i]] + left
        return (m-1) + count_comparisons_medium_element(left) + count_comparisons_medium_element(right)

file = open('count_comparisons_data.txt', 'r')
a = []
for line in file.readlines():
    a.append(int(line))
num = count_comparisons_first_element(a)
print(num)

138382, 164123, 162085
