from lab2.lab_python_fp.gen_random import gen_random
class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = iter(items)
        self.unique_set = set()
        self.ignore_case = kwargs.get('ignore_case', False)

    def __next__(self):
        while True:
            item = next(self.items)
            key = item.lower() if self.ignore_case and isinstance(item, str) else item
            if key not in self.unique_set:
                self.unique_set.add(key)
                return item

    def __iter__(self):
        return self


if __name__ == '__main__':
    # Пример использования:
    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    unique_iter1 = Unique(data1)
    print("data1: "+str(list(unique_iter1)))  # Вывод: [1, 2]

    data2 = gen_random(10, 1, 3)
    unique_iter2 = Unique(data2)
    print("data1: "+str(list(unique_iter2)))  # Вывод: Случайные числа без дубликатов

    data3 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    unique_iter3 = Unique(data3)
    print("data3: "+str(list(unique_iter3))) # Вывод: ['a', 'A', 'b', 'B']

    unique_iter4 = Unique(data3, ignore_case=True)
    print("data4: "+str(list(unique_iter4)))  # Вывод: ['a', 'b']