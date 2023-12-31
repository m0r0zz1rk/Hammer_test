### Тестовое задание "API реферальной системы" для Hammer Systems
___

#### Назначение

Выполнение тестового задания создания API 
для работы с личным кабинетом реферальной системы
___

#### Деплой

Проект развернут по адресу: http://m0r0zzz1rk.pythonanywhere.com

На главной страницы расположен Swagger, для использования авторизации
необходимо указывать следующее: 'Token (JWT токен полученный при авторизации)'

---

#### Зависимости
Для установки зависимостей воспользуйтесь файлом req.txt в каталоге `referal_back`:  
`pip install -r req.txt`

___

#### Переменные окружения
Для запуска проекта в директории `referral_back/web_app/` необходимо создать файл `.env` 
на основе файла `.env_example` и заполнить его необходимыми значениями

___

#### Приложения проекта
+ `authen` - приложение для аутентификациии и авторизации пользователей  
+ `commons` - приложение с общими методами
+ `referral` - приложение для работы с реферальной системой
+ 
___

#### Модели

В приложении `authen` созданы две модели:  
+ `Profiles` - модель профилей пользователей, для каждого пользователя Django создается одна запись
  (OneToOneField). Содержит номер телефона, собственный и активированный инвайт-коды
+ `AuthRequests` - модель запросов авторизации. При запросе кода авторизации на первом этапе авторизации
 сохраняет запись вида: пользователь Django - код авторизации

Обе модели отображены в администраторской панели 
(логин: adm, пароль: }ffT*#6n)

---

#### API

Приложение `authen` содержит следующие эндпоинты:  

`POST /api/v1/auth/auth_request/` - отправка запроса на авторизацию. В теле запроса необходимо 
указать параметр `phone` со значением, равным номеру телефона в формате +7 (###) ###-##-##. В качестве
ответа появится сообщение с кодом авторизации.

`POST /api/v1/auth/login/` - авторизация пользователя. В теле запроса необходимо указать параметр
`phone` со значением, равным номеру телефона в формате +7 (###) ###-##-##, и `auth_code` со строкой, 
состоящей из 4 цифр. В случае, если номер телефона и код авторизации были указаны верно, в ответе
будет представлен JWT токен и id пользователя Django

`GET /api/v1/auth/check_auth` - проверка авторизации пользователя. В header должен быть добавлен заголовок
`Authorization` со значением `Token (полученный от системы JWT токен)`. Ответ от системы с кодом 200 в случае
если предоставлен корректный токен, и 401 - в остальных случаях.

`GET /api/v1/auth/profile` - получение данных из профиля пользователя. В header должен быть добавлен заголовок
`Authorization` со значением `Token (полученный от системы JWT токен)`. Содержание ответа:
+ `phone` - номер телефона
+ `invite_code` - личный инвайт-код
+ `activated_invite_code` - активированный пользователем инвайт-код
+ `referrals` - список номеров телефонов рефералов

Приложение `referral` содержит следующие эндпоинты: 

`POST /api/v1/referral/activate_invite_code` - активация полученного инвайт-кода в профиле пользователя.
В header должен быть добавлен заголовок`Authorization` со значением `Token (полученный от системы JWT токен)`.
В теле запроса необходимо указать параметр `invite_code`, который содержит 6-значный инвайт-код для
активации. В ответе - сообщение об успешной активации кода

`GET /api/v1/referral/get_referrals` - получение списка рефералов пользователя. В header должен быть добавлен 
заголовок`Authorization` со значением `Token (полученный от системы JWT токен)`. В качестве ответа - список рефералов
пользователя (по аналогии с получением из профиля)

---

#### Frontend

В директории `referral_front` расположен небольшой проект на Vue.js, предназначений для формирования
интерфейса приложения. Для запуска необходимо следующее:  
+ Установить `node.js` и `npm`
+ Перейти в директорию `referral_front`
+ Запустить команду для установки зависимостей `npm i`
+ Создать файл `.env` и указать в нем: `VUE_APP_BACKEND_URL=(адрес запущенного приложения Django)`
+ Запустить команду для запуска тестового сервера `npm run serve`
+ 
---

### Postman-коллекция с запросами

В файле `hammer_test.postman_collection.json` находится коллекция с запросами ко всем API приложения

---

### Docker

В связи с отсутствием возможности размещения проекта в контейнерах docker на сервер (ввиду отсутствия сервера)
не создавал `Dockerfile` для фронта, бека и nginx, а также не создавал файл сценария `docker-compose.yml`.
Но опыт создания и развертывания имеется, в другом репозиторие на гитхабе под названием `Olympiad` есть
пример






