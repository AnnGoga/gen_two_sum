class Averager:

    ___data_list = []

    @staticmethod
    def add_data(data):
        Averager.___data_list.append(data)

    @staticmethod
    def get_average():
        return sum(Averager.___data_list) / len(Averager.___data_list)

    @staticmethod
    def clear():
        Averager.___data_list.clear()


def deco(func):
    import functools
    import time

    @functools.wraps(func)
    def inner(*args, **kwargs):
        start_time = time.time() #начало таймера
        result = func(*args, **kwargs)
        end_time = time.time() #завершение таймера
        time_delta = end_time - start_time
        Averager.add_data(time_delta)
        return result

    return inner


@deco
def two_sum_brute(nums, target): # deco(two_sum_brute)
    """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
    """

    length = len(nums)
    for i in range(length):
        for j in range(length):
            if nums[j] == target - nums[i]:
                return [i, j]


@deco
def two_sum(nums, target):
    """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
    """
    length = len(nums)
    nums_map = dict()
    for i in range(length):
        nums_map[nums[i]] = i

    for i in range(length):
        diff = target - nums[i]

        if (diff in nums_map.keys()) and (nums_map.get(diff, -1) != i):
            return [i, nums_map.get(diff)]


def array_generator(a: int, b: int):
    import random
    array = list(range(random.randint(a, b)))
    for i in range(len(array)):
        array[i] = random.randint(0, 10) #элементы генерируемого массива генерируются в этом диапазоне
    return array


def test_1(count: int):
    import random

    Averager.clear()

    input_first = array_generator(100, 200)#сгенерированный массив two_sum_brute
    input_second = random.randint(0, 10)#сгенерированный таргет
    for i in range(count):
        two_sum_brute(input_first, input_second)

    print(f"Среднее время работы функции two_sum_brute: {Averager.get_average()}")
    Averager.clear()


def test_2(count: int):
    import random

    Averager.clear()

    input_first = array_generator(100, 200)
    input_second = random.randint(0, 10)
    for i in range(count):
        two_sum(input_first, input_second)

    print(f"Среднее время работы функции two_sum: {Averager.get_average()}")
    Averager.clear()


if __name__ == "__main__":
    test_1(100)
    test_2(100)
