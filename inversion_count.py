def count_inversion(inver):
    assert type(inver) == list
    len_num = len(inver)
    inver_count = 0
    if len_num == 1:
        return [0, inver]
    elif len_num == 2:
        if inver[0] > inver[1]:
            inver_count += 1
            a = inver[0]
            inver[0] = inver[1]
            inver[1] = a
            return [inver_count, inver]
        else:
            return [inver_count, inver]
    else:
        merged_count = []
        left = inver[0:(len_num//2)]
        right = inver[(len_num//2):len_num]
        count_split = count_inversion(left)[0] + count_inversion(right)[0]
        left_converted = count_inversion(left)[1]
        right_converted = count_inversion(right)[1]
        j=0
        i=0
        while i < len(right) and j < len(left):
            if right_converted[i] < left_converted[j]:
                count_split += len(left_converted[j:])
                merged_count += [right_converted[i]]
                i += 1
            else:
                merged_count += [left_converted[j]]
                j += 1
        if i < len(right):
            merged_count += right_converted[i:]
        elif j< len(left) :
            merged_count += left_converted[j:]
        return [count_split, merged_count]

file = open('data_set.txt', 'r')
row = []
for line in file.readlines():
    row.append(line)
a=[]
for i in row:
    a.append(int(i))

num = count_inversion(a)[0]
print(num)
