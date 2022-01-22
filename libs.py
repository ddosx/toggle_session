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

# Функция для создания/удаления временного файла
def toggletempfile(status,path):
    # Если нужно создать
    if status == 'lock':
        # Создаём
        os.system('echo "lock" >' +path+'/status.txt')
    # Если нужно удалить
    elif status == 'unlock':
        # Проверка на существование
        if os.path.exists(path+'/status.txt'):
            # Удаление
            os.system('rm '+path+'/status.txt')
    # Возвращение status
    return status