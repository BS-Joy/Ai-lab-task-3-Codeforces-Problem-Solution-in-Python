pos = None
pos_list = []
t = int(input())
while t > 0:
    n = int(input())
    array_a = list(map(int, input().split()))
    for j in range(len(array_a) - 1):
        if array_a[j] != array_a[j+1]:
            pos = j + 1

    if array_a[0] != array_a[pos]:
        if pos == 1:
            pos_list.append(pos)
        else:
            pos += 1
            pos_list.append(pos)
    else:
        pos_list.append(pos)

    t -= 1

for i in pos_list:
    print(i)
