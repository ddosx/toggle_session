import os

# Функция для создания временной папки
def createtmppath(path):
    # Проверка на наличие
    if not os.path.isdir(path):
        # если её нет - создаём
        os.system('mkdir '+str(path))
        # Возвращаем path
        return path
    # если она есть
    # Возвращаем path
    return path
