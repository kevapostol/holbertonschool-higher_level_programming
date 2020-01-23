#!/usr/bin/python3
'''
The 14-pascal_triangle module
'''


def pascal_triangle(n):
    if n <= 0:
        return []
    else:
        li = [[1]]
        temp = [1]

        for i in range(n - 1):
            temp = li[len(li) - 1].copy()
            temp.insert(0, 0)
            temp.append(0)

            temp2 = []
            for j in range(len(temp) - 1):
                p1 = temp[j]
                p1 = temp[j + 1]
                temp2.append(p1 + p2)
            li.append(temp2)
    return li
