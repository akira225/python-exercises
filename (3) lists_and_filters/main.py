def task1():
    return filter(lambda x: x % 17 == 0, range(1, 1001))


def task2():
    return filter(lambda x: str(x).count("2") > 0, range(1, 1001))


def task3():
    return filter(lambda x: str(x) == str(x)[::-1], range(1, 10001))


def task4(s: str):
    return s.count(" ")


def task5(s: str):
    vowels = ["a", "o", "i", "y", "u", "e", "A", "O", "I", "Y", "U", "E"]
    return "".join(list(map(lambda ch: '' if ch in vowels else ch, list(s))))


def task6(s: str):
    return filter(lambda word: len(word) <= 5, s.split())


def task7(s: str):
    return dict((word, len(word)) for word in s.split())


def task8(s: str):
    return list(set(filter(lambda x: x.isalpha(), list(s.lower()))))


def task9(l: list):
    return [x ** 2 for x in l]


def task10(points: list):
    return dict(map(lambda point: (point, (point[0] ** 2 + point[1] ** 2) ** 0.5),
                    filter(lambda point: point[1] == 5 * point[0] - 2, points)))


def task11():
    return [x ** 2 for x in filter(lambda y: y % 2 == 0, range(2, 28))]


def task12(points: list):
    return max(map(lambda point: point[0] ** 2 + point[1] ** 2,
                   filter(lambda point: point[0] >= 0 and point[1] >= 0, points))) ** 0.5


def task13(nums_first: list, nums_second: list):
    return [(x + y, x - y) for x, y in zip(nums_first, nums_second)]


def task14(nums: list):
    map(str, [y ** 2 for y in filter(lambda x: x % 2 == 0, map(int, nums))])


def task15(s: str):
    return [dict((line.split(',')[0], line.split(',')[i])
                 for line in s.split("\n")) for i in range(1, len(s.split("\n")[0].split(',')))]


def task16(mat: list):
    return [sum([mat[i][j] for i in range(len(mat))]) for j in range(len(mat[0]))]
