import time
from contextlib import contextmanager

class cm_timer1:
    def __init__(self):
        # self.startTime = time.localtime()
        pass

    def __enter__(self):
        self.startTime = time.time()
        # Должен возвращаться значимый объект
        # например, открытый файл

    def __exit__(self, exp_type, exp_value, traceback):
        if exp_type is not None:
            print(exp_type, exp_value, traceback)
        else:
            self.endTime = time.time()
            print(self.endTime - self.startTime)

with cm_timer1():
    time.sleep(2)


@contextmanager
def cm_timer2():
    startTime = time.time()
    yield
    endTime = time.time()
    print(endTime - startTime)

with cm_timer2():
    time.sleep(2)