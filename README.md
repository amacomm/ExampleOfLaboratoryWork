# Пример структуры лабораторной работы
Данный репозиторий служит примером структуры проекта с инсталируемым пакетом.  
Пример работы с пакетом показан в `notrbook.ipynb` файле.
Пакет содержит модуль тестирования, для выполнения тестов необходимо выполнить команду `python -m unittest discover -s .\simpcalc\`, тесты должны завершиться с сообщением 
```
......
----------------------------------------------------------------------
Ran 6 tests in 0.001s
```
Отмечу, что в данном коде присутствует ошибка, которая не отлавливается текущими тестами, для избежания подобных ситуаий в своих вариантах работы рекомендую посмотреть файлы `calculator.py`, `test_calculator.py` и ответить на следующие вопросы: *"Почему ошибка не была отловлена?"*, *"Как пофиксить код для исчезновения ошибки?"*, *"Как исключить данную ситуацию в дальнейшем?"*.