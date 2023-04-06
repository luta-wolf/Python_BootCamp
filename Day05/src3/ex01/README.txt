- Создать виртуальное окружение в папке с продуктом
        python3 -m venv venv

- Активировать виртуальное окружение
        . venv/bin/activate     (выйти из ВО "deactivate")

- Обновить pip
        pip install --upgrade pip

- Установить flask
        pip install -r requirements.txt

- Запустить сервер
        flask --app screwdriver.py run --host=127.0.0.1 --port=8888

- Открыть в браузере адрес http://127.0.0.1:8888

- Сначала "обзор" (для выбора файла), затем "загрузить для скачивания"

