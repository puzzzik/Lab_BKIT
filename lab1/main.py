# -*- coding: utf-8 -*-

import sys
import math


def get_coef(index, prompt):
    """
        Читаем коэффициент из командной строки или вводим с клавиатуры
        Args:
            index (int): Номер параметра в командной строке
            prompt (str): Приглашение для ввода коэффицента
        Returns:
            float: Коэффициент квадратного уравнения
        """
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
        float(coef_str)
    except:
        # Вводим с клавиатуры
        while True:
            print(prompt)
            coef_str = input()
            for sym in coef_str:
                if sym.isdigit() or sym == '-':
                    break
            else:
                continue
            break
    # Переводим строку в действительное число
    coef = float(coef_str)
    return coef


def get_roots(a, b, c):
    """
    Вычисление корней квадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        list[float]: Список корней
    """
    result = set()
    D = b * b - 4 * a * c
    if D == 0.0:
        root = -b / (2.0 * a)
        if root > 0:
            result.add(math.sqrt(root))
            result.add(-math.sqrt(root))
        elif root == 0:
            result.add(abs(math.sqrt(root)))


    elif D > 0.0:
        sqD = math.sqrt(D)
        rootSq1 = (-b + sqD) / (2.0 * a)
        rootSq2 = (-b - sqD) / (2.0 * a)

        if rootSq1 > 0:
            root1 = math.sqrt(rootSq1)
            root2 = -math.sqrt(rootSq1)
        elif rootSq1 == 0:
            root1 = abs(math.sqrt(rootSq1))

        if rootSq2 > 0:
            root3 = math.sqrt(rootSq2)
            root4 = -math.sqrt(rootSq2)
        elif rootSq2 == 0:
            root3 = abs(math.sqrt(rootSq2))

        result.add(root1)
        try:
            result.add(root2)
        except:
            pass
        result.add(root3)
        try:
            result.add(root4)
        except:
            pass

    return list(result)


def main():
    """
    Основная функция
    """
    a = get_coef(1, 'Введите коэффициент А:')
    while a == 0:
        a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a, b, c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {}, {} и {}'.format(roots[0], roots[1], roots[2]))
    else:
        print('Четыре корня: {}, {}, {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# qr.py 1 0 -4
