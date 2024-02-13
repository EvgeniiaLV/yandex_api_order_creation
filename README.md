# Автотесты для POST запроса веб-приложения Яндекс.Самокат Создание заказа
- Тесты для проверки сценария:
  1. Клиент создает заказ.
  2. Проверяется, что по треку заказа можно получить данные о заказе.
- Шаги автотеста:
  1. Выполнить запрос на создание заказа.
  2. Сохранить номер трека заказа.
  3. Выполнить запрос на получения заказа по треку заказа.
  4. Проверить, что код ответа равен 200.

# Выполнение автотестов с построением Allure Report
# Требования к окружению
-  Для запуска тестов должны быть установлены `Python 3.11` и библиотеки pytest и requests
- `pip install pytest-xdist`   - для параллелизации запуска тестов
- `pip install allure-pytest`
- `JAVA 8+`  (нужна для генерации allure репорта) скачать можно отсюда - https://jdk.java.net/archive/
- Прописать путь до папки с установленной Java в переменные окружения. В Path должны быть добавлены пути до Java и до папки Java\bin
- Скачать архив с `Allure` - https://github.com/allure-framework/allure2/releases/download/2.26.0/allure-2.26.0.zip
- Прописать путь до папки с Allure в переменные окружения Path

# Запуск тестов (из консоли cmd или терминала PyCharm)
- Запустить тестовый сервер с приложением (дождаться окончания запуска и проверить, что приложение открывается)
- Обновить параметр `URL_SERVICE` в файле `configuration.py` значением URL запущенного тестового стенда
- Открыть cmd / terminal
- Перейти в директорию с проектом ~/yandex_api_order_creation
- Выполнить команду `pytest -n=4 --alluredir=./allure-results  order_creation_test.py` (параметр -n=4 указывает на запуск тестов в 4 потока)
- Все названия исполняемых тестовых функций начинаются с префикса 'test'
- После выполнения тестов выполнить команду `allure serve` для генерации отчета


# Список баг-репортов:
- https://ev-liasheva.youtrack.cloud/issue/YS-33/Tip-dannyh-deliveryDate-otlichaetsya-na-bekende-v-tablice-Orders-i-v-API-sozdaniya-zakaza
- https://ev-liasheva.youtrack.cloud/issue/YS-34/Ogranicheniya-na-vvod-dannyh-sozdaniya-zakaza-otsutstvuyut-v-trebovaniyah-k-bekendu-i-API-v-otlichii-ot-trebovanij-k-frontendu
- https://ev-liasheva.youtrack.cloud/issue/YS-35/Neobyazatelnoe-pole-Comment-na-frontende-yavlyaetsya-obyazatelnym-dlya-zapolneniya-v-POST-zaprose-api-v1-orders-soglasno
- https://ev-liasheva.youtrack.cloud/issue/YS-36/500-oshibka-pri-sozdanii-zakaza-s-peredannym-znacheniem-parametra-tipa-string-dlinoj-bolshe-3000-simvolov-cherez-POST-zapros-api
- https://ev-liasheva.youtrack.cloud/issue/YS-37/Otsutstvuet-validaciya-nesootvetstvuyushego-tipa-dannyh-pri-sozdanii-zakaza-cherez-POST-zapros-api-v1-orders
- https://ev-liasheva.youtrack.cloud/issue/YS-38/Zakaz-uspeshno-sozdan-pri-pustom-obyazatelnom-pole-cherez-POST-zapros-api-v1-orders
- https://ev-liasheva.youtrack.cloud/issue/YS-39/500-oshibka-pri-sozdanii-zakaza-cherez-POST-zapros-api-v1-orders-s-nulevoj-deliveryDate
- https://ev-liasheva.youtrack.cloud/issue/YS-40/Zakaz-uspeshno-sozdan-s-otricatelnym-znacheniem-rentTime-pri-sozdanii-zakaza-cherez-POST-zapros-api-v1-orders
- https://ev-liasheva.youtrack.cloud/issue/YS-41/Zakaz-uspeshno-sozdan-cherez-POST-zapros-api-v1-orders-pri-otsutstvuyushem-parametre-zaprosa


 
