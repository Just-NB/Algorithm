import random
def mergesort(list):
# divide
    if len(list) == 1:
        return list

    half = int(len(list)/2)

    left = list[0:half]
    right = list[half:]
    left = mergesort(left)
    right = mergesort(right)

# merge
    lcnt = 0
    rcnt = 0
    cnt = 0

    while (lcnt < len(left)) and (rcnt < len(right)):
        if left[lcnt] < right[rcnt]:
            list[cnt] = left[lcnt]
            lcnt += 1
        else:
            list[cnt] = right[rcnt]
            rcnt += 1
        cnt += 1

    if lcnt == len(left) :
        list[cnt:] = right[rcnt:]
    if rcnt == len(right) :
        list[cnt:] = left[lcnt:]

    return list


if __name__ == '__main__':
    list = random.sample(range(0,100),100)
    print('original : {0}'.format(list))
    print('sorted : {0}'.format(mergesort(list)))
