class Emp:
    """Сотрудник"""

    def __init__(self, id, fio, sal, dep_id):
        self.id = id
        self.fio = fio
        self.sal = sal
        self.dep_id = dep_id


class Dep:
    """Отдел"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class EmpDep:
    """
    'Сотрудники отдела' для реализации
    связи многие-ко-многим
    """

    def __init__(self, dep_id, emp_id):
        self.dep_id = dep_id
        self.emp_id = emp_id

