import os

# Функция для создания временной папки
def createtmppath():
    path = '.tmp'
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
def toggletempfile(status):
    path = '.tmp'
    # Если нужно создать
    if status == 'lock':
        # Создаём
        os.system('echo "lock" > ' +path+'/status.txt')
    # Если нужно удалить
    elif status == 'unlock':
        # Проверка на существование
        if os.path.exists(path+'/status.txt'):
            # Удаление
            os.system('rm '+path+'/status.txt')
    # Возвращение status
    return status

# Функция для проверки существования временного файла
def checktempfile():
    path = '.tmp'
    # Проверка
    if os.path.exists(path+'/status.txt'):
        status = 'lock'
    else:
        status = 'unlock'
    # Возращение статуса
    return status

# Функция для изменения статуса
def returnstatus(status):
    if status == 'lock':
        status = 'unlock'
    else:
        status = 'lock'
    # Возращение статуса
    return status