    
import inspect
import os
import sys

"""Данный фрагмент кода был взят с сайта 
https://stackoverflow.com/questions/3718657/how-to-properly-determine-current-script-directory/22881871#22881871 
помогает нам корректно импортировать наш пакетик
Модуль sys обеспечивает доступ к некоторым переменным и функциям, взаимодействующим с интерпретатором python.
sys.path.append - добавляет относительные пути для поиска модулей.
"""


def get_script_dir(follow_symlinks=True):
    if getattr(sys, 'frozen', False):
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)


sys.path.append(get_script_dir())

import Registration
