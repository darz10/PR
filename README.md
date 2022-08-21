# Place_remeber

Приложение для создания воспомнинаий привязанных к месту и хранения их. В приложении существует авторизация через социальную сеть VK.  
___

## Запуск приложения
```
git clone https://github.com/darz10/Places_Remember
```
Создайте виртуальное окружение проекта
```
python3 -m virtualenv venv
```
Запустите созданное окружение командой
```
source venv/bin/activate
```
Загрузите все зависимости проекта
```
pip install -r requirements.txt
```
Установите миграции
```
python manage.py migrate
```
Запустите приложение
```
python manage.py runserver
```
