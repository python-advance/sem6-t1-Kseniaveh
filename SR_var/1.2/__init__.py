"""Данный фрагмент кода был взят с сайта 
https://stackoverflow.com/questions/3718657/how-to-properly-determine-current-script-directory/22881871#22881871 
помогает нам корректно импортировать наш пакетик

Модуль sys обеспечивает доступ к некоторым переменным и функциям, взаимодействующим с интерпретатором python.
sys.path.append - добавляет относительные пути для поиска модулей.
"""

import sys
sys.path.append(get_script_dir())
from RegistrationBook import Registration
