# COT-3
Домашнее задание №3 - описание работы.

## Deploy
* Имеется 3 контейнера:
  + minio - сама хранилка минио, также для нее указан вольюм для хранения данных с ограничением 
  по размеру.
  + init-minio - контейнер для инициализации хранилища, в нем происходит добавление пользователя для приложения, создание бакета, загружается политика, чтобы пользователь имел доступ к бакету и также выделяется квота на размер бакета в 10 мегабайт.
  + app - контейнер с приложением, которое в цикле загружает картинку под разными названиями в бакет достаточно большое число раз, чтобы заполнить квоту, делается это из-под пользователя, который создан в контейнере init-minio.

* Для воспроизведения с квотой необходимо выполнить следующее(Default behaviour):
  + положить в корень репозитория файл ```.env```(можно просто скопировать из .env.example)
  + запустить ```docker compose up -d```
  + наслаждаться результатом

* Для воспроизведения ситуации, когда исчерпывается диск:
  + закомментить sleep в main.py в app
  + заменить настройку сканера минио на более медленную.

## Логи
* Есть 4 файла логов для 2 случаев: первый - когда достигнут размер квоты и минио  не может принять новую картинку из-за квоты, второй - когда исчерпано место на диске.
* Названия файлов логов для случая с квотой: app-quota-limit.logs и minio-quota-limit.logs
* Названия файлов логов для случая с исчерпанием диска: app-no-disk.logs и minio-no-disk.logs
* Также приложен скриншот, показывающий что на самом деле в бакете может быть больше занятого места, чем указано в квоте, так как условия квоты проверяются не постоянно, а при каждом новом проходе сканера.
* Чтобы посмотреть логи при воспроизведении: ```docker compose logs -f <service_name>```
