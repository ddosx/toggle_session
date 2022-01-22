from http.client import OK
import os

# Функция для создания временной папки
def createtmppath(path):
    # Проверка на наличие
    if not os.path.isdir(path):
        # если её нет - создаём
        os.system('mkdir '+str(path))
        # Возвращаем True
        return True
    # если она есть
    # Возвращаем True
    return True

