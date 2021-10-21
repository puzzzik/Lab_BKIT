# -*- coding: utf-8 -*-

from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

import numpy as np

def main():
    r = Rectangle("синего", 3, 2)
    c = Circle("зеленого", 5)
    s = Square("красного", 5)
    print(r)
    print(c)
    print(s)


    a = np.array([1, 2, 3, 4, 5], int)
    print(a)


if __name__ == '__main__':
    main()
