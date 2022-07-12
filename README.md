# ToDoList
## Приложение для управления персональными и рабочими задачами

####ЗАПУСК ПРИЛОЖЕНИЯ
* Склонировать репозиторий
https://github.com/SvetlanaNosatenko/todo_list.git

### Функционал ToDoList
* Возможность входа/регистрации/аутентификации через Вк.
* Функционал «шеринга» доски — чтобы пользователи могли совместно редактировать/просматривать наборы целей.
* Методы API представлены в swagger.
* Телеграм-бот @ToDoListNS_bot (https://t.me/ToDoListNS_bot) - дает возможность просматривать и создавать цели.
________________________
#### ЦЕЛИ
#### Создание целей
* Выбор временного интервала цели с отображением кол-ва дней до завершения цели.
* Выбор категории цели с возможностью добавлять/удалять/обновлять категории.
* Выбор приоритета цели.
* Выбор статуса выполнения цели (в работе, выполнен, просрочен, в архиве).
#### Изменение целей
* Изменение описания цели.
* Изменение статуса.
* Возможность менять приоритет и категорию у цели.
#### Удаление цели
* При удалении цель меняет статус на «в архиве».
#### Поиск по названию цели
#### Фильтрация по статусу, категории, приоритету, году
#### Выгрузка целей в CSV/JSON
#### Комментарии к целям (создавать, редактировать, удалять)
________________
#### АДМИНКА
У администраторов портала есть возможность просматривать все созданные сущности (доска, категория, цель, пользователь). Для каждой сущности существует свой раздел, внутри которого можно просматривать/редактировать/удалять сущности.
________________
####ТЕЛЕГРАМ-БОТ

Идентификация пользователя:
* Пользователь пишет боту в первый раз.
* Бот отправляет код для верификации.
* Пользователь копирует код верификации и вводит его в приложение, когда авторизован.

Команды:
* /goals - получить список открытых целей пользователя.
* /create - создать цель.
* /cancel - отмена текущего действия.