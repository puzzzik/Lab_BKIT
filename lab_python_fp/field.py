# -*- coding: utf-8 -*-

def field(items, *args):
    assert len(args) > 0
    # Необходимо реализовать генератор

    for item in items:
        if len(args) == 1:
            if item.get(args[0]) and item[args[0]] is not None:
                yield item[args[0]]
        else:
            d = {arg : item[arg] for arg in args if item.get(arg) and item[arg] is not None}
            if len(d) != 0:
                yield d



# goods = [
#     {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#     {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
#     {'price': 2000},
#     {'color': 'black'}
#]
# field(goods, 'title')  # 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price')  # {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}


# def main():
#     name = goods
#
#     args = []
#
#     cur = input("Введите названия пункта: ")
#     while cur:
#         args.append(cur)
#         cur = input("Введите названия пункта: ")
#     result = field(name, *args)
#     print(list(result))
#
#
# if __name__ == "__main__":
#     main()