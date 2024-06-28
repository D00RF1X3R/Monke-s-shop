<p align="center" object-fit: cover;>
	<img width="400" height="400" src="https://github.com/D00RF1X3R/MonkesShop/tree/main/readme-images/logo.png">
</p>

# BigGeek
BigGeek - Магазин товаров для geek'ов, заинтересованных в сериалах, играх и музыке. Так же в магазине есть форум для удобного обсуждения товаров и просмотра отзывов.


# Сайт

Сайт возможно запустить только на локальной машине из-за трудностей с хостингом на бесплатных ресурсах, связанных с одной из библиотек, используемых в проекте.

# Инструкция по запуску

- Клонировать репозиторий
  ```
   git clone https://github.com/D00RF1X3R/MonkesShop
  ```
- Установить зависимотри с помощью requirements.txt
   ```
   pip install -r requirements.txt
  ```
 - Запустить сервер
     ```
   python manage.py makemigrations
   python manage.py migrate
   python manage.py collectstatic
   python manage.py runserver
   ```
 - Создать админку
   ```
   python manage.py createsuperuser
	```
- Для корректной работы программы необходимо вручную открыть базу данных с помощью СУБД и в таблицу users_customerdata пользователя с id = 1.
- Зайти в админ панель, кнопка для которой появится в навигационной панели после авторизации в аккаунт админа.
- Добавить вселенные и категории.
# Технические моменты

>Если вы столкнулись с какой-либо ошибкой, пожалуйста, создайте [issue](https://github.com/D00RF1X3R/MonkesShop/issues/new).

## Архитектура базы данных

<p align="center" object-fit: cover;>
	<img width="838" height="1027" src="https://github.com/D00RF1X3R/MonkesShop/tree/main/readme-images/database.png">
</p>


## Команда

| [Савва](https://github.com/Nytrock) | [Даня](https://github.com/Damsmh)  | [Я](https://github.com/D00RF1X3R)  | [Влад](https://github.com/ttoddo)  | [Никита](https://github.com/dotbh)  | [Андрей](https://github.com/Rabotyaga00)  |
|---|---|---|---|---|---|
