from enum import Enum

# Токент бота
TOKEN = "5031931528:AAHssOqk4aGjf2Nwj3J8owc8JoVz6ngpRYY"

# Файл базы данных Vedis
db_file = "db.vdb"

# Ключ записи в БД для текущего состояния
CURRENT_STATE = "CURRENT_STATE"

# Состояния автомата
class States(Enum):
    STATE_START = "0"  # Начало нового диалога
    STATE_ENTER_COUNTRY = "1"
    STATE_ENTER_CITY = "2"
    STATE_SEND_WEATHER = "3"