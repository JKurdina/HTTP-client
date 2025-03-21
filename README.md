# HTTP-client
Этот проект представляет собой CLI-программу, которая является клиентом к условному сервису. Программа использует сокеты для отправки HTTP-запросов и поддерживает конфигурацию через файл в формате TOML.
## Запуск
Запустите программу, передав необходимые аргументы:
```sh
python main.py --fr "+123456789" --t "+987654321" --text "Hello, World!"
```
Где:
- fr — номер отправителя
- t — номер получателя
- text — текст сообщения

Результат выполнения:
- Код ответа и тело ответа будут выведены в консоль
- Логи будут записаны в файл sms_client.log

## Тестирование
Чтобы запустить тесты воспользуйтесь командой:
```sh
pytest
```
Тесты проверяют:
- Отправку SMS
- Формирование HTTP-запросов
- Преобразование HTTP-ответов из байтов
