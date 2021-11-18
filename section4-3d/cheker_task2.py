import json
import re


def solve():
    return "verts = [(1.0, 1.0, 0.0), (1.0, -1.0, 0.0), (-1.0, -1.0, 0.0), (-1.0, 1.0, 0.0), (1.0, 1.0, -1.0), (1.0, -1.0, -1.0), (-1.0, -1.0, -1.0), (-1.0, 1.0, -1.0), (0.5, 0.5, -1.6), (0.5, -0.5, -1.6), (-0.5, -0.5, -1.6), (-0.5, 0.5, -1.6), ] faces = [[0, 1, 2, 3], [0, 4, 5, 1], [1, 5, 6, 2], [2, 6, 7, 3], [3, 7, 4, 0], [4, 8, 9, 5], [5, 9, 10, 6], [6, 10, 11, 7], [7, 11, 8, 4], [8, 9, 10, 11] ]"


def check(reply):

    verts = [(1.0, 1.0, 0.0),
             (1.0, -1.0, 0.0),
             (-1.0, -1.0, 0.0),
             (-1.0, 1.0, 0.0),
             (1.0, 1.0, -1.0),
             (1.0, -1.0, -1.0),
             (-1.0, -1.0, -1.0),
             (-1.0, 1.0, -1.0),
             (0.5, 0.5, -1.6),
             (0.5, -0.5, -1.6),
             (-0.5, -0.5, -1.6),
             (-0.5, 0.5, -1.6),
             ]

    faces = [[0, 1, 2, 3],
             [0, 4, 5, 1],
             [1, 5, 6, 2],
             [2, 6, 7, 3],
             [3, 7, 4, 0],
             [4, 8, 9, 5],
             [5, 9, 10, 6],
             [6, 10, 11, 7],
             [7, 11, 8, 4],
             [8, 9, 10, 11]
             ]

    def parse_list(lst):

        lst = lst[1:-1]

        lst = re.sub('[\{\[\(]', '', lst)
        lst = lst.split("]")

        if len(lst) == 1:
            lst = lst[0].split(")")

        lst = list(filter(lambda line: line != ",", lst))

        def split_and_filter(line):
            return list(filter(None, line.split(",")))

        return list(map(split_and_filter, lst))

    splited_line = re.sub('[\s\n\ta-zA-Z+]', '', reply)

    splited_line = splited_line.split("=")

    r_verts = splited_line[1]
    r_faces = splited_line[2]

    rv = parse_list(r_verts)
    rf = parse_list(r_faces)

    for i in range(len(verts)):
        for j in range(len(verts[i])):
            if verts[i][j] != float(rv[i][j]):
                print(verts[i], rv[i])
                return False

    for i in range(len(faces)):
        for j in range(len(faces[i])):
            if faces[i][j] != float(rf[i][j]):
                print(faces[i], rf[i])
                return False
    return True


print(check(reply))

# def solve():
#     """Return a correct reply. This function is *optional*.
#
#     It is used to test the correctness of the 'check' function.
#
#     :return: a string that is a correct reply to the problem
#
#     """
#     return "Hello"
