def field(items, *args):
    assert len(args) > 0

    for item in items:
        # Если передан только один аргумент, выдаем значения полей
        if len(args) == 1:
            field_name = args[0]
            value = item.get(field_name)
            if value is not None:
                yield value
        else:
            # Если передано несколько аргументов, выдаем словари
            result_dict = {}
            has_value = False
            for field_name in args:
                value = item.get(field_name)
                if value is not None:
                    result_dict[field_name] = value
                    has_value = True
            if has_value:
                yield result_dict


if __name__ == '__main__':

    # Пример использования:
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]

    # Примеры вызова:
    for value in field(goods, 'title'):
        print(value)
    # Результат: 'Ковер', 'Диван для отдыха'

    for value_dict in field(goods, 'title', 'price'):
        print(value_dict)
    # Результат: {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}
