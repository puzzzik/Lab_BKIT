class Cd:
    """CD-диск"""

    def __init__(self, id, song, author, price, lib_id):
        self.id = id
        self.song = song
        self.author = author
        self.price = price
        self.lib_id = lib_id


class Lib:
    """Библиотека"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class LibCd:
    """
    'Диск из библиотеки' для реализации
    связи многие-ко-многим
    """

    def __init__(self, cd_id, lib_id):
        self.cd_id = cd_id
        self.lib_id = lib_id

